"""
Exercice 2 : Chat et édition de code avec GitHub Copilot
======================================================

PROMPTS À COPIER-COLLER DANS COPILOT CHAT :
==========================================

1. NORMALISATION DES DONNÉES :
"En utilisant scikit-learn, peux-tu ajouter une étape de normalisation Z-score sur les colonnes numériques avec StandardScaler avant la visualisation ?"

2. CHANGEMENT DE LIBRAIRIE :
"Peux-tu remplacer la visualisation Matplotlib/Seaborn par un graphique interactif avec Plotly ?"

3. SAUVEGARDE DU GRAPHIQUE :
"Comment puis-je sauvegarder ce graphique Plotly dans un fichier HTML nommé 'graph.html' ?"

PROMPTS BONUS :
==============
"Ajoute une analyse statistique pour comparer les groupes control vs treatment"
"Crée un dashboard avec plusieurs graphiques pour explorer toutes les variables"
"Peux-tu refactoriser ce code en utilisant des fonctions pour le rendre plus modulaire ?"
"Ajoute des docstrings et des commentaires détaillés à ce code"

DONNÉES : data.csv 
- Colonnes : sample, condition (control/treatment), gene_A, gene_B, gene_C

INSTRUCTIONS :
1. Ouvrez Copilot Chat (icône chat ou Ctrl+Shift+I)
2. Sélectionnez le code concerné avant chaque demande
3. Copiez-collez les prompts ci-dessus un par un
4. Appliquez les modifications suggérées
5. Testez le code après chaque changement
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Script de départ pour l'exercice 2
# TODO: Utiliser Copilot Chat pour améliorer ce code

# 1. Charger les données
df = pd.read_csv('data.csv')

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
