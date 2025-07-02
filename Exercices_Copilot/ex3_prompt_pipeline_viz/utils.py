"""
Fonctions utilitaires pour l'analyse des données biologiques
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Optional


def load_and_validate_csv(file) -> Tuple[pd.DataFrame, List[str]]:
    """
    Charge et valide un fichier CSV.
    
    Args:
        file: Fichier uploadé via Streamlit
        
    Returns:
        Tuple[pd.DataFrame, List[str]]: DataFrame et liste des erreurs
    """
    errors = []
    
    try:
        df = pd.read_csv(file)
        
        # Vérifications de base
        if df.empty:
            errors.append("Le fichier est vide")
            return df, errors
            
        if df.shape[0] < 2:
            errors.append("Le fichier doit contenir au moins 2 lignes de données")
            
        # Vérification des colonnes manquantes
        if df.isnull().all().any():
            empty_cols = df.columns[df.isnull().all()].tolist()
            errors.append(f"Colonnes entièrement vides : {empty_cols}")
            
        return df, errors
        
    except Exception as e:
        errors.append(f"Erreur lors du chargement du fichier : {str(e)}")
        return pd.DataFrame(), errors


def detect_column_types(df: pd.DataFrame) -> Dict[str, List[str]]:
    """
    Détecte automatiquement les types de colonnes.
    
    Args:
        df: DataFrame à analyser
        
    Returns:
        Dict contenant les listes de colonnes par type
    """
    categorical_cols = []
    numerical_cols = []
    id_cols = []
    
    for col in df.columns:
        # Colonnes d'identifiant
        if 'id' in col.lower() or col.lower() in ['sample', 'patient', 'subject']:
            id_cols.append(col)
        # Colonnes numériques
        elif pd.api.types.is_numeric_dtype(df[col]):
            numerical_cols.append(col)
        # Colonnes catégorielles
        elif df[col].dtype == 'object' or df[col].nunique() <= 10:
            categorical_cols.append(col)
        else:
            # Par défaut, traiter comme numérique si possible
            try:
                pd.to_numeric(df[col])
                numerical_cols.append(col)
            except:
                categorical_cols.append(col)
    
    return {
        'categorical': categorical_cols,
        'numerical': numerical_cols,
        'id': id_cols
    }


def calculate_statistics(df: pd.DataFrame, group_col: str, numerical_cols: List[str]) -> pd.DataFrame:
    """
    Calcule les statistiques descriptives par groupe.
    
    Args:
        df: DataFrame avec les données
        group_col: Nom de la colonne de groupement
        numerical_cols: Liste des colonnes numériques
        
    Returns:
        DataFrame avec les statistiques
    """
    stats = []
    
    for col in numerical_cols:
        for group in df[group_col].unique():
            group_data = df[df[group_col] == group][col]
            
            stats.append({
                'Variable': col,
                'Groupe': group,
                'N': len(group_data),
                'Moyenne': group_data.mean(),
                'Médiane': group_data.median(),
                'Écart-type': group_data.std(),
                'Min': group_data.min(),
                'Max': group_data.max(),
                'Q1': group_data.quantile(0.25),
                'Q3': group_data.quantile(0.75)
            })
    
    return pd.DataFrame(stats)


def perform_statistical_tests(df: pd.DataFrame, group_col: str, numerical_cols: List[str]) -> pd.DataFrame:
    """
    Effectue des tests statistiques entre les groupes.
    
    Args:
        df: DataFrame avec les données
        group_col: Nom de la colonne de groupement
        numerical_cols: Liste des colonnes numériques
        
    Returns:
        DataFrame avec les résultats des tests
    """
    from scipy import stats
    
    results = []
    groups = df[group_col].unique()
    
    if len(groups) != 2:
        return pd.DataFrame()  # Pour simplifier, on ne traite que 2 groupes
    
    group1_name, group2_name = groups
    
    for col in numerical_cols:
        group1_data = df[df[group_col] == group1_name][col].dropna()
        group2_data = df[df[group_col] == group2_name][col].dropna()
        
        if len(group1_data) > 0 and len(group2_data) > 0:
            # Test de normalité (Shapiro-Wilk)
            _, p_norm1 = stats.shapiro(group1_data) if len(group1_data) <= 5000 else (0, 0.05)
            _, p_norm2 = stats.shapiro(group2_data) if len(group2_data) <= 5000 else (0, 0.05)
            
            # Test approprié selon la normalité
            if p_norm1 > 0.05 and p_norm2 > 0.05:
                # Données normales : t-test
                statistic, p_value = stats.ttest_ind(group1_data, group2_data)
                test_used = "T-test"
            else:
                # Données non-normales : Mann-Whitney U
                statistic, p_value = stats.mannwhitneyu(group1_data, group2_data, alternative='two-sided')
                test_used = "Mann-Whitney U"
            
            # Calcul de l'effet size (Cohen's d)
            pooled_std = np.sqrt((group1_data.var() + group2_data.var()) / 2)
            cohens_d = (group1_data.mean() - group2_data.mean()) / pooled_std if pooled_std > 0 else 0
            
            results.append({
                'Variable': col,
                'Test': test_used,
                'Statistique': statistic,
                'P-value': p_value,
                'Significatif (α=0.05)': 'Oui' if p_value < 0.05 else 'Non',
                "Cohen's d": cohens_d,
                'Taille effet': interpret_effect_size(abs(cohens_d))
            })
    
    return pd.DataFrame(results)


def interpret_effect_size(cohens_d: float) -> str:
    """
    Interprète la taille de l'effet selon Cohen's d.
    
    Args:
        cohens_d: Valeur absolue de Cohen's d
        
    Returns:
        Interprétation textuelle
    """
    if cohens_d < 0.2:
        return "Négligeable"
    elif cohens_d < 0.5:
        return "Petit"
    elif cohens_d < 0.8:
        return "Moyen"
    else:
        return "Grand"


def filter_dataframe(df: pd.DataFrame, filters: Dict) -> pd.DataFrame:
    """
    Applique des filtres au DataFrame.
    
    Args:
        df: DataFrame à filtrer
        filters: Dictionnaire des filtres
        
    Returns:
        DataFrame filtré
    """
    filtered_df = df.copy()
    
    for col, values in filters.items():
        if col in df.columns and values:
            if df[col].dtype == 'object':
                filtered_df = filtered_df[filtered_df[col].isin(values)]
            else:
                min_val, max_val = values
                filtered_df = filtered_df[
                    (filtered_df[col] >= min_val) & 
                    (filtered_df[col] <= max_val)
                ]
    
    return filtered_df
