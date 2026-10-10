# Student Performance Analytics System

A simple, beginner-friendly Python project for the **Python with AI** internship assignment. It analyzes 20 student records using Python, Pandas and NumPy. No machine learning or advanced programming is used.

## Features
- Reads student records from `students.csv` with Pandas
- Calculates each student's total and average marks
- Assigns grades using a simple grading rule
- Marks students Pass/Fail (at least 40 marks in every subject to pass)
- Displays class average, highest/lowest average, pass/fail counts and attendance average
- Analyzes Maths, Python and AI subject averages
- Shows the top 3 students
- Uses NumPy for median and standard deviation
- Saves calculated data to `student_results.csv`

## Requirements
- Python 3.9 or newer recommended
- Pandas
- NumPy

## Run in VS Code
1. Extract the ZIP file.
2. Open the `student_performance_analytics` folder in VS Code.
3. Open Terminal → New Terminal.
4. (Optional but recommended) Create a virtual environment:
   - macOS/Linux: `python3 -m venv .venv`
   - Windows: `py -m venv .venv`
5. Activate it:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
6. Install packages:
   `python -m pip install -r requirements.txt`
7. Run:
   - macOS/Linux: `python3 main.py`
   - Windows: `python main.py`

Keep `main.py` and `students.csv` in the same folder.

## Grade rule
| Average marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## Dataset
The sample dataset contains 20 fictional BCA students, three subject marks (Maths, Python and AI), and attendance percentages. Replace the sample rows with your own data if required, but keep the column names unchanged.

## Files
- `main.py` — main program
- `students.csv` — sample dataset
- `requirements.txt` — required libraries
- `README.md` — setup and usage
- `Project_Documentation.md` — report template/content for submission

## Learning note
Please read the code and understand the functions before submitting. Be prepared to explain how Pandas loads the CSV, how NumPy calculates median and standard deviation, and how the grade/pass-fail rules work.
