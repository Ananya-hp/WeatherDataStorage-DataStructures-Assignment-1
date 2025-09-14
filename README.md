****🌦️Weather Data Storage System****

**📌 Project Overview**


This project is a Weather Data Storage System implemented in Python.
It allows users to store, retrieve, delete, and analyze weather temperature records for different years and cities.
The program also demonstrates concepts of 2D arrays, ADTs (Abstract Data Types), sparse representation, and complexity analysis.

**🛠️ Features**

1. Insert Record – Add a temperature record for a given city and year.

2. Delete Record – Remove an existing record by providing the date and city.

3. Retrieve Record – Get the stored temperature for a given city and year.

4. Row-Major Traversal – Display records row by row (year-wise).

5. Column-Major Traversal – Display records column by column (city-wise).

6. Sparse Representation – Show only the non-empty records to save memory.

7. Complexity Analysis – Prints the time and space complexity of operations.

**🏗️ ADT Design**


**WeatherRecord ADT**


**Attributes:**

- Date: string (e.g., "12/08/2025")

- City: string

- Temperature: float

**Methods:**

- insert(year, city, temperature)

- delete(date, city)

- retrieve(city, year)

**🗂️ Data Storage Class**


**WeatherDataStorage**

**Attributes:**


- years: list of years

- cities: list of cities

- data: 2D array (rows = years, columns = cities)

**Methods:**


- insert(year, city, temperature) – Add a record.

- delete(date, city) – Remove a record.

- retrieve(city, year) – Fetch a temperature.

- row_major_access() – Row-wise traversal.

- column_major_access() – Column-wise traversal.

- handle_sparse_data() – Store only non-empty records in dictionary form.

- analyze_complexity() – Print time and space complexity.

**🔄Row-Major vs Column-Major Traversal**

**Row-Major:**  Visit data row by row (year by year).

**Column-Major:**  Visit data column by column (city by city).

Both traversals are implemented to compare efficiency.

**📦 Handling Sparse Data**

In real datasets, many entries may be missing (None).

To save space, we create a **dictionary-based sparse representation:**

(year, city) → temperature

Only non-empty records are stored, which is more memory-efficient.

**📊 Complexity Analysis**

**Insert:** O(1)

**Delete:** O(1)

**Retrieve:** O(1)

**Row/Column Traversal:** O(M × N), where M = number of years, N = number of cities

**Sparse Representation:** O(N) space (where N = number of non-empty records)

**📂Project Structure**

│── SAMPLE_OUTPUT.md     # Example Program Output

│── Weather_Storage.py   # Main program file

│── README.md            # Documentation

**📊 Sample Menu (on running the program)**

📋 --- Weather Data Menu ---

1. Insert Record

2. Delete Record

3. Retrieve Record

4. Row-Major Traversal

5. Column-Major Traversal

6. Sparse Representation

7. Complexity Analysis

0. Exit

**🖥️Sample Run**

Enter number of years:2

Enter years:

Year 1: 2023

Year 2: 2024

Enter number of cities: 2

Enter cities:

City 1: Delhi

City 2: Mumbai

📋 --- Weather Data Menu ---

Enter choice: 1

Year: 2023

City: Delhi

Temperature: 32.5

✅ Record inserted.

Enter choice: 3

Year: 2023

City: Delhi

🌡️ Temperature in Delhi (2023) = 32.5°C

**🎯 Learning Outcomes**

- Implemented 2D array storage with mappings.

- Practiced row-major and column-major traversal.

- Learned how to build a sparse representation.

- Analyzed time and space complexity of ADT operations.


