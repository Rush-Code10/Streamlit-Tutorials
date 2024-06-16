import streamlit as st

st.title("Streamlit Tutorial from YT 6")

st.write("The video I followed - [How to Use Containers in Streamlit - Easy Tutorial](https://youtu.be/6R8EDJPuyv4?si=3rVX_zTRwGCE47F1)")

main_container = st.container()
if "coun_ter" not in st.session_state:
    st.session_state.coun_ter = 0
#st.write(st.session_state.coun_ter)
if st.button("up"):
    main_container.write(st.session_state.coun_ter)
    st.session_state.coun_ter += 1
if st.button("reset"):
    st.session_state.coun_ter = 0