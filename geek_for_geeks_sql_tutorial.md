Author: Geek for Geeks
PhD: 
Title: [SQL Tutorial](https://www.geeksforgeeks.org/sql/sql-tutorial/)
Year: 
Assigned Pages: 
Access: pdf
Class: Digital Methods III
Date: 2025-08-25
Topic: Data Infrastructure and Management
Tags: #digital #data_infastructure #data_management

Notes:
- Structured Query Language (SQL) is the standard language used to interact with relational databases.
- - ****End with Semicolon (******`**;**`******)****: Each SQL statement must end with a semicolon to execute properly.
- ****Case Insensitivity****: SQL keywords (e.g., `SELECT`, `INSERT`) are not case-sensitive. However, table/column names may be case-sensitive depending on the DBMS.
- ****Whitespace Allowed****: Queries can span multiple lines, but use spaces between keywords and names.
- ****Reserved Words****: Avoid using SQL keywords as names. If needed, wrap them in quotes (`" "`) or backticks (`` ` ``).
- ****String Values****: Enclose strings in single quotes (`'text'`).
- SELECT first_name, last_name, hire_date  
FROM employees  
WHERE department = 'Sales'  
ORDER BY hire_date DESC;
	- This query retrieves employees' first and last names, along with their hire dates, from the employees table, specifically for those in the 'Sales' department, sorted by hire date.
- 