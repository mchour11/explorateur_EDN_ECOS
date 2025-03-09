import streamlit as st
import pandas as pd

# Charger les données
file_path = "250310_EDN_SDD.csv"
df = pd.read_csv(file_path, sep=None, engine="python")

# Interface Streamlit
st.title("Explorateur EDN/ECOS — ECOS Alpha")

# Ajouter une colonne combinée pour affichage
df["SDD_display"] = df["SDD_num"].astype(str) + " - " + df["SDD"]
df["EDN_display"] = df["EDN_num"].astype(str) + " - " + df["EDN"]

# Trier les valeurs
sdd_sorted = df[["SDD_num", "SDD_display"]].drop_duplicates().sort_values("SDD_num")
edn_sorted = df[["EDN_num", "EDN_display"]].drop_duplicates().sort_values("EDN_num")

# Choix du mode d'exploration
mode = st.radio("Choisissez un mode :", ["Par SDD", "Par EDN"])

if mode == "Par SDD":
    sdd_choice = st.selectbox("Sélectionnez une Situation de Départ (SDD) :", sdd_sorted.set_index("SDD_num")["SDD_display"])
    result = df[df["SDD_display"] == sdd_choice][["EDN_num", "EDN"]].drop_duplicates()
    st.write(f"### Items EDN liés à la SDD {sdd_choice} :")
    st.dataframe(result.set_index("EDN_num"))
else:
    edn_choice = st.selectbox("Sélectionnez un item EDN :", edn_sorted.set_index("EDN_num")["EDN_display"])
    result = df[df["EDN_display"] == edn_choice][["SDD_num", "SDD"]].drop_duplicates()
    st.write(f"### Situations de Départ liées à l'item EDN {edn_choice} :")
    st.dataframe(result.set_index("SDD_num"))