# Installation Guide - GitHub Copilot Workshop
## Guide d'installation - Atelier GitHub Copilot

### 📋 Prérequis / Prerequisites

- Python 3.8 ou plus récent / Python 3.8 or newer
- pip (installé avec Python / installed with Python)
- GitHub Copilot activé dans VS Code / GitHub Copilot enabled in VS Code

### 🚀 Installation rapide / Quick Installation

Pour installer toutes les dépendances nécessaires pour tous les exercices :
*To install all dependencies needed for all exercises:*

```bash
pip install -r requirements.txt
```

### 📁 Installation par exercice / Per-Exercise Installation

Si vous souhaitez travailler sur un exercice spécifique :
*If you want to work on a specific exercise:*

#### Exercice 1 - Autocomplétion Plot Violin
```bash
cd "Exercices_Copilot/ex1_autocomplete_plot_violin"
pip install -r requirements.txt
```

#### Exercice 2 - Chat Edit Clean
```bash
cd "Exercices_Copilot/ex2_chat_edit_clean"
pip install -r requirements.txt
```

#### Exercice 3 - Prompt Pipeline Visualization
```bash
cd "Exercices_Copilot/ex3_prompt_pipeline_viz"
pip install -r requirements.txt
```

### 🔧 Installation alternative / Alternative Installation

Si vous préférez installer manuellement les librairies principales :
*If you prefer to manually install the main libraries:*

```bash
# Librairies de base / Core libraries
pip install pandas numpy matplotlib seaborn

# Pour l'exercice 2 / For exercise 2
pip install plotly scikit-learn

# Pour l'exercice 3 / For exercise 3
pip install streamlit

# Support Jupyter (optionnel) / Jupyter support (optional)
pip install jupyter ipykernel
```

### ✅ Vérification de l'installation / Installation Verification

Pour vérifier que tout est correctement installé :
*To verify everything is properly installed:*

```python
# Test rapide / Quick test
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("✅ Installation réussie / Installation successful!")
```

### 🆘 Dépannage / Troubleshooting

#### Problème avec Plotly / Issue with Plotly
Si les graphiques Plotly ne s'affichent pas dans VS Code :
*If Plotly graphs don't display in VS Code:*

1. Vérifiez l'installation : `pip install plotly`
2. Ouvrez le fichier `graph.html` généré dans votre navigateur

#### Problème avec Streamlit / Issue with Streamlit
Pour l'exercice 3, si Streamlit ne démarre pas :
*For exercise 3, if Streamlit doesn't start:*

```bash
# Vérifiez l'installation / Check installation
pip install --upgrade streamlit

# Lancez l'application / Run the application
streamlit run app.py
```

#### Problème de versions / Version conflicts
En cas de conflit de versions :
*In case of version conflicts:*

```bash
# Créez un environnement virtuel / Create virtual environment
python -m venv copilot_workshop
# Windows
copilot_workshop\Scripts\activate
# macOS/Linux
source copilot_workshop/bin/activate

# Installez les dépendances / Install dependencies
pip install -r requirements.txt
```

### 📝 Notes importantes / Important Notes

- Tous les exercices utilisent des chemins relatifs avec `os.path` pour la compatibilité multiplateforme
  *All exercises use relative paths with `os.path` for cross-platform compatibility*

- Les données sont fournies dans chaque dossier d'exercice
  *Data files are provided in each exercise folder*

- GitHub Copilot doit être activé dans VS Code pour profiter pleinement des exercices
  *GitHub Copilot must be enabled in VS Code to fully benefit from the exercises*
