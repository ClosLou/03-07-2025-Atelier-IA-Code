"""
Exercice 3 : Projet piloté par prompt (Chain of Thought)
======================================================

PROMPT OPTIMISÉ À COPIER-COLLER DANS COPILOT CHAT (AGENT):
=================================================

Je veux créer une application complète de visualisation de données biologiques. 
Voici ma réflexion étape par étape :

ÉTAPE 1 - ANALYSE DU BESOIN :
- J'ai un fichier CSV avec des données biologiques (sample_id, group, gene_expr_1, gene_expr_2, protein_level_1, protein_level_2)
- Je veux analyser automatiquement les patterns entre groupes (Healthy vs Diseased)
- Je veux une interface utilisateur simple pour charger différents fichiers

ÉTAPE 2 - ARCHITECTURE TECHNIQUE :
- Backend : Python avec pandas pour l'analyse des données
- Visualisation : seaborn/plotly pour les graphiques en violon
- Frontend : Streamlit pour l'interface web
- Détection automatique des colonnes catégorielles vs numériques

ÉTAPE 3 - FONCTIONNALITÉS REQUISES :
1. Upload de fichier CSV via interface web
2. Détection automatique de la structure des données
3. Génération de violin plots pour chaque variable numérique vs catégorielle
4. Interface interactive pour explorer les résultats
5. Option de téléchargement des graphiques

ÉTAPE 4 - LIVRABLES :
Peux-tu créer ces fichiers :
- `app.py` : Application Streamlit complète avec toutes les fonctionnalités
- `requirements.txt` : Toutes les dépendances nécessaires
- `README.md` : Documentation avec instructions d'installation et d'usage
- `utils.py` : Fonctions utilitaires pour l'analyse des données

CONTRAINTES TECHNIQUES :
- Code Python propre et commenté
- Gestion d'erreurs pour fichiers incorrects
- Interface responsive et intuitive
- Support des formats CSV standards

DONNÉES TEST DISPONIBLES :
Le fichier data.csv contient : sample_id, group (Healthy/Diseased), gene_expr_1, gene_expr_2, protein_level_1, protein_level_2

Peux-tu générer cette application complète ?

DONNÉES : data.csv 
- Structure : sample_id, group (Healthy/Diseased), gene_expr_1, gene_expr_2, protein_level_1, protein_level_2
- Objectif : Application Streamlit pour analyse interactive

INSTRUCTIONS :
1. Ouvrez Copilot Chat (icône chat ou Ctrl+Shift+I)
2. Copiez-collez le prompt optimisé ci-dessus
3. Acceptez la création des fichiers proposés
4. Testez l'application avec le fichier data.csv fourni

COMMANDES POUR TESTER :
pip install -r requirements.txt
streamlit run app.py
"""
