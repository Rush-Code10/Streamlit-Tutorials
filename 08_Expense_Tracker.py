import streamlit as st
import pandas as pd

# Initialize session state variables
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])

# Function to add a new expense
def add_expense(date, category, description, amount):
    new_expense = pd.DataFrame({
        'Date': [date],
        'Category': [category],
        'Description': [description],
        'Amount': [amount]
    })
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

# Streamlit app title
st.title("Expense Tracker")

# Input fields for new expenses
with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    submit = st.form_submit_button("Add Expense")

    if submit:
        add_expense(date, category, description, amount)
        st.success("Expense added successfully!")

# Display expenses
st.subheader("Expenses")
st.dataframe(st.session_state.expenses)

# Summary statistics
if not st.session_state.expenses.empty:
    st.subheader("Summary Statistics")
    total_expense = st.session_state.expenses['Amount'].sum()
    st.write(f"Total Expense: ₹{total_expense:.2f}")

    expenses_by_category = st.session_state.expenses.groupby('Category')['Amount'].sum()
    st.bar_chart(expenses_by_category)
