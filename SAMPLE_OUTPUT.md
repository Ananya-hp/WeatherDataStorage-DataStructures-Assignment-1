📅 Enter number of years:

2

📅 Enter years:

Year 1: 2021

Year 2: 2022

🏙 Enter number of cities:

2

🏙 Enter cities:

City 1: Delhi

City 2: Mumbai

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
 
Enter choice: 1

Date (DD/MM/YYYY): 10/9/2021

City: Delhi

Temperature: 39.5

✅ Record inserted.

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
   
Enter choice: 1

Date (DD/MM/YYYY): 10/12/2022

City: Mumbai

Temperature: 35.5

✅ Record inserted.

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
 
Enter choice: 3

Year: 2021

City: Delhi

🌡 [10/9/2021] Delhi: 39.5°C

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
 
Enter choice: 4

🔍 Row-Major Traversal:

(2021, Delhi) = [10/9/2021] Delhi: 39.5°C

(2021, Mumbai) = None

(2022, Delhi) = None

(2022, Mumbai) = [10/12/2022] Mumbai: 35.5°C

✅ Row-major traversal complete.

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit

Enter choice: 5

🔍 Column-Major Traversal:

(2021, Delhi) = [10/9/2021] Delhi: 39.5°C

(2022, Delhi) = None

(2021, Mumbai) = None

(2022, Mumbai) = [10/12/2022] Mumbai: 35.5°C

✅ Column-major traversal complete.

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
 
Enter choice: 6

📦 Sparse Representation:

(2021, 'Delhi'): 39.5°C

(2022, 'Mumbai'): 35.5°C

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
   
Enter choice: 7

📊 Time & Space Complexity:

Insert/Delete/Retrieve: O(1) time, O(1) space

Row/Column Traversal: O(4) time

Sparse Representation: O(N) space, where N = number of non-missing records

📋 --- Weather Data Menu ---
1. Insert Record
2. Delete Record
3. Retrieve Record
4. Row-Major Traversal
5. Column-Major Traversal
6. Sparse Representation
7. Complexity Analysis
0. Exit
   
Enter choice: 2

Date (DD/MM/YYYY): 10/9/2021

City: Delhi

🗑 Record deleted.

