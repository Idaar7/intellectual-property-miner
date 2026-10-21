import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="IP Mining & Patent Brokerage Platform", layout="wide")

# Language Toggle Layer
lang = st.radio("🌐 Select Language / Choisir la langue", ["EN", "FR"], horizontal=True)

if lang == "EN":
    st.title("🧪 DeepTech Intellectual Property Mining Hub")
    st.write("Cross-referencing sleeping academic patents with tech enterprise roadmaps to extract high-value brokerage liquidities.")
    sub1 = "🔍 Live Patent Semantical Valuation Matrix"
    sub2 = "💼 Brokerage Execution Interface"
    lbl_patent = "Select target dormant patent ID:"
    lbl_buyer = "Target Acquirer Pipeline:"
    val_label = "Estimated Patent Valuation (USD)"
    comm_label = "Your Premium Brokerage Commission (20%)"
    btn_broker = "Initiate Acquisition Protocol"
    success_msg = "Brokerage protocol initialized. Multi-party legal frameworks generated."
else:
    st.title("🧪 Hub d'Arbitrage et de Valorisation de Brevets Dormants")
    st.write("Croisement algorithmique des brevets académiques dormants avec les besoins industriels des GAFAM pour générer des commissions de courtage.")
    sub1 = "🔍 Matrice de Valorisation Sémantique des Brevets"
    sub2 = "💼 Interface de Courtage de Haute Technologie"
    lbl_patent = "Sélectionnez le brevet dormant cible :"
    lbl_buyer = "Acquéreur stratégique ciblé :"
    val_label = "Valorisation Estimée du Brevet (USD)"
    comm_label = "Votre Commission de Courtage Premium (20%)"
    btn_broker = "Initialiser le Protocole de Vente"
    success_msg = "Protocole d'acquisition lancé. Documents contractuels inter-institutionnels générés."

@st.cache_data(ttl=5)
def get_patent_data():
    patents = [
        "US-99201-B2 (Quantum Dot Encryption)", 
        "EP-40192-A1 (Solid-State Battery Anode)", 
        "US-88210-B1 (Neural Net Quantization Engine)"
    ]
    data = []
    valuations = [12000000, 8500000, 15000000]
    buyers = ["NVIDIA Inc", "Tesla Motors", "Microsoft Corporation"]
    
    for i, p in enumerate(patents):
        val = valuations[i]
        buyer = buyers[i]
        data.append({
            "Patent ID / Technology" if lang=="EN" else "ID Brevet / Technologie": p,
            "Target Strategic Acquirer" if lang=="EN" else "Acquéreur Stratégique Cible": buyer,
            "Scoring Fit (%)": np.random.randint(91, 99),
            "Estimated Asset Value ($)" if lang=="EN" else "Valeur Estimée ($)": int(val)
        })
    return pd.DataFrame(data)

df_patents = get_patent_data()
st.subheader(sub1)
st.dataframe(df_patents, use_container_width=True)

st.write("---")
st.subheader(sub2)
col1, col2 = st.columns(2)
with col1:
    selected_p = st.selectbox(lbl_patent, df_patents.iloc[:, 0].tolist())
    current_row = df_patents[df_patents.iloc[:, 0] == selected_p]
    target_b = st.text_input(lbl_buyer, value=current_row.iloc[0, 1])
with col2:
    est_value = current_row.iloc[0, 3]
    st.metric(label=val_label, value=f"{est_value:,.2f} $")
    st.metric(label=comm_label, value=f"{(est_value * 0.20):,.2f} $", delta="Net Profit (20%)")
    
    if st.button(btn_broker):
        st.success(f"{success_msg} Target Pipeline: {target_b}")

