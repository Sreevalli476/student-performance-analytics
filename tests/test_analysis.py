
import unittest
import pandas as pd

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    get_result,
    analyze_students,
    SUBJECTS
)


class TestStudentAnalytics(unittest.TestCase):

    def test_total_marks(self):
        self.assertEqual(
            calculate_total([80, 90, 70, 60]), 300
        )

    def test_average_marks(self):
        self.assertEqual(
            calculate_average([80, 90, 70, 60]), 75
        )

    def test_grade_assignment(self):
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(55), "E")
        self.assertEqual(assign_grade(45), "F")

    def test_pass_result(self):
        self.assertEqual(
            get_result([80, 70, 60, 90]), "Pass"
        )

    def test_fail_result(self):
        self.assertEqual(
            get_result([80, 35, 60, 90]), "Fail"
        )

    def test_dataset_and_analysis(self):
        df = pd.read_csv("data/students.csv")
        result = analyze_students(df)

        self.assertEqual(len(result), 20)
        self.assertIn("Total_Marks", result.columns)
        self.assertIn("Average_Marks", result.columns)
        self.assertIn("Grade", result.columns)
        self.assertIn("Result", result.columns)

    def test_each_average_is_correct(self):
        df = pd.read_csv("data/students.csv")
        result = analyze_students(df)

        for _, row in result.iterrows():
            expected = row[SUBJECTS].mean()
            self.assertAlmostEqual(
                row["Average_Marks"], expected, places=2
            )


if __name__ == "__main__":
    unittest.main()
