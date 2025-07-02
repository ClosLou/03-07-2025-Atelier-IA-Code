"""
Exercice 2 : Chat et édition de code avec GitHub Copilot
======================================================

PRÉREQUIS D'INSTALLATION :
========================
Avant de commencer, installez les librairies nécessaires :
pip install pandas plotly scikit-learn matplotlib seaborn

PROMPTS À COPIER-COLLER DANS COPILOT CHAT :
==========================================

1. NORMALISATION DES DONNÉES :
"En utilisant scikit-learn, peux-tu ajouter une étape de normalisation Z-score sur les colonnes numériques avec StandardScaler avant la visualisation ?"

2. CHANGEMENT DE LIBRAIRIE AVEC GESTION D'AFFICHAGE :
"Peux-tu remplacer la visualisation Matplotlib/Seaborn par un graphique interactif avec Plotly ? Assure-toi d'inclure à la fois fig.show() et fig.write_html('graph.html') pour garantir l'affichage"


PROMPTS BONUS :
==============
"Ajoute une analyse statistique pour comparer les groupes control vs treatment"
"Crée un dashboard avec plusieurs graphiques pour explorer toutes les variables"
"Peux-tu refactoriser ce code en utilisant des fonctions pour le rendre plus modulaire ?"
"Ajoute des docstrings et des commentaires détaillés à ce code"

DONNÉES : data.csv 
- Colonnes : sample, condition (control/treatment), gene_A, gene_B, gene_C

INSTRUCTIONS DÉTAILLÉES :
=======================
1. Vérifiez que toutes les librairies sont installées
2. Ouvrez Copilot Chat (icône chat ou Ctrl+Shift+I)
3. Sélectionnez le code concerné avant chaque demande
4. Copiez-collez les prompts ci-dessus un par un (dans l'ordre)
5. Appliquez les modifications suggérées
6. Testez le code après chaque changement
7. Si Plotly ne s'affiche pas : vérifiez le fichier graph.html généré

DÉPANNAGE PLOTLY :
================
- Si le graphique ne s'affiche pas dans VS Code ouvrez graph.html dans votre navigateur
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Script de départ pour l'exercice 2
# TODO: Utiliser Copilot Chat pour améliorer ce code

# 1. Charger les données avec gestion des chemins
data_file = os.path.join(os.path.dirname(__file__), 'data.csv')
df = pd.read_csv(data_file)

# 2. Visualisation simple avec Matplotlib/Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='gene_A', y='gene_B', hue='condition')
plt.title('Expression de Gene_A vs Gene_B')
plt.xlabel('Expression Gene A')
plt.ylabel('Expression Gene B')
plt.grid(True)
plt.show()

# Le participant utilisera le chat Copilot pour modifier ce script.
# ÉTAPES À SUIVRE :
# 1. Sélectionnez tout le code ci-dessus
# 2. Copiez le premier prompt depuis le haut du fichier
# 3. Collez dans Copilot Chat et appliquez les suggestions
# 4. Répétez avec les autres prompts dans l'ordre
