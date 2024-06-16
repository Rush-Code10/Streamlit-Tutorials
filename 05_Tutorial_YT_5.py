import streamlit as st

st.title("Streamlit Tutorial from YT 5")

st.write("The video I followed - [How to Use the Session State in Streamlit - Easy Tutorial!](https://youtu.be/v90luNr14Xw?si=MjAt7rgCgNFq6yhm)")

st.header("Without Session State")
counter = 0
st.write(counter)

if st.button("UP"):
    counter = counter + 1
    st.write(counter)

st.header("With Session State")
if "coun_ter" not in st.session_state:
    st.session_state.coun_ter = 0
#st.write(st.session_state.coun_ter)
if st.button("up"):
    st.session_state.coun_ter += 1
    st.write(st.session_state.coun_ter) 
if st.button("reset"):
    st.session_state.coun_ter = 0