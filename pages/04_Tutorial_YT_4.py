import streamlit as st
import spacy

st.title("Streamlit Tutorial from YT 4")

st.write("The video I followed - [How to Cache Models and Data in Streamlit](https://youtu.be/nF-PQj0k5-o?si=1xuROXfrlXz1kXeE)")

@st.cache_resource

def load_model(model_name):
    nlp = spacy.load(model_name)
    return (nlp)
nlp = load_model("en_core_web_sm") #"python -m spacy download en_core_web_lg"

def extract_entities(ent_types, text):
    results = []
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, ent.label_))
    return (results)

form1 = st.sidebar.form(key = "Options") 
form1.header("Parameters")
ent_types = form1.multiselect("Select the entities you want to extract", ["PERSON", "ORG", "GPE"])
form1.form_submit_button("Click Me")

text = st.text_area("Sample Text", "James enjoys playing basketball in Florida for the Salvation Army")

hits = extract_entities(ent_types, text)
st.write(hits)