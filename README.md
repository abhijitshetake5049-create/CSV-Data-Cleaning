# CSV Data Cleaning using Pandas and NumPy

## Project Overview

This is a small Data Analytics project focused on cleaning an employee CSV dataset using Python, Pandas, and NumPy.

The original dataset contains missing values, invalid values, infinite values, negative values, and duplicate records. The project identifies and handles these issues to create a cleaner dataset.

## Technologies Used

* Python
* Pandas
* NumPy
* CSV

## Data Cleaning Performed

The following cleaning operations were performed:

* Checked the dataset for missing values.
* Filled missing numerical values.
* Identified and replaced invalid numerical values.
* Handled `inf` and `-inf` values.
* Handled negative values in numerical columns.
* Filled missing categorical values.
* Removed duplicate records.
* Exported the cleaned dataset as a new CSV file.

## Project Files

* `employee_dirty_data.csv` — Original dataset.
* `cleaning.py` — Python code used for cleaning the dataset.
* `cleaned_employee_data.csv` — Cleaned dataset.
* `README.md` — Project documentation.

## Workflow

```text
Employee CSV
     ↓
Inspect Data
     ↓
Find Missing & Invalid Values
     ↓
Clean Data using Pandas & NumPy
     ↓
Remove Duplicates
     ↓
Export Cleaned CSV
```

## Purpose

The purpose of this project is to practice basic **data cleaning and preprocessing** using Pandas and NumPy before performing further data analysis.

## Author

**Abhijit Shetake**

B.Tech Computer Science & Engineering






