# Project Documentation: Student Performance Analytics System

**Student Name:** ____________________  
**Course/Internship:** Python with AI  
**Project Title:** Student Performance Analytics System

## 1. Objective
The objective of this project is to analyze student marks and attendance using Python, Pandas and NumPy. It summarizes student performance and helps identify top performers, subject averages, and pass/fail counts.

## 2. Technologies Used
- Python
- Pandas
- NumPy
- CSV file for storing the sample data
- Visual Studio Code for development

## 3. Dataset Description
The file `students.csv` contains 20 fictional student records. Its columns are Student_ID, Name, Department, Maths, Python, AI and Attendance. Subject marks are out of 100 and attendance is a percentage.

## 4. Implementation
1. `pandas.read_csv()` loads the CSV file into a DataFrame.
2. The program checks that the expected columns exist.
3. Pandas calculates each student's total and average marks.
4. A function assigns grades according to the average-mark rules.
5. A loop checks each student's marks. A student passes if they score at least 40 in every subject.
6. Pandas calculates class and subject statistics.
7. NumPy calculates the median and standard deviation of student averages.
8. The program sorts averages to display the top three students.
9. The processed results are saved to `student_results.csv`.

## 5. Key Features
- Student-wise total and average
- Grade and pass/fail status
- Highest, lowest and overall average
- Pass/fail count and attendance average
- Subject-wise averages and highest/lowest marks
- Top three students
- Export of calculated results to a new CSV

## 6. Grading Rules
- 90 and above: A+
- 80 to below 90: A
- 70 to below 80: B
- 60 to below 70: C
- 50 to below 60: D
- Below 50: F

A student passes only if they score at least 40 in each subject.

## 7. Output / Screenshots
After running `main.py`, take a screenshot of the terminal showing the summary, student results, subject analysis and top three students. Add the screenshot here or in the repository.

## 8. Final Outcome
The program reads a CSV dataset, processes 20 student records and displays clear performance statistics. It also creates `student_results.csv` with calculated totals, averages, grades and results.

## 9. Challenges & Learning
Example points to personalize after testing:
- Learned to read CSV files into Pandas DataFrames.
- Practiced functions, loops, conditions and DataFrame columns.
- Used NumPy for median and standard deviation.
- Learned to export processed data back to CSV.

Replace these examples with the actual challenges you faced and what you learned.

## 10. GitHub Repository
Repository URL: ____________________

## How to run
Install dependencies using `python -m pip install -r requirements.txt`, then run `python main.py`.
