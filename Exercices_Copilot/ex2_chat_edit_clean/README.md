# 💬 Exercice 2 : Chat et édition de code

## Objectif
Utiliser le **chat GitHub Copilot** pour améliorer un script Python existant.

## 📁 Fichiers
- `data.csv` : données d'expression génique (sample, condition, gene_A, gene_B, gene_C)
- `script_base.py` : **← TRAVAILLEZ DANS CE FICHIER**
- `consignes.ipynb` : instructions détaillées
- `README.md` : ce guide rapide

## 🚀 Guide rapide

### 1. Ouvrir Copilot Chat
- Icône 💬 dans la barre d'activité à gauche
- Ou `Ctrl+Shift+I` (Windows) / `Cmd+Shift+I` (Mac)

### 2. Demandes à tester

#### 🔍 **Analyse générale**
Sélectionnez tout le code et demandez :
```
"Peux-tu analyser ce code et suggérer des améliorations ?"
```

#### 📊 **Normalisation des données**
```
"En utilisant scikit-learn, peux-tu ajouter une étape de normalisation Z-score sur les colonnes numériques avec StandardScaler avant la visualisation ?"
```

#### 🎨 **Changer de librairie**
```
"Peux-tu remplacer la visualisation Matplotlib/Seaborn par un graphique interactif avec Plotly ?"
```

#### 💾 **Sauvegarde**
```
"Comment puis-je sauvegarder ce graphique Plotly dans un fichier HTML nommé 'graph.html' ?"
```

### 3. Tests bonus
- `"Ajoute une analyse statistique pour comparer les groupes"`
- `"Crée un dashboard avec plusieurs graphiques"`
- `"Refactorise ce code en utilisant des fonctions"`
- `"Ajoute des docstrings et commentaires détaillés"`

## 📊 Structure des données
```csv
sample,condition,gene_A,gene_B,gene_C
S1,control,10.2,5.4,12.1
S4,treatment,25.3,8.2,15.3
```

## 💡 Conseils
- **Sélectionnez le code** avant de poser vos questions
- **Soyez spécifique** dans vos demandes
- **Testez** chaque modification avant de continuer
- **Itérez** si le résultat n'est pas parfait

---
**Objectif** : Apprendre à collaborer efficacement avec Copilot Chat !
