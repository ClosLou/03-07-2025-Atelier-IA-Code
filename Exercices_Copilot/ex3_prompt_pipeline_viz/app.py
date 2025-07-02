import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
from utils import (
    load_and_validate_csv, 
    detect_column_types, 
    calculate_statistics,
    perform_statistical_tests,
    filter_dataframe
)

# Configuration de la page
st.set_page_config(
    page_title="BioViz - Analyseur de Données Biologiques",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour améliorer l'apparence
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2e8b57;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-left: 4px solid #2e8b57;
        padding-left: 1rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stAlert {
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Fonction principale de l'application"""
    
    # En-tête principal
    st.markdown('<h1 class="main-header">🧬 BioViz - Analyseur de Données Biologiques</h1>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    **Application interactive pour l'analyse et la visualisation de données biologiques**
    
    📊 Téléchargez vos données CSV, explorez les patterns entre groupes, et générez des visualisations interactives.
    """)
    
    # Sidebar pour les paramètres
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Section d'upload de fichier
        st.subheader("📁 Chargement des données")
        uploaded_file = st.file_uploader(
            "Choisissez un fichier CSV",
            type=['csv'],
            help="Le fichier doit contenir des colonnes avec identifiants, groupes et variables numériques"
        )
        
        # Exemple de données
        if st.button("📋 Utiliser les données d'exemple"):
            st.session_state['use_example'] = True
        
        # Aide
        with st.expander("❓ Format des données attendu"):
            st.markdown("""
            **Structure recommandée :**
            - Une colonne d'identifiant (ex: sample_id, patient_id)
            - Une colonne de groupement (ex: group, condition)
            - Plusieurs colonnes de variables numériques
            
            **Exemple :**
            ```
            sample_id,group,gene_expr_1,protein_level_1
            ID01,Healthy,95.2,33.8
            ID02,Diseased,120.5,45.1
            ```
            """)
    
    # Gestion des données
    df = None
    use_example = st.session_state.get('use_example', False)
    
    if uploaded_file is not None:
        df, errors = load_and_validate_csv(uploaded_file)
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            st.success("✅ Fichier chargé avec succès !")
            st.session_state['use_example'] = False
    
    elif use_example:
        try:
            df = pd.read_csv("data.csv")
            st.success("✅ Données d'exemple chargées !")
        except FileNotFoundError:
            st.error("❌ Fichier data.csv introuvable dans le répertoire")
    
    if df is not None and not df.empty:
        analyze_data(df)
    else:
        show_welcome_screen()


def show_welcome_screen():
    """Affiche l'écran d'accueil"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ### 🚀 Bienvenue dans BioViz !
        
        Cette application vous permet d'analyser et visualiser vos données biologiques de manière interactive.
        
        **Fonctionnalités principales :**
        - 📈 Génération automatique de violin plots
        - 📊 Statistiques descriptives par groupe
        - 🔬 Tests statistiques automatiques
        - 🎯 Interface interactive et intuitive
        - 💾 Téléchargement des graphiques
        
        **Pour commencer :**
        1. Téléchargez un fichier CSV dans la barre latérale
        2. Ou utilisez les données d'exemple fournies
        3. Explorez vos données avec les visualisations interactives
        
        ---
        
        **Développé avec ❤️ pour l'analyse de données biologiques**
        """)


def analyze_data(df):
    """Analyse complète des données"""
    
    # Détection automatique des types de colonnes
    column_types = detect_column_types(df)
    
    # Informations générales sur le dataset
    st.markdown('<h2 class="section-header">📋 Aperçu des données</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Lignes", df.shape[0])
    with col2:
        st.metric("📋 Colonnes", df.shape[1])
    with col3:
        st.metric("🔢 Variables numériques", len(column_types['numerical']))
    with col4:
        st.metric("🏷️ Variables catégorielles", len(column_types['categorical']))
    
    # Affichage des premières lignes
    with st.expander("👀 Aperçu des données (premières lignes)", expanded=False):
        st.dataframe(df.head(10), use_container_width=True)
    
    # Configuration de l'analyse
    st.markdown('<h2 class="section-header">⚙️ Configuration de l\'analyse</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sélection de la colonne de groupement
        if column_types['categorical']:
            group_column = st.selectbox(
                "🏷️ Sélectionnez la colonne de groupement",
                column_types['categorical'],
                help="Colonne utilisée pour comparer les groupes"
            )
        else:
            st.error("❌ Aucune colonne catégorielle détectée pour le groupement")
            return
    
    with col2:
        # Sélection des variables à analyser
        if column_types['numerical']:
            selected_vars = st.multiselect(
                "🔢 Sélectionnez les variables à analyser",
                column_types['numerical'],
                default=column_types['numerical'],
                help="Variables numériques pour l'analyse"
            )
        else:
            st.error("❌ Aucune variable numérique détectée")
            return
    
    if not selected_vars:
        st.warning("⚠️ Veuillez sélectionner au moins une variable à analyser")
        return
    
    # Filtres optionnels
    with st.expander("🎛️ Filtres optionnels", expanded=False):
        filters = {}
        
        # Filtre sur les groupes
        available_groups = df[group_column].unique().tolist()
        selected_groups = st.multiselect(
            f"Filtrer par {group_column}",
            available_groups,
            default=available_groups
        )
        if selected_groups != available_groups:
            filters[group_column] = selected_groups
        
        # Filtres sur les variables numériques
        for var in selected_vars:
            col1, col2 = st.columns(2)
            min_val, max_val = float(df[var].min()), float(df[var].max())
            
            with col1:
                min_filter = st.number_input(f"Min {var}", value=min_val, key=f"min_{var}")
            with col2:
                max_filter = st.number_input(f"Max {var}", value=max_val, key=f"max_{var}")
            
            if min_filter != min_val or max_filter != max_val:
                filters[var] = [min_filter, max_filter]
        
        # Appliquer les filtres
        if filters:
            df_filtered = filter_dataframe(df, filters)
            st.info(f"📊 Données filtrées : {len(df_filtered)} lignes (sur {len(df)} originales)")
        else:
            df_filtered = df
    
    # Vérification qu'il reste des données après filtrage
    if df_filtered.empty:
        st.error("❌ Aucune donnée ne correspond aux filtres sélectionnés")
        return
    
    # Statistiques descriptives
    show_descriptive_statistics(df_filtered, group_column, selected_vars)
    
    # Tests statistiques
    show_statistical_tests(df_filtered, group_column, selected_vars)
    
    # Visualisations
    show_visualizations(df_filtered, group_column, selected_vars)


def show_descriptive_statistics(df, group_column, selected_vars):
    """Affiche les statistiques descriptives"""
    st.markdown('<h2 class="section-header">📈 Statistiques descriptives</h2>', unsafe_allow_html=True)
    
    stats_df = calculate_statistics(df, group_column, selected_vars)
    
    if not stats_df.empty:
        # Tableau interactif
        st.dataframe(
            stats_df.round(3),
            use_container_width=True,
            hide_index=True
        )
        
        # Option de téléchargement
        csv = stats_df.to_csv(index=False)
        st.download_button(
            label="📥 Télécharger les statistiques (CSV)",
            data=csv,
            file_name="statistiques_descriptives.csv",
            mime="text/csv"
        )


def show_statistical_tests(df, group_column, selected_vars):
    """Affiche les résultats des tests statistiques"""
    st.markdown('<h2 class="section-header">🔬 Tests statistiques</h2>', unsafe_allow_html=True)
    
    if len(df[group_column].unique()) == 2:
        test_results = perform_statistical_tests(df, group_column, selected_vars)
        
        if not test_results.empty:
            # Mise en forme des p-values avec couleurs
            def color_pvalue(val):
                if isinstance(val, (int, float)):
                    if val < 0.001:
                        return 'background-color: #d4edda; color: #155724'  # Vert foncé
                    elif val < 0.01:
                        return 'background-color: #fff3cd; color: #856404'  # Orange
                    elif val < 0.05:
                        return 'background-color: #f8d7da; color: #721c24'  # Rouge clair
                return ''
            
            styled_df = test_results.style.applymap(color_pvalue, subset=['P-value'])
            st.dataframe(styled_df, use_container_width=True, hide_index=True)
            
            # Légende
            st.markdown("""
            **Légende des couleurs :**
            - 🟢 p < 0.001 : Très significatif
            - 🟡 0.001 ≤ p < 0.01 : Significatif  
            - 🔴 0.01 ≤ p < 0.05 : Faiblement significatif
            - ⚪ p ≥ 0.05 : Non significatif
            """)
            
            # Option de téléchargement
            csv = test_results.to_csv(index=False)
            st.download_button(
                label="📥 Télécharger les tests statistiques (CSV)",
                data=csv,
                file_name="tests_statistiques.csv",
                mime="text/csv"
            )
        else:
            st.info("ℹ️ Aucun test statistique calculé")
    else:
        st.info("ℹ️ Les tests statistiques ne sont disponibles que pour 2 groupes")


def show_visualizations(df, group_column, selected_vars):
    """Affiche les visualisations"""
    st.markdown('<h2 class="section-header">📊 Visualisations interactives</h2>', unsafe_allow_html=True)
    
    # Options de visualisation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        plot_type = st.selectbox(
            "📈 Type de graphique",
            ["Violin Plot", "Box Plot", "Strip Plot"],
            help="Type de visualisation pour les données"
        )
    
    with col2:
        color_palette = st.selectbox(
            "🎨 Palette de couleurs",
            ["Set2", "viridis", "plasma", "Set1", "husl"],
            help="Palette de couleurs pour les groupes"
        )
    
    with col3:
        show_points = st.checkbox(
            "🔸 Afficher les points individuels",
            value=True,
            help="Superposer les points de données sur les graphiques"
        )
    
    # Génération des graphiques
    for i, var in enumerate(selected_vars):
        st.markdown(f"### 📊 {var}")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            fig = create_plot(df, group_column, var, plot_type, color_palette, show_points)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Statistiques rapides pour cette variable
            st.markdown("**Statistiques rapides :**")
            for group in df[group_column].unique():
                group_data = df[df[group_column] == group][var]
                st.metric(
                    f"{group}",
                    f"{group_data.mean():.2f}",
                    f"σ = {group_data.std():.2f}"
                )
            
            # Bouton de téléchargement pour ce graphique
            img_buffer = BytesIO()
            fig.write_image(img_buffer, format="png", width=800, height=600)
            
            st.download_button(
                label=f"📥 Télécharger",
                data=img_buffer.getvalue(),
                file_name=f"plot_{var}.png",
                mime="image/png",
                key=f"download_{i}"
            )
    
    # Graphique de corrélation si plusieurs variables
    if len(selected_vars) > 1:
        st.markdown("### 🔗 Matrice de corrélation")
        
        correlation_matrix = df[selected_vars].corr()
        
        fig_corr = px.imshow(
            correlation_matrix,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu",
            title="Matrice de corrélation entre les variables"
        )
        fig_corr.update_layout(height=500)
        st.plotly_chart(fig_corr, use_container_width=True)


def create_plot(df, group_column, variable, plot_type, color_palette, show_points):
    """Crée un graphique selon le type spécifié"""
    
    if plot_type == "Violin Plot":
        fig = px.violin(
            df, 
            x=group_column, 
            y=variable,
            color=group_column,
            box=True,
            points="all" if show_points else False,
            color_discrete_sequence=px.colors.qualitative.__dict__[color_palette],
            title=f"Distribution de {variable} par {group_column}"
        )
    
    elif plot_type == "Box Plot":
        fig = px.box(
            df,
            x=group_column,
            y=variable,
            color=group_column,
            points="all" if show_points else False,
            color_discrete_sequence=px.colors.qualitative.__dict__[color_palette],
            title=f"Distribution de {variable} par {group_column}"
        )
    
    else:  # Strip Plot
        fig = px.strip(
            df,
            x=group_column,
            y=variable,
            color=group_column,
            color_discrete_sequence=px.colors.qualitative.__dict__[color_palette],
            title=f"Distribution de {variable} par {group_column}"
        )
    
    # Mise en forme
    fig.update_layout(
        height=500,
        showlegend=True,
        xaxis_title=group_column.replace('_', ' ').title(),
        yaxis_title=variable.replace('_', ' ').title(),
        font=dict(size=12),
        plot_bgcolor='white'
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    return fig


if __name__ == "__main__":
    main()
