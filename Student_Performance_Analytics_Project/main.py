import pandas as pd
import numpy as np

DATA_FILE = "students.csv"
SUBJECTS = ["Maths", "Python", "AI"]


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def load_data():
    try:
        data = pd.read_csv(DATA_FILE)
        return data
    except FileNotFoundError:
        print(f"Error: Could not find {DATA_FILE}. Keep it beside main.py.")
        return None


def analyse_students(data):
    data = data.copy()
    data["Total"] = data[SUBJECTS].sum(axis=1)
    data["Average"] = data[SUBJECTS].mean(axis=1).round(2)

    grades = []
    results = []
    for _, student in data.iterrows():
        grades.append(assign_grade(student["Average"]))
        if all(student[subject] >= 40 for subject in SUBJECTS):
            results.append("Pass")
        else:
            results.append("Fail")

    data["Grade"] = grades
    data["Result"] = results
    return data


def show_summary(data):
    print("\n" + "=" * 58)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 58)
    print(f"Number of students : {len(data)}")
    print(f"Overall class average: {data['Average'].mean():.2f}")
    print(f"Highest student average: {data['Average'].max():.2f}")
    print(f"Lowest student average : {data['Average'].min():.2f}")
    print(f"Passed students     : {(data['Result'] == 'Pass').sum()}")
    print(f"Failed students     : {(data['Result'] == 'Fail').sum()}")
    print(f"Average attendance  : {data['Attendance'].mean():.2f}%")

    # NumPy numerical calculations
    averages = data["Average"].to_numpy()
    print(f"Median student average: {np.median(averages):.2f}")
    print(f"Standard deviation   : {np.std(averages):.2f}")


def show_student_results(data):
    print("\n--- Individual Student Results ---")
    columns = ["Student_ID", "Name", "Total", "Average", "Grade", "Result", "Attendance"]
    print(data[columns].to_string(index=False))


def show_subject_analysis(data):
    print("\n--- Subject-wise Performance ---")
    for subject in SUBJECTS:
        print(f"{subject:8} Average: {data[subject].mean():.2f} | "
              f"Highest: {data[subject].max()} | Lowest: {data[subject].min()}")
    best_subject = data[SUBJECTS].mean().idxmax()
    print(f"Best-performing subject: {best_subject}")


def show_top_students(data):
    print("\n--- Top 3 Students ---")
    top_students = data.sort_values(by="Average", ascending=False).head(3)
    print(top_students[["Name", "Department", "Average", "Grade"]].to_string(index=False))


def save_results(data):
    output_columns = ["Student_ID", "Name", "Department", "Maths", "Python", "AI",
                      "Attendance", "Total", "Average", "Grade", "Result"]
    data[output_columns].to_csv("student_results.csv", index=False)
    print("\nSaved full analysis to student_results.csv")


def main():
    data = load_data()
    if data is None:
        return

    required_columns = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing = [column for column in required_columns if column not in data.columns]
    if missing:
        print("Error: CSV is missing columns:", ", ".join(missing))
        return

    data = analyse_students(data)
    show_summary(data)
    show_student_results(data)
    show_subject_analysis(data)
    show_top_students(data)
    save_results(data)
    print("\nProject completed successfully!")


if __name__ == "__main__":
    main()
