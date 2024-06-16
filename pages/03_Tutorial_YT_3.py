import streamlit as st
import spacy

st.title("Streamlit Tutorial from YT 3")

st.write("The video I followed - [How to Use Forms in Streamlit EASY](https://youtu.be/FwvesOnxP60?si=xQlRH1o5BQXcnRFJ)")

nlp = spacy.load("en_core_web_sm") #"python -m spacy download en_core_web_lg"

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