# 🎓 Student Performance Analytics System

An interactive dashboard that analyzes student academic performance using Python, Pandas, NumPy, and Streamlit.

## 📌 Project Overview

The Student Performance Analytics System helps analyze student marks, calculate totals and averages, assign grades, determine pass/fail results, and identify top performers. The Streamlit dashboard provides an interactive interface for exploring student data.

## 🎯 Objectives

- Analyze student academic performance.
- Calculate total and average marks.
- Assign grades and determine pass/fail results.
- Compare subject-wise performance.
- Identify top and lowest performers.
- Display results through an interactive dashboard.
- Export analyzed data as CSV reports.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas** — Dataset handling and analysis
- **NumPy** — Numerical calculations
- **Streamlit** — Interactive web dashboard
- **Unittest** — Automated testing
- **CSV** — Dataset and report format

## ✨ Features

- Dashboard summary with student count, class average, pass count, and fail count
- Department filter and student search by name or ID
- Individual student performance profiles
- Subject-wise marks analysis
- Grade and pass/fail distribution
- Top-performer leaderboard
- Downloadable student analysis reports

## 📁 Project Structure

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

## 📊 Dataset

The dataset contains 20 sample student records with the following fields:

- Student ID
- Name
- Department
- Python marks
- NumPy marks
- Pandas marks
- Data Analysis marks
- Attendance

The records are fictional and intended for educational purposes.

## 🧮 Analysis Rules

- **Total Marks:** Sum of marks across four subjects.
- **Average Marks:** Total marks divided by four.
- **Grade A:** Average of 90 or above.
- **Grade B:** Average of 80–89.99.
- **Grade C:** Average of 70–79.99.
- **Grade D:** Average of 60–69.99.
- **Grade E:** Average of 50–59.99.
- **Grade F:** Average below 50.
- **Pass:** At least 40 marks in every subject.
- **Fail:** Below 40 in any subject.

## ⚙️ Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Sreevalli476/student-performance-analytics.git
cd student-performance-analytics
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Launch the interactive dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

### 4. Run the analysis from the terminal

```bash
python main.py
```

### 5. Run unit tests

```bash
python -m unittest discover -s tests -v
```

## 📄 Output Reports

- `outputs/student_analysis.csv` — Student records with calculated totals, averages, grades, and results.
- `outputs/subject_summary.csv` — Subject-wise average marks.

The dashboard also provides downloadable CSV files.

## 🧪 Testing

The project includes unit tests for total marks, average marks, grade assignment, pass/fail logic, dataset analysis, and average calculations.

## 📚 Learning Outcomes

- Working with CSV files and Pandas DataFrames
- Using NumPy for numerical calculations
- Applying Python functions, loops, and conditions
- Creating interactive dashboards with Streamlit
- Writing unit tests
- Managing and publishing a project using Git and GitHub

## 👩‍💻 Author

**Sreevalli**

GitHub: https://github.com/Sreevalli476

## 🔗 Repository

https://github.com/Sreevalli476/student-performance-analytics

## 🏁 Conclusion

This project demonstrates how Python data-analysis libraries can be used to analyze student performance and present meaningful academic insights through an interactive dashboard.
