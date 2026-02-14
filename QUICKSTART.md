# 🚀 Guide de Démarrage Rapide

## Installation et Lancement en 3 étapes

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer l'API
```bash
python app.py
```

L'API démarre sur : **http://localhost:8000**

### 3. Tester l'API

#### Option A: Documentation interactive
Ouvrez dans votre navigateur : http://localhost:8000/docs

#### Option B: Script de test
```bash
python test_api.py
```

#### Option C: Curl
```bash
curl -X POST "http://localhost:8000/classify" ^
  -H "Content-Type: application/json" ^
  -d "{\"translation\": \"Je veux réserver un vol\"}"
```

## 📥 Format d'entrée
```json
{
  "translation": "Je veux réserver un vol pour Paris"
}
```

## 📤 Format de sortie
```json
{
  "class": "TRIP",
  "sentence": "Je veux réserver un vol pour Paris"
}
```

## 💡 Classes possibles
- **TRIP** : Intention liée à un voyage/voyage
- **NOT_TRIP** : Intention non liée à un voyage

---

Pour plus de détails, consultez le [README.md](README.md) complet.
