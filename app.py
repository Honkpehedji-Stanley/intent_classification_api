from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Intent Classification API",
    description="API pour classifier les intentions TRIP/NOT_TRIP",
    version="1.0.0"
)

# Modèle global
model = None
tokenizer = None
id2label = {0: "NOT_TRIP", 1: "TRIP"}

# Schémas Pydantic
class TranslationRequest(BaseModel):
    translation: str

class ClassificationResponse(BaseModel):
    class_: str
    sentence: str
    
    class Config:
        # Permet d'utiliser 'class' dans le JSON
        fields = {'class_': 'class'}

@app.on_event("startup")
async def load_model():
    """Charge le modèle au démarrage de l'application"""
    global model, tokenizer
    try:
        logger.info("Chargement du modèle...")
        model_path = "./intent_model_final"  # Modèle local (DistilCamemBERT ~260 Mo)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSequenceClassification.from_pretrained(model_path)
        model.eval()
        logger.info("Modèle chargé avec succès!")
    except Exception as e:
        logger.error(f"Erreur lors du chargement du modèle: {e}")
        raise

@app.get("/")
async def root():
    """Endpoint racine pour vérifier que l'API fonctionne"""
    return {
        "message": "Intent Classification API est en ligne",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Vérification de la santé de l'API"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/classify", response_model=ClassificationResponse)
async def classify_intent(request: TranslationRequest):
    """
    Classifie l'intention d'une phrase en français
    
    Args:
        request: Objet contenant la traduction française
    
    Returns:
        ClassificationResponse: Objet contenant la classe et la phrase
    """
    if model is None or tokenizer is None:
        raise HTTPException(
            status_code=503,
            detail="Le modèle n'est pas encore chargé"
        )
    
    if not request.translation or not request.translation.strip():
        raise HTTPException(
            status_code=400,
            detail="La traduction ne peut pas être vide"
        )
    
    try:
        # Tokenization
        inputs = tokenizer(
            request.translation,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        )
        
        # Prédiction
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class_id = torch.argmax(logits, dim=1).item()
        
        # Mapping vers le label
        predicted_label = id2label.get(predicted_class_id, "UNKNOWN")
        
        logger.info(f"Classification: '{request.translation}' -> {predicted_label}")
        
        return ClassificationResponse(
            class_=predicted_label,
            sentence=request.translation
        )
    
    except Exception as e:
        logger.error(f"Erreur lors de la classification: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la classification: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
