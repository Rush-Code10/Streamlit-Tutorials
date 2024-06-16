import streamlit as st

grading_scale = {
    "A+": 4.00,
    "A": 3.75,
    "A-": 3.50,
    "B+": 3.25,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.25,
    "C-": 2.00,
    "D": 1.50,
    "F": 0.0
}

if 'courses' not in st.session_state:
    st.session_state.courses = []

def add_course():
    course_name = st.session_state.course_name
    course_grade = st.session_state.course_grade
    credit_hours = int(st.session_state.credit_hours)

    st.session_state.courses.append((course_name, course_grade, credit_hours))

st.title("GPA Calculator")

course_name = st.text_input("Course Name", key="course_name")
course_grade = st.selectbox("Grade", options=list(grading_scale.keys()), key="course_grade")
credit_hours = st.text_input("Credit Hours", key="credit_hours")

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if st.button("Add Course"):
        add_course()

if st.session_state.courses:
    st.subheader("Courses")
    course_data = {"Course": [], "Grade": [], "Credit Hours": []}
    for course in st.session_state.courses:
        course_data["Course"].append(course[0])
        course_data["Grade"].append(course[1])
        course_data["Credit Hours"].append(course[2])
    st.table(course_data)

    total_grade_points = sum(grading_scale[course[1]] * course[2] for course in st.session_state.courses)
    total_credit_hours = sum(course[2] for course in st.session_state.courses)
    gpa = total_grade_points / total_credit_hours
    st.subheader(f"GPA: {gpa:.2f}")
