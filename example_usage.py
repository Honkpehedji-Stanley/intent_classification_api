"""
Exemple d'utilisation de l'API de classification d'intentions
"""
import requests
import json

# Configuration
API_URL = "http://localhost:8000/classify"

def classify_text(text):
    """
    Envoie une phrase à l'API pour classification
    
    Args:
        text (str): Phrase en français à classifier
        
    Returns:
        dict: Résultat de la classification
    """
    payload = {"translation": text}
    
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Lève une exception si le status n'est pas 200
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Exemples d'utilisation
if __name__ == "__main__":
    # Exemple 1: Phrase liée aux voyages
    result1 = classify_text("Je veux réserver un vol pour Paris")
    print("Exemple 1:")
    print(json.dumps(result1, indent=2, ensure_ascii=False))
    print()
    
    # Exemple 2: Phrase non liée aux voyages
    result2 = classify_text("Quel temps fait-il aujourd'hui?")
    print("Exemple 2:")
    print(json.dumps(result2, indent=2, ensure_ascii=False))
    print()
    
    # Exemple 3: Liste de phrases à classifier
    phrases = [
        "Réserver un hôtel à Lyon",
        "Comment vas-tu?",
        "Je voudrais partir en vacances",
        "Quelle est la capitale de la France?"
    ]
    
    print("Exemple 3 - Classification en batch:")
    for phrase in phrases:
        result = classify_text(phrase)
        if "error" not in result:
            print(f"'{phrase}' -> {result['class']}")
        else:
            print(f"Erreur pour '{phrase}': {result['error']}")
