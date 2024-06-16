import streamlit as st

st.title("Streamlit Tutorial from YT 2")

st.write("The video I followed - [How to Control the Layout in Streamlit in 20 Minutes!](https://youtu.be/saOv9z6Fk88?si=FNaifoETR8fxcOTq)")

_ = '''
Sample Text:

Hello buddy, I said `hello, from ALASKA`. Thank you for that suprise.

Hi, `bud`.
'''

def clean_text(text):
    text = text.replace("`","").replace("-\n", "").replace("\n", " ").strip()
    return text

st.sidebar.header(".sidebar section")
text = st.sidebar.text_area("Paste Text Here")
button1 = st.sidebar.button("Clean Text")
if button1:
    col1,col2 = st.columns(2)

    col1_expander = col1.expander("Show Original")
    with col1_expander:
        col1_expander.header("Original Text")
        col1_expander.write(text)
    
    col2_expander = col2.expander("Show Cleaned")
    with col2_expander:
        col2_expander.header("Cleaned Text")
        col2_expander.write(clean_text(text))

st.sidebar.image("sunset.png", caption = "Sunset")