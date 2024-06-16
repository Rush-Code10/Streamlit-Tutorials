import streamlit as st

st.title("Streamlit Tutorial from YT 1")

st.write("The video I followed - [How to use Streamlit in 30 Minutes!](https://www.youtube.com/watch?v=43RJ3JByygE&list=PL2VXyKi-KpYtZzm1K8UKnnBzsOCtekhKq&index=1)")

st.header(".write section")
st.write("Hello World !!!")

st.header(".button section")
button1 = st.button("Click Me")

if button1:
    st.write('Hello bro its a great day to be alive 😊')

st.header(".checkbox section")
like = st.checkbox("Was it a good day ?")
if st.button("Done ??"):
    if like:
        st.write("Great !")
    else:
        st.write("No probs, tommorrow will be better 😁")

st.header(".radiobutton section")
animal = st.radio("What's your favourite animal ?", ("Lion", "Elephant", "Sharks"))
if st.button("Submit Animal"):
    st.write(animal)

st.header(".selectbox section")
animal2 = st.selectbox("What's your favourite animal ?", ("Lion", "Elephant", "Sharks"))
if st.button("Submit"):
    st.write(animal2)

st.header(".multiselect section")
options = st.multiselect("What animals do you like ?", ["Lion", "Elephant", "Shark"])
if st.button("Print Animals"):
    st.write(options)

st.header(".slider section")
age = st.slider("What's your age ?", 1,120, 18)
if st.button("Slider Button"):
    st.write(age)

st.header(".text_input section")
user_text1 = st.text_input("What's you favourite movie ?", "Star Trek")
if st.button("Enter"):
    st.write(user_text1)

st.header(".number_input section")
user_text2 = st.number_input("How many cars do you own ?")
if st.button("Input"):
    st.write(user_text2)

def run_analysis(txt):
    st.write(f"DONE 👍🏻, {txt}")

st.header(".text_area section")
txt = st.text_area('Text: ', '''The horse is in the stable around the shed, livig his day to day life accordingly, thank you for joining in with rushabh's tutorials...''')
st.write("Analysis: ", run_analysis(txt))