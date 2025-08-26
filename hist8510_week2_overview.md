Methods in Digital History III
Dr. Amanda Regan

Week 2: Unit 1: Data Infrastructure and Management

Readings:
- Read through Geek for Geeks, [SQL Tutorial](https://www.geeksforgeeks.org/sql/sql-tutorial/)
- DeBarros, Practical Guide to SQL, Ch 1-8
- Install VS Code Extensions
    - Search for: [SQLite by alexcvzz](https://open-vsx.org/extension/alexcvzz/vscode-sqlite)
    - Search for: [SQLite Viewer by Florian Klampfer](https://open-vsx.org/extension/qwtel/sqlite-viewer)

Notes
SQL and Python: Creating and Running Local Databases 
- SQL = structured query language 
- standard language for working with relational databases
- used across all database systems, not just SQLite
- commands like CREATE, INSERT, SELECT and they all work the same way in all database formats 
- others 
	- MySQL/PostgreSQL -- full database servers (require setup and admin)
	- Access or Filemaker Pro --desktop apps but not open source 
- SQLite - filebase structure. what tropy uses. very powerful, yet very lite. 
- Why SQlite?
	- cross platform
	- mo server setup
	- open source
	- ideal source under 1 million records
	- archive friendly - stored as simple files 
- Declarative vs. Procedural Languages
	- SQL is a declarative language
	- different from Python which is procedural
	- what does that mean?
		- in procedural:
			- step-by-step instructions
			- tells compute how to do something
			- specify the sequence of operations
		- in declarative:
			- what you want
			- system figures out how to get it 
		- key difference:
			- procedural: go through all, select the ones that apply
			- declarative: find me all that apply
	- uses english like commands -- SELECT INSTER CREATE DELETE
		- COMMAND target FROM source WHERE conditions 
		- SELECT title, city FROM venues WHERE type =  'bar'
- CREATE - build database structure
	- CREATE TABLE cities (
		city_id INTEGER PRIMARY KEY,
		city_name TEXT NOT NULL,
		state TEXT
		);
- INSERT - add new data
	- INSERT INTO cities
		( 
- SELECT - retrieves data 
- UPDATE - modifies existing data 
		- UPDATE cities SET 
- DELETE - duh 
- SQL Data types
	- TEXT - for names, descriptions, addresses
	- INTEGERS - names, counts, IDs
	- REAL - coordinates, ratings, measurements 
	- NULL - missing data
- SQL Data Constraints 
	- PRIMARY KEY - unique identifier for each record 
	- FOREIGN KEY - links to another table 
	- NOT NULL - field must have a value 
		- keys yes, but hardly any other circumstance you want that
	- UNIQUE - prevents duplicates 
- running SQL code in python
	- can't talk directly to SQLite in Python
	- you need an intermediary - the cursor 
	- think of it like: 
		- connection(conn) = phone line to the database
		- cursor = actual conversation your having
	- a cursor  
		- is like a pointer pr messenger that sends command to database 
import sqlite3
conn = sqlite3.connect('database.db')
cursor=con.cursor


conn.commit()
conn.close()