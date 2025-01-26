import streamlit as st
from SideBarLogo import add_logo

st.session_state["theme"] = "dark"

classifier_page = st.Page("Classifier.py", title="Bullying Detection", icon="✨")
model_explanation_page = st.Page("ModelExplanation.py", title="Model Breakdown", icon="🧩")
bullying_facts_page = st.Page("BullyingFacts.py", title="Bullying Education", icon="💡")
myth_vs_reality_page = st.Page("BullyingCase.py", title="Bullying Case Files", icon="🔮")

pg = st.navigation(
        {
            "Classifier": [classifier_page],
            "Model": [model_explanation_page,],
            "Bullying 101":[bullying_facts_page, myth_vs_reality_page]
        }
    )

st.set_page_config(page_title="BullyAware", page_icon="🎗️",layout="wide")

add_logo()
pg.run()