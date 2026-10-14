
import pandas as pd
from functions import analyze_students, display_summary

# Load the student dataset
df = pd.read_csv("data/students.csv")

# Display the original dataset information
print("\n========== STUDENT DATASET ==========")
print(df.head())
print("\nTotal students:", len(df))

# Analyze all students
analyzed_df = analyze_students(df)

# Display the complete analysis summary
display_summary(analyzed_df)
# Save detailed student analysis
analyzed_df.to_csv(
    "outputs/student_analysis.csv",
    index=False
)

# Save subject-wise averages
analyzed_df[
    ["Python", "NumPy", "Pandas", "Data_Analysis"]
].mean().to_csv(
    "outputs/subject_summary.csv",
    header=["Average_Marks"]
)

print("\nReports saved successfully in the outputs folder.")