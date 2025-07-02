# BioViz - Analyseur de Données Biologiques 🧬

## Description

BioViz est une application web interactive développée avec Streamlit pour l'analyse et la visualisation de données biologiques. Elle permet de détecter automatiquement les patterns entre différents groupes (ex: Healthy vs Diseased) et de générer des visualisations interactives.

## Fonctionnalités principales

### 📊 Analyse automatique des données
- Détection automatique des types de colonnes (catégorielles, numériques, identifiants)
- Calcul de statistiques descriptives par groupe
- Tests statistiques automatiques (t-test, Mann-Whitney U)
- Calcul de la taille d'effet (Cohen's d)

### 📈 Visualisations interactives
- **Violin plots** : Distribution et densité des données
- **Box plots** : Quartiles et valeurs aberrantes
- **Strip plots** : Points de données individuels
- **Matrice de corrélation** : Relations entre variables
- Personnalisation des couleurs et options d'affichage

### 🔧 Interface utilisateur intuitive
- Upload de fichiers CSV via glisser-déposer
- Filtres interactifs pour explorer les données
- Métriques en temps réel
- Téléchargement des graphiques et statistiques
- Interface responsive et moderne

### 🛡️ Gestion d'erreurs robuste
- Validation automatique des fichiers
- Messages d'erreur explicites
- Gestion des données manquantes
- Support des formats CSV standards

## Installation

### Prérequis
- Python 3.8 ou plus récent
- pip (gestionnaire de paquets Python)

### Instructions d'installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd votre-repertoire
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

4. **Ouvrir dans le navigateur**
   L'application s'ouvrira automatiquement à l'adresse : `http://localhost:8501`

## Structure du projet

```
📁 BioViz/
├── 📄 app.py              # Application Streamlit principale
├── 📄 utils.py            # Fonctions utilitaires pour l'analyse
├── 📄 requirements.txt    # Dépendances Python
├── 📄 README.md          # Documentation (ce fichier)
└── 📄 data.csv           # Données d'exemple
```

## Format des données

### Structure attendue

Votre fichier CSV doit contenir :
- **Une colonne d'identifiant** (ex: `sample_id`, `patient_id`)
- **Une colonne de groupement** (ex: `group`, `condition`, `treatment`)
- **Une ou plusieurs colonnes de variables numériques** (ex: `gene_expr_1`, `protein_level_1`)

### Exemple de fichier CSV

```csv
sample_id,group,gene_expr_1,gene_expr_2,protein_level_1,protein_level_2
ID01,Healthy,95.2,92.3,33.8,180.9
ID02,Diseased,120.5,88.2,45.1,203.4
ID03,Healthy,98.6,90.1,35.2,185.2
ID04,Diseased,125.1,85.6,47.3,210.1
```

## Utilisation

### 1. Chargement des données
- Utilisez le bouton "Choisissez un fichier CSV" dans la barre latérale
- Ou cliquez sur "Utiliser les données d'exemple" pour tester l'application

### 2. Configuration de l'analyse
- Sélectionnez la colonne de groupement (variable catégorielle)
- Choisissez les variables numériques à analyser
- Appliquez des filtres optionnels si nécessaire

### 3. Exploration des résultats
- **Aperçu des données** : Métriques générales et premières lignes
- **Statistiques descriptives** : Moyennes, médianes, écarts-types par groupe
- **Tests statistiques** : Comparaisons entre groupes avec p-values
- **Visualisations** : Graphiques interactifs personnalisables

### 4. Export des résultats
- Téléchargez les statistiques au format CSV
- Sauvegardez les graphiques en PNG
- Partagez l'URL de l'application pour collaborer

## Dépendances

- **streamlit** (1.28.1) : Framework web pour l'interface utilisateur
- **pandas** (2.1.3) : Manipulation et analyse des données
- **plotly** (5.17.0) : Graphiques interactifs
- **seaborn** (0.13.0) : Visualisations statistiques
- **matplotlib** (3.8.2) : Graphiques statiques
- **numpy** (1.25.2) : Calculs numériques
- **scipy** (1.11.4) : Tests statistiques

## Tests statistiques automatiques

L'application effectue automatiquement les tests appropriés selon la distribution des données :

- **Test de normalité** : Shapiro-Wilk
- **Données normales** : t-test de Student
- **Données non-normales** : Test de Mann-Whitney U
- **Taille d'effet** : Cohen's d avec interprétation

## Personnalisation

### Ajouter de nouveaux types de graphiques

Modifiez la fonction `create_plot()` dans `app.py` pour ajouter de nouveaux types de visualisations.

### Personnaliser les tests statistiques

Étendez la fonction `perform_statistical_tests()` dans `utils.py` pour inclure d'autres tests.

### Modifier l'apparence

Personnalisez le CSS dans la section `st.markdown()` de `app.py`.

## Troubleshooting

### Problèmes courants

1. **Erreur de module manquant**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Port 8501 déjà utilisé**
   ```bash
   streamlit run app.py --server.port 8502
   ```

3. **Problème d'encodage CSV**
   Assurez-vous que votre fichier CSV est encodé en UTF-8

4. **Données non détectées**
   Vérifiez que votre fichier contient au moins une colonne catégorielle et une colonne numérique

### Support

Pour signaler un bug ou demander une fonctionnalité :
1. Vérifiez que toutes les dépendances sont installées
2. Testez avec les données d'exemple fournies
3. Consultez les messages d'erreur dans l'interface

## Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Poussez vers la branche
5. Ouvrez une Pull Request

## License

Ce projet est distribué sous license MIT. Voir le fichier `LICENSE` pour plus de détails.

## Crédits

Développé avec ❤️ pour l'analyse de données biologiques
- **Framework** : Streamlit
- **Visualisations** : Plotly, Seaborn
- **Analyses** : Pandas, SciPy
- **Interface** : CSS personnalisé

---

**Version** : 1.0.0  
**Dernière mise à jour** : Juillet 2025
