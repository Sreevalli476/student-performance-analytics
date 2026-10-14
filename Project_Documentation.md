# STUDENT PERFORMANCE ANALYTICS SYSTEM

## Project Documentation

**Course:** EWB Courses – Python with AI  
**Project Type:** Python Mini Project  
**Student Name:** Sreevalli  
**GitHub Repository:** https://github.com/Sreevalli476/student-performance-analytics

---

## 1. Introduction

The Student Performance Analytics System is a Python-based application designed to analyze student academic performance. It processes student records stored in a CSV file and calculates total marks, average marks, grades, and pass/fail results.

The project uses Pandas for data processing and NumPy for numerical calculations. A Streamlit dashboard provides an interactive interface for searching student records, filtering departments, comparing subject performance, viewing top performers, and downloading reports.

## 2. Problem Statement

Analyzing student performance manually can be time-consuming when a dataset contains many student records. Calculating totals and averages, assigning grades, determining results, and comparing subject marks may also lead to mistakes.

This project automates these calculations and presents the results through an interactive dashboard, making student performance easier to explore and understand.

## 3. Objectives

1. Read student records from a CSV dataset.
2. Process student information using Pandas DataFrames.
3. Perform numerical calculations using NumPy.
4. Calculate total and average marks.
5. Assign grades according to defined rules.
6. Determine student pass/fail results.
7. Identify the highest and lowest performers.
8. Calculate subject-wise average marks.
9. Develop an interactive dashboard using Streamlit.
10. Generate downloadable CSV reports.
11. Test important calculations using Python's unittest framework.
12. Publish the source code and documentation on GitHub.

## 4. Technologies Used

| Technology | Application |
|---|---|
| Python | Application logic and calculations |
| Pandas | Dataset loading and data analysis |
| NumPy | Numerical calculations |
| Streamlit | Interactive dashboard interface |
| CSV | Dataset storage and report generation |
| unittest | Automated unit testing |
| Git | Source-code version control |
| GitHub | Repository hosting and project sharing |

## 5. Dataset Description

The input file is `data/students.csv`. It contains 20 fictional student records.

### Dataset columns

| Column | Description |
|---|---|
| Student_ID | Unique student ID |
| Name | Student name |
| Department | Academic department |
| Python | Python subject marks |
| NumPy | NumPy subject marks |
| Pandas | Pandas subject marks |
| Data_Analysis | Data Analysis subject marks |
| Attendance | Attendance value recorded for each student |

The four subject marks are out of 100. Attendance is included as a separate dataset field.

## 6. System Design and Implementation

### 6.1 Dataset loading

Pandas reads the CSV file and stores its contents in a DataFrame. The DataFrame provides structured access to student IDs, names, departments, marks, and attendance.

### 6.2 Total marks calculation

The `calculate_total()` function uses NumPy to calculate the sum of the four subject marks.

**Formula:**

Total Marks = Python + NumPy + Pandas + Data Analysis

### 6.3 Average marks calculation

The `calculate_average()` function uses NumPy to calculate the average marks.

**Formula:**

Average Marks = Total Marks / 4

### 6.4 Grade assignment

The `assign_grade()` function assigns grades according to the student's average marks.

| Average Marks | Grade |
|---|---|
| 90 and above | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| 50 to below 60 | E |
| Below 50 | F |

### 6.5 Pass/fail determination

The `get_result()` function checks all four subject marks. A student passes if every subject mark is at least 40. If any subject mark is below 40, the result is Fail.

### 6.6 Student analysis

The `analyze_students()` function processes the student records and adds four calculated fields:

- `Total_Marks`
- `Average_Marks`
- `Grade`
- `Result`

This allows the same analysis results to be displayed in the terminal and interactive dashboard.

### 6.7 Class summary and subject analysis

The `display_summary()` function reports the total number of students, class average, highest and lowest performers, pass/fail counts, subject-wise averages, and top five performers.

### 6.8 Interactive dashboard

The `app.py` file uses Streamlit to provide the following pages and features:

- **Dashboard:** Summary metrics, subject averages, grade distribution, and pass/fail statistics.
- **Student Explorer:** Search by student name or ID, department filtering, and individual student profiles.
- **Subject Analysis:** Subject selection, average marks, highest marks, lowest marks, and student comparisons.
- **Top Performers:** A leaderboard ranked by average marks.
- **CSV Downloads:** Download the complete analyzed dataset or filtered records.

### 6.9 Report generation

The project generates two CSV reports:

1. `outputs/student_analysis.csv` — Contains student records with calculated totals, averages, grades, and results.
2. `outputs/subject_summary.csv` — Contains subject-wise average marks.

The Streamlit interface also provides downloadable CSV files.

## 7. Project Folder Structure

```text
student-performance-analytics/
├── data/
│   └── students.csv
├── outputs/
│   ├── student_analysis.csv
│   └── subject_summary.csv
├── screenshots/
│   ├── dashboard.png
│   ├── student_explorer.png
│   ├── top_performers.png
│   └── test_results.png
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

## 8. Application Screenshots

### 8.1 Dashboard Overview

![Student Performance Analytics Dashboard](screenshots/dashboard.png)

**Description:** The dashboard presents summary metrics and visualizations for student academic performance.

### 8.2 Student Explorer

![Student Explorer](screenshots/student_explorer.png)

**Description:** The Student Explorer provides department filtering, student search, and individual student performance details.

### 8.3 Top Performers

![Top Performers](screenshots/top_performers.png)

**Description:** The leaderboard displays students ranked by average marks.

### 8.4 Unit Test Results

![Unit Test Results](screenshots/test_results.png)

**Description:** The screenshot records the output of the automated unit test run.

*Note: Replace or remove any screenshot reference if the corresponding image has not been added to the `screenshots/` folder.*

## 9. Execution Instructions

### 9.1 Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 9.2 Run the terminal analysis

```bash
python main.py
```

### 9.3 Launch the interactive dashboard

```bash
python -m streamlit run app.py
```

The terminal displays a local URL, usually `http://localhost:8501`. Open that URL in a browser to use the dashboard.

### 9.4 Run the unit tests

```bash
python -m unittest discover -s tests -v
```

## 10. Testing and Validation

The project contains seven unit tests.

| Test | Purpose |
|---|---|
| Total marks | Verifies the sum of subject marks |
| Average marks | Verifies the average calculation |
| Grade assignment | Checks grade boundaries |
| Pass result | Checks the passing condition |
| Fail result | Checks the failing condition |
| Dataset and analysis | Verifies the dataset size and calculated columns |
| Average correctness | Checks averages for individual student records |

**Reported result:** All seven tests passed during the project's test run.

The test output screenshot is included in Section 8.4 when the corresponding image is available.

## 11. Challenges Faced

### 11.1 Dataset filename mismatch

Initially, the dataset could not be loaded because the filename referenced by the program did not match the actual CSV filename. This was resolved by naming the file `students.csv` and using the path `data/students.csv`.

### 11.2 Dashboard integration

The existing analysis functions were reused in the Streamlit interface. This avoided duplicating the calculation logic and allowed the dashboard to display analyzed student results.

### 11.3 Automated testing

Unit tests were created to validate calculations, grade assignment, pass/fail logic, and dataset analysis.

### 11.4 Git and GitHub

The project was committed and pushed to GitHub. The local and remote changes were merged before the final push was completed.

## 12. Learning Outcomes

Through this project, I learned how to:

- Read CSV datasets using Pandas.
- Perform numerical calculations using NumPy.
- Work with DataFrames and tabular data.
- Implement Python functions, loops, and conditions.
- Calculate totals, averages, grades, and results.
- Build interactive interfaces with Streamlit.
- Display charts, tables, and summary metrics.
- Generate downloadable CSV reports.
- Write and execute unit tests.
- Use Git and GitHub for version control and project hosting.

## 13. Limitations and Future Enhancements

### Current limitations

- The system uses a sample CSV dataset rather than a live student database.
- The dashboard does not currently provide user authentication.
- Analysis is limited to the available student fields and four subjects.

### Future enhancements

- Add a CSV upload feature.
- Support additional subjects and semesters.
- Add attendance-based analysis and alerts.
- Integrate a database for persistent records.
- Generate downloadable PDF reports.
- Deploy the Streamlit application online.

## 14. Final Outcome

The Student Performance Analytics System combines Python programming, data processing, numerical calculations, interactive visualization, automated testing, and report generation.

It provides an organized way to analyze student performance, compare subject marks, identify top performers, and explore results through a web-based dashboard.

## 15. GitHub Repository

**Repository URL:**  
https://github.com/Sreevalli476/student-performance-analytics

The repository contains the source code, dataset, tests, dependency file, README, project documentation, and screenshots that have been added.

## 16. Conclusion

This project demonstrates the practical use of Python, Pandas, NumPy, and Streamlit to create an interactive academic performance analysis application. It reduces manual calculations and presents student results in a structured and user-friendly format.

The project also provides practical experience in data analysis, visualization, testing, documentation, and version control.
