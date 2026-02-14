# API de Classification d'Intentions

Une API FastAPI simple pour classifier des phrases françaises en intentions **TRIP** ou **NOT_TRIP** en utilisant un modèle CamemBERT fine-tuné.

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip

## 🚀 Installation

1. **Cloner le projet** (ou télécharger les fichiers)

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Démarrage de l'API

Pour lancer l'API en local :

```bash
python app.py
```

Ou avec uvicorn directement :

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

L'API sera accessible sur : `http://localhost:8000`

## 📖 Utilisation

### Endpoints disponibles

#### 1. **GET /** - Page d'accueil
Vérifier que l'API est en ligne.

```bash
curl http://localhost:8000/
```

#### 2. **GET /health** - Health Check
Vérifier la santé de l'API et si le modèle est chargé.

```bash
curl http://localhost:8000/health
```

#### 3. **POST /classify** - Classification d'intention
Classifier une phrase française.

**Format de la requête :**
```json
{
  "translation": "Je veux réserver un vol pour Paris"
}
```

**Format de la réponse :**
```json
{
  "class": "TRIP",
  "sentence": "Je veux réserver un vol pour Paris"
}
```

### Exemples d'utilisation

#### Avec curl :
```bash
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{"translation": "Je veux réserver un hôtel"}'
```

#### Avec Python (requests) :
```python
import requests

url = "http://localhost:8000/classify"
data = {"translation": "Je voudrais partir en vacances"}

response = requests.post(url, json=data)
print(response.json())
```

#### Avec JavaScript (fetch) :
```javascript
fetch('http://localhost:8000/classify', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    translation: 'Réserver un billet d\'avion'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 📚 Documentation interactive

FastAPI génère automatiquement une documentation interactive :

- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

## 🐳 Déploiement

### Option 1: Docker

#### Construire l'image Docker :
```bash
docker build -t intent-classification-api .
```

#### Lancer le conteneur :
```bash
docker run -p 8000:8000 intent-classification-api
```

L'API sera accessible sur : `http://localhost:8000`

### Option 2: Services Cloud

#### Déploiement sur Heroku :
1. Créer un `Procfile` :
   ```
   web: uvicorn app:app --host 0.0.0.0 --port $PORT
   ```

2. Déployer :
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku create nom-de-votre-app
   git push heroku main
   ```

#### Déploiement sur Railway :
1. Connecter votre repo GitHub
2. Railway détectera automatiquement Python
3. L'app sera déployée automatiquement

#### Déploiement sur Render :
1. Créer un nouveau Web Service
2. Connecter votre repo
3. Build Command : `pip install -r requirements.txt`
4. Start Command : `uvicorn app:app --host 0.0.0.0 --port $PORT`

## 📁 Structure du projet

```
intent_classification_api/
│
├── app.py                      # Application FastAPI principale
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation
│
└── intent_model_final/         # Modèle CamemBERT
    ├── config.json
    ├── model.safetensors
    ├── tokenizer.json
    ├── tokenizer_config.json
    ├── special_tokens_map.json
    ├── sentencepiece.bpe.model
    └── added_tokens.json
```

## 🔧 Configuration

Les labels de classification sont définis dans `app.py` :
```python
id2label = {0: "NOT_TRIP", 1: "TRIP"}
```

Pour modifier les labels, ajustez ce dictionnaire selon votre modèle.

## ⚠️ Remarques importantes

- Le modèle est chargé au démarrage de l'application (peut prendre quelques secondes)
- La longueur maximale des phrases est de 512 tokens
- Pour la production, considérez l'ajout de rate limiting et d'authentification

## 📝 License

Ce projet est fourni tel quel pour usage personnel ou professionnel.
