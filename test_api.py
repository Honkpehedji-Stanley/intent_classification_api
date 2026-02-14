"""
Script de test pour l'API de classification d'intentions
"""
import requests
import json

# URL de base de l'API
BASE_URL = "http://localhost:8000"

def test_health():
    """Test du endpoint health"""
    print("🔍 Test du endpoint /health...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Réponse: {response.json()}\n")

def test_classify(text):
    """Test du endpoint classify"""
    print(f"🔍 Test de classification pour: '{text}'")
    
    data = {"translation": text}
    response = requests.post(
        f"{BASE_URL}/classify",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Résultat: {json.dumps(result, indent=2, ensure_ascii=False)}\n")
    else:
        print(f"❌ Erreur: {response.text}\n")
    
    return response

if __name__ == "__main__":
    print("=" * 60)
    print("Test de l'API de Classification d'Intentions")
    print("=" * 60 + "\n")
    
    # Test health check
    try:
        test_health()
    except requests.exceptions.ConnectionError:
        print("❌ Erreur: Impossible de se connecter à l'API.")
        print("Assurez-vous que l'API est démarrée avec: python app.py\n")
        exit(1)
    
    # Tests de classification
    test_phrases = [
        "Je veux réserver un vol pour Paris",
        "Quel temps fait-il aujourd'hui?",
        "Réserver un hôtel à Lyon",
        "Comment vas-tu?",
        "Je voudrais partir en vacances",
        "Quelle est la capitale de la France?",
        "Acheter des billets d'avion",
        "Bonjour, comment allez-vous?"
    ]
    
    print("📝 Tests de classification:\n")
    for phrase in test_phrases:
        test_classify(phrase)
    
    print("=" * 60)
    print("Tests terminés!")
    print("=" * 60)
