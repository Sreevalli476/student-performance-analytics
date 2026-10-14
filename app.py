
import streamlit as st
import pandas as pd
from functions import analyze_students

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Analytics Pro",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f4f8ff, #eefbf4);
}
h1, h2, h3 {
    color: #17365d;
}
[data-testid="stMetric"] {
    background: white;
    border: 1px solid #dce6f1;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    data = pd.read_csv("data/students.csv")
    return analyze_students(data)

try:
    df = load_data()
except Exception as error:
    st.error("Could not load the student dataset.")
    st.code(str(error))
    st.stop()

SUBJECTS = ["Python", "NumPy", "Pandas", "Data_Analysis"]

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Student Analytics")
st.sidebar.caption("Academic Performance System")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "Student Explorer",
        "Subject Analysis",
        "Top Performers"
    ]
)

st.sidebar.divider()
st.sidebar.info("Dataset: 20 student records")
st.sidebar.caption("Built with Python, Pandas, NumPy & Streamlit")

# ---------------- HEADER ----------------
st.title("🎓📚 Student Performance Analytics")
st.caption("An interactive dashboard for academic performance analysis.")

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    total = len(df)
    average = round(df["Average_Marks"].mean(), 2)
    passed = int((df["Result"] == "Pass").sum())
    failed = int((df["Result"] == "Fail").sum())

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("👥 Total Students", total)
    c2.metric("📊 Class Average", average)
    c3.metric("✅ Passed", passed)
    c4.metric("❌ Failed", failed)

    st.subheader("📈 Subject-wise Average Marks")
    subject_avg = df[SUBJECTS].mean()
    st.bar_chart(subject_avg, height=320)

    left, right = st.columns(2)

    with left:
        st.subheader("🎯 Grade Distribution")
        grade_counts = (
            df["Grade"]
            .value_counts()
            .reindex(["A", "B", "C", "D", "E", "F"], fill_value=0)
        )
        st.bar_chart(grade_counts)

    with right:
        st.subheader("📋 Pass / Fail Summary")
        result_counts = (
            df["Result"]
            .value_counts()
            .reindex(["Pass", "Fail"], fill_value=0)
        )
        st.bar_chart(result_counts)

# ---------------- STUDENT EXPLORER ----------------
elif page == "Student Explorer":

    st.subheader("🔎 Find and Filter Students")

    departments = ["All"] + sorted(df["Department"].unique().tolist())
    department = st.selectbox("Department", departments)
    search = st.text_input("Search by student name or ID")

    filtered = df.copy()

    if department != "All":
        filtered = filtered[filtered["Department"] == department]

    if search:
        mask = (
            filtered["Name"].str.contains(search, case=False, na=False)
            | filtered["Student_ID"].str.contains(
                search, case=False, na=False
            )
        )
        filtered = filtered[mask]

    st.write("Matching students:", len(filtered))
    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.subheader("👤 Individual Student Profile")

    if not filtered.empty:
        selected_id = st.selectbox(
            "Select student",
            filtered["Student_ID"].tolist()
        )

        student = filtered[filtered["Student_ID"] == selected_id].iloc[0]

        st.markdown(
            "### " + str(student["Name"]) +
            " — " + str(student["Department"])
        )

        p1, p2, p3 = st.columns(3)
        p1.metric("Average Marks", round(student["Average_Marks"], 2))
        p2.metric("Grade", str(student["Grade"]))
        p3.metric("Result", str(student["Result"]))

        marks = student[SUBJECTS]
        st.bar_chart(marks)
    else:
        st.warning("No students match your search.")

    csv_data = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download Filtered Students",
        data=csv_data,
        file_name="filtered_students.csv",
        mime="text/csv"
    )

# ---------------- SUBJECT ANALYSIS ----------------
elif page == "Subject Analysis":

    st.subheader("📚 Explore Subject Performance")

    subject = st.selectbox("Choose subject", SUBJECTS)

    st.metric("Class Average", round(df[subject].mean(), 2))
    st.metric("Highest Mark", int(df[subject].max()))
    st.metric("Lowest Mark", int(df[subject].min()))

    st.subheader("Marks by Student")
    subject_data = df[["Name", subject]].set_index("Name")
    st.bar_chart(subject_data, height=400)

    st.subheader("Subject Statistics")
    st.dataframe(
        df[["Student_ID", "Name", "Department", subject]]
        .sort_values(subject, ascending=False),
        use_container_width=True,
        hide_index=True
    )

# ---------------- TOP PERFORMERS ----------------
elif page == "Top Performers":

    st.subheader("🏆 Student Leaderboard")

    number = st.slider("Number of students", 3, len(df), 5)

    ranking = df.sort_values(
        "Average_Marks", ascending=False
    ).head(number).copy()

    ranking.insert(0, "Rank", range(1, len(ranking) + 1))

    st.dataframe(
        ranking[
            ["Rank", "Student_ID", "Name", "Department",
             "Average_Marks", "Grade", "Result"]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.subheader("🏅 Performance Comparison")
    st.bar_chart(
        ranking.set_index("Name")[["Average_Marks"]],
        height=350
    )

# ---------------- DOWNLOAD FULL REPORT ----------------
st.divider()

full_csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Complete Student Analysis",
    data=full_csv,
    file_name="student_analysis.csv",
    mime="text/csv"
)

st.caption("Student Performance Analytics System | Python Mini Project")
