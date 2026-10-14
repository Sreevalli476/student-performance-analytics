
import numpy as np
import pandas as pd

# Subjects included in our dataset
SUBJECTS = ["Python", "NumPy", "Pandas", "Data_Analysis"]


def calculate_total(marks):
    return np.sum(marks)


def calculate_average(marks):
    return np.mean(marks)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"


def get_result(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"

    return "Pass"



def analyze_students(df):
    # Create a copy so the original dataset remains unchanged
    df = df.copy()

    # Process each student one by one
    for index, row in df.iterrows():

        # Get marks for the four subjects
        marks = row[SUBJECTS].to_numpy(dtype=float)

        # Calculate total and average
        total = calculate_total(marks)
        average = calculate_average(marks)

        # Store calculated results in the DataFrame
        df.loc[index, "Total_Marks"] = total
        df.loc[index, "Average_Marks"] = round(average, 2)
        df.loc[index, "Grade"] = assign_grade(average)
        df.loc[index, "Result"] = get_result(marks)

    return df

def display_summary(df):
    print("\n========== CLASS SUMMARY ==========")

    print("Total Students:", len(df))
    print("Class Average:", round(df["Average_Marks"].mean(), 2))

    # Find the highest-performing student
    top_student = df.loc[df["Average_Marks"].idxmax()]

    # Find the lowest-performing student
    low_student = df.loc[df["Average_Marks"].idxmin()]

    print(
        "Top Performer:",
        top_student["Name"],
        "-",
        top_student["Average_Marks"]
    )

    print(
        "Lowest Performer:",
        low_student["Name"],
        "-",
        low_student["Average_Marks"]
    )

    # Count pass and fail students
    print("Passed:", (df["Result"] == "Pass").sum())
    print("Failed:", (df["Result"] == "Fail").sum())

    # Calculate subject-wise averages
    print("\n========== SUBJECT AVERAGES ==========")

    for subject in SUBJECTS:
        print(subject, ":", round(df[subject].mean(), 2))

    # Display the top five students
    print("\n========== TOP 5 STUDENTS ==========")

    top_five = df.sort_values(
        by="Average_Marks",
        ascending=False
    ).head(5)

    print(
        top_five[
            ["Student_ID", "Name", "Average_Marks", "Grade", "Result"]
        ].to_string(index=False)
    )
