# 🚀 Exercice 3 : Projet piloté par prompt

## Objectif
Générer une **application Streamlit complète** avec GitHub Copilot en utilisant un prompt structuré (chain of thought).

## 📁 Fichiers
- `data.csv` : données biologiques (Healthy vs Diseased)
- `projet_consignes.py` : **← PROMPT OPTIMISÉ À COPIER**
- `consignes.ipynb` : instructions détaillées
- `README.md` : ce guide rapide

## 🚀 Guide ultra-rapide

### 1. Copier le prompt
Ouvrez `projet_consignes.py` et copiez le prompt complet (avec chain of thought).

### 2. Lancer Copilot Chat
- Icône chat ou `Ctrl+Shift+I`
- Collez le prompt et envoyez

### 3. Accepter les fichiers
Copilot proposera de créer :
- `app.py` (application principale)
- `requirements.txt` (dépendances)
- `README.md` (documentation)
- `utils.py` (utilitaires)

### 4. Tester l'application
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 5. Charger les données
Uploadez le fichier `data.csv` dans l'interface web.

## 📊 Données disponibles
```csv
sample_id,group,gene_expr_1,gene_expr_2,protein_level_1,protein_level_2
ID01,Diseased,120.5,88.2,45.1,203.4
ID03,Healthy,95.2,92.3,33.8,180.9
```

## 🎯 Chain of Thought
Le prompt guide Copilot à travers :
1. **Analyse** du besoin
2. **Architecture** technique  
3. **Fonctionnalités** requises
4. **Livrables** attendus

## ✨ Résultat attendu
Application web interactive avec :
- Upload de fichiers CSV
- Détection automatique des colonnes
- Génération de violin plots
- Interface Streamlit responsive

---
**Conseil** : La qualité du prompt détermine la qualité du résultat !
