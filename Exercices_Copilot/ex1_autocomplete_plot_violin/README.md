# 🎯 Exercice 1 : Autocomplétion GitHub Copilot

## Objectif
Tester l'autocomplétion de GitHub Copilot en créant un violin plot.

## 📁 Fichiers
- `data.tsv` : données (condition, expression)
- `exercice_copilot.py` : **← TRAVAILLEZ DANS CE FICHIER**
- `consignes.ipynb` : instructions détaillées
- `README.md` : ce guide rapide

## 🚀 Guide rapide

### 1. Imports
```python
import pandas  # Copilot devrait suggérer "as pd"
import seaborn  # Copilot devrait suggérer "as sns"  
import matplotlib  # Copilot devrait suggérer ".pyplot as plt"
```

### 2. Données
```python
df = pd.read_  # Copilot devrait proposer read_csv avec sep='\t'
```

### 3. Visualisation
```python
plt.figure(figsize=  # Copilot proposera une taille
sns.violin  # Copilot proposera les bons paramètres
plt.title('  # Copilot proposera un titre approprié
plt.show  # Copilot ajoutera les parenthèses
```

## 💡 Structure des données
```
condition	expression
control	1.5
treatment	3.4
control	1.8
treatment	3.8
```

## ✨ Tests à faire
- Changez `data.tsv` en `data.csv` → observez les suggestions
- Remplacez `violin` par `box` → voyez les alternatives
- Ajoutez des commentaires descriptifs → améliore les suggestions

---
**Conseil** : Tapez lentement et observez les suggestions de Copilot !
