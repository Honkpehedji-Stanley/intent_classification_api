# 🤖 Configuration du Modèle

## Taille du modèle

Le modèle CamemBERT est stocké dans `intent_model_final/` et pèse environ **400-500 MB**. Il est exclu du repository Git pour éviter les problèmes de taille.

## ⬇️ Installation du modèle

### Option 1: Récupération locale
Si vous clonez ce repository localement, le modèle doit être présent dans le dossier `intent_model_final/` où il fonctionnera.

### Option 2: Téléchargement depuis Hugging Face (optionnel)
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "vôtre-model-huggingface"  # À remplacer par le nom réel
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Sauvegarder localement
model.save_pretrained("./intent_model_final")
tokenizer.save_pretrained("./intent_model_final")
```

### Option 3: Git LFS (Git Large File Storage)
Pour versionner les gros fichiers avec Git :

```bash
# Installation
git lfs install

# Tracker le modèle
git lfs track "intent_model_final/*.safetensors"
git lfs track "intent_model_final/*.bin"

# Ajouter et commiter
git add intent_model_final/
git add .gitattributes
git commit -m "Add model with Git LFS"
```

## 📦 Fichiers du modèle

```
intent_model_final/
├── config.json              # Configuration du modèle
├── model.safetensors        # Poids du modèle (~400 MB)
├── tokenizer.json           # Configuration du tokenizer
├── tokenizer_config.json    # Config recommandations
├── special_tokens_map.json  # Tokens spéciaux
├── sentencepiece.bpe.model  # Modèle SentencePiece
└── added_tokens.json        # Tokens ajoutés
```

## 🚀 Déploiement en production

### Docker (recommandé)
Le `Dockerfile` inclut automatiquement le modèle dans l'image :

```bash
docker build -t intent-classification-api .
docker run -p 8000:8000 intent-classification-api
```

### Heroku / Railway / Render
- Le modèle doit être cloné localement avant le déploiement
- Ou téléchargé automatiquement au démarrage (voir alternative ci-dessus)
- Assurez-vous d'avoir au moins 1 GB de stockage

## ✅ Vérification

Pour vérifier que le modèle est correctement chargé :

```bash
python -c "from transformers import AutoModel; m = AutoModel.from_pretrained('./intent_model_final'); print('✓ Modèle chargé')"
```
