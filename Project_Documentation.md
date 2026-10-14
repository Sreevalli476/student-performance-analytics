# STUDENT PERFORMANCE ANALYTICS SYSTEM

## Project Documentation

**Project Type:** Python Mini Project  
**Course:** EWB Courses – Python with AI  
**Student Name:** Sreevalli  
**GitHub Repository:** https://github.com/Sreevalli476/student-performance-analytics

---

## 1. Introduction

The Student Performance Analytics System is a Python-based mini-project developed to analyze student academic performance. It uses Pandas and NumPy to process student marks, calculate totals and averages, assign grades, determine pass/fail results, and identify top performers.

An interactive web dashboard has been developed using Streamlit. It allows users to explore student records, filter students by department, search for individual students, view subject-wise performance, and download analysis reports.

## 2. Problem Statement

Manually calculating student totals, averages, grades, and results for multiple students can be time-consuming and may lead to errors. Comparing subject performance and identifying students who need academic support can also be difficult when information is maintained only in raw datasets.

This project addresses these problems by automating student performance calculations and presenting the results in an interactive dashboard.

## 3. Objectives

1. Read and process student data from a CSV file.
2. Store and manipulate records using Pandas DataFrames.
3. Use NumPy for numerical calculations.
4. Calculate total and average marks for each student.
5. Assign grades based on average marks.
6. Determine pass/fail status using subject marks.
7. Identify the highest and lowest performers.
8. Calculate subject-wise average marks.
9. Display academic insights through a Streamlit dashboard.
10. Export analyzed results as CSV reports.
11. Test important functions using Python's unittest framework.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming and application logic |
| Pandas | Reading CSV data and processing DataFrames |
| NumPy | Calculating totals and averages |
| Streamlit | Building the interactive dashboard |
| CSV | Storing student data and generated reports |
| unittest | Testing calculation and analysis functions |
| Git and GitHub | Version control and project hosting |

## 5. Dataset Description

The input dataset is stored in `data/students.csv`. It contains 20 fictional student records.

### Dataset fields

- Student_ID
- Name
- Department
- Python
- NumPy
- Pandas
- Data_Analysis
- Attendance

Each subject is represented by marks out of 100. Attendance is recorded separately as a percentage-like value in the sample dataset.

The dataset supports student-level analysis, department filtering, subject comparison, and performance ranking.

## 6. System Design and Implementation

### 6.1 Dataset loading

Pandas reads the CSV file into a DataFrame. This provides a structured way to access student names, departments, marks, and attendance.

### 6.2 Total marks calculation

NumPy calculates the sum of marks obtained in the four subjects.

**Formula:**

Total Marks = Python + NumPy + Pandas + Data Analysis

### 6.3 Average marks calculation

The average is calculated by dividing the total marks by four.

**Formula:**

Average Marks = Total Marks / 4

### 6.4 Grade assignment

The `assign_grade()` function assigns grades based on average marks.

| Average Marks | Grade |
|---|---|
| 90 and above | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| 50 to below 60 | E |
| Below 50 | F |

### 6.5 Pass/fail determination

The `get_result()` function checks every subject mark. A student passes only when all four subject marks are at least 40. If any subject mark is below 40, the student is marked as failed.

### 6.6 Student analysis

The `analyze_students()` function processes each student record and adds the following calculated fields:

- Total_Marks
- Average_Marks
- Grade
- Result

### 6.7 Class and subject analysis

The `display_summary()` function reports the number of students, class average, highest and lowest performers, pass/fail counts, subject-wise averages, and top five students.

### 6.8 Interactive dashboard

The `app.py` file implements the user interface with Streamlit. It includes:

- Dashboard summary metrics
- Department filtering
- Search by student name or ID
- Individual student performance profiles
- Subject-wise marks analysis
- Grade distribution
- Pass/fail distribution
- Top-performer leaderboard
- CSV download options

### 6.9 Report generation

The application generates CSV reports in the `outputs/` directory:

1. `student_analysis.csv` — Includes the analyzed student records and calculated fields.
2. `subject_summary.csv` — Contains subject-wise average marks.

## 7. Project Folder Structure

```text
student-performance-analytics/
├── data/
│   └── students.csv
├── outputs/
│   ├── student_analysis.csv
│   └── subject_summary.csv
├── tests/
│   └── test_analysis.py
├── app.py
├── functions.py
├── main.py
├── requirements.txt
├── README.md
├── Project_Documentation.md
└── .gitignore
```

## 8. Execution Instructions

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run the terminal analysis

```bash
python main.py
```

### Run the interactive dashboard

```bash
python -m streamlit run app.py
```

The dashboard opens in a web browser using the local address displayed in the terminal.

### Run the unit tests

```bash
python -m unittest discover -s tests -v
```

## 9. Testing

The project includes seven unit tests covering:

1. Total marks calculation
2. Average marks calculation
3. Grade assignment
4. Pass result
5. Fail result
6. Dataset loading and analysis
7. Correct average calculation for every student

**Testing status:** All seven tests passed in the reported test run.

## 10. Output and Screenshots

The project produces an interactive dashboard with summary metrics, student records, filters, charts, and a top-performer leaderboard. It also produces downloadable CSV reports.

Insert actual screenshots of the running application below:

### Screenshot 1: Dashboard overview

*Insert the screenshot showing the dashboard heading, summary metrics, and subject-wise chart.*

### Screenshot 2: Student Explorer

*Insert the screenshot showing student search, department filter, and individual student details.*

### Screenshot 3: Top Performers

*Insert the screenshot showing the student leaderboard.*

### Screenshot 4: Unit test results

*Insert the terminal screenshot showing all seven tests passing.*

## 11. Challenges Faced

### Dataset filename mismatch

Initially, the Python application could not locate the dataset because the filename used in the code did not match the actual CSV filename. The issue was resolved by ensuring the dataset was named `students.csv` and the code referenced `data/students.csv`.

### Integrating the dashboard

The existing analysis functions were reused in the Streamlit application so that the dashboard could display calculated student results without duplicating the analysis logic.

### Testing and version control

Unit tests were used to verify important calculations. Git and GitHub were then used to commit and publish the project files.

## 12. Learning Outcomes

Through this project, I learned how to:

- Read and process CSV files using Pandas
- Perform numerical calculations using NumPy
- Write reusable Python functions
- Apply loops and conditional statements
- Calculate grades and academic results
- Build an interactive dashboard using Streamlit
- Display tables, charts, and summary metrics
- Generate downloadable CSV reports
- Write unit tests
- Use Git and GitHub for version control and project hosting

## 13. Limitations and Future Enhancements

### Current limitations

- The project uses a sample dataset rather than a live student database.
- The dashboard does not include user authentication.
- The analysis is limited to the available student and subject fields.

### Future enhancements

- Upload new datasets directly through the dashboard.
- Add more subjects and academic semesters.
- Introduce attendance-based alerts.
- Add database integration.
- Generate PDF reports.
- Deploy the dashboard online.

## 14. Final Outcome

The Student Performance Analytics System successfully combines Python programming, data analysis, automated calculations, unit testing, and interactive visualization. It provides a structured way to explore student performance and generate reports.

The project demonstrates the practical use of Python libraries to transform raw student data into useful academic information.

## 15. GitHub Repository

**Repository URL:**  
https://github.com/Sreevalli476/student-performance-analytics

## 16. Conclusion

This mini-project demonstrates how Python, Pandas, NumPy, and Streamlit can be used together to create an interactive student performance analysis application. It reduces manual calculation, supports student-level and subject-level analysis, and presents results in a user-friendly format.
