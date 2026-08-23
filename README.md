# CSV Data Cleaning using Pandas & NumPy

## 📌 Project Overview

This project focuses on cleaning and preprocessing an employee CSV dataset using **Python, Pandas, and NumPy**.

The dataset initially contained missing values, invalid values, infinite values, negative values, duplicate records, and inconsistent data. The cleaning process transforms the raw dataset into a cleaner and more reliable dataset suitable for further **Data Analysis and visualization**.

## 🎯 Objectives

* Identify missing and invalid data
* Handle missing values appropriately
* Detect and replace invalid and infinite values
* Remove duplicate records
* Handle negative and inconsistent values
* Prepare a clean dataset for further analysis

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **CSV**

## 🧹 Data Cleaning Operations

The following operations were performed on the employee dataset:

### 1. Missing Value Handling

Missing values were identified using Pandas and handled using appropriate replacement techniques such as median-based filling for numerical columns.

### 2. Invalid Values

Invalid values such as negative values and infinite values (`inf` and `-inf`) were identified and replaced with appropriate values.

### 3. Duplicate Removal

Duplicate employee records were identified and removed to improve data consistency.

### 4. Missing Categorical Values

Missing categorical values such as city and performance rating were handled using suitable replacement values.

### 5. Data Validation

The dataset was checked after cleaning to ensure that the resulting data was more consistent and suitable for further analysis.

## 📂 Project Files

| File                        | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| `employee_dirty_data.csv`   | Original dataset containing missing and inconsistent data |
| `cleaning.py`               | Python script used for data cleaning                      |
| `cleaned_employee_data.csv` | Dataset after the cleaning process                        |
| `README.md`                 | Project documentation                                     |

## 🔄 Project Workflow

```text
Raw Employee CSV
       ↓
Data Inspection
       ↓
Identify Missing & Invalid Values
       ↓
Handle Missing Values
       ↓
Handle Infinite & Negative Values
       ↓
Remove Duplicate Records
       ↓
Validate Cleaned Data
       ↓
Clean Employee CSV
```

## 📊 Result

The cleaning process produced a more consistent employee dataset by:

* Handling missing numerical values
* Handling missing categorical values
* Replacing invalid and infinite values
* Removing duplicate records
* Improving overall data quality

The cleaned dataset can now be used for **Exploratory Data Analysis (EDA), visualization, and further analytics**.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Install the required libraries

```bash
pip install pandas numpy
```

### 3. Run the cleaning script

```bash
python cleaning.py
```

## 👨‍💻 Author

**Abhijit Shetake**

B.Tech Computer Science & Engineering

### ⭐ Skills Demonstrated

**Python | Pandas | NumPy | Data Cleaning | Data Preprocessing | Data Analytics**
