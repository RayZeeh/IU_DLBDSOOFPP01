# Import needed librarys
import streamlit as st
from storage import DataHandler
import pandas as pd

st.set_page_config(layout="wide")

@st.cache_data
def load_module():
    handler = DataHandler()
    return handler.load_module()


st.sidebar.image("./resources/IU_Internationale_Hochschule_logo.svg", use_container_width=True)
st.sidebar.title("Demo Menu")

st.title("Demo Dashboard", text_alignment="center")

#First ROW
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.subheader("Studiengang")
        st.markdown("Bachelor<br>Cyber Security (B.Sc)", unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.subheader("Semester")
        st.write("Winter 2025")

with col3:
    with st.container(border=True):
        st.subheader("ETCS")
        st.metric(label="Fortschitt", value=f"55 / 180", delta=f"125 ETCS verbleibemd")

with col4:
    with st.container(border=True):
        st.subheader("Notendurschnitt")
        st.metric(label="Ø-Note", value=f"2.0")

#Second Row

st.subheader("Module")
modules = load_module()

if modules:
    df = pd.DataFrame([m.__dict__ for m in modules])

    # Optional: nicer column names
    df = df.rename(columns={
        "code": "Code",
        "name": "Modulname",
        "ects": "ECTS",
        "bestanden": "Bestanden",
        "bemerkung": "Bemerkung",
        "semesterNummer": "Semester"
    })

    st.dataframe(
        df,
        hide_index=True,
    )
else:
    st.info("Keine Module gefunden.")
