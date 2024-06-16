import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Streamlit Basic from Documentation")

st.write("Documentation Link - [Basic Concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)")

# Basic write & button
st.write("Hello World !!!")
button1 = st.button("Hiiii")

# if true then will print this
if button1:
    st.write('Hello bro its a great day to be alive 😊')

# this will directly print a dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df
_ = ''' 
this will directly print a dataframe using .write
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
'''

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

_ = '''
Here's a breakdown of what each part does:

dataframe = np.random.randn(10, 20):

This line creates a NumPy array named dataframe.
np.random.randn(10, 20) generates a random sample from a standard normal distribution.
The shape of the array is specified as (10, 20), meaning it will have 10 rows (observations) and 20 columns (features).
st.dataframe(dataframe):

This line uses the st.dataframe function from the Streamlit library.
It takes the dataframe (the NumPy array you just created) as input.
The function displays the data in an interactive table format within your Streamlit app.
'''

# this will show a slider and it also prints the cube
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'cubed is', x * x * x)

# textual input
st.text_input("Your name", key="name")
st.session_state.name

# use checkboxes to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# use a selectbox for options
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column']+df['second column'])
'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)