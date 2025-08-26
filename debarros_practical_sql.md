Author: Anthony DeBarros
PhD: 
Title: *Practical SQL: A Beginner's Guide to Storytelling with Data*
Year: 
Assigned Pages: ch. 1-8
Access: pdf
Class: Digital Methods III
Date: 2025-08-25
Topic: Data Infrastructure and Management
Tags: #digital #data_infastructure #data_management

Anthony DeBarros is an award-winning journalist who has combined avid interests in data analysis, coding, and storytelling for much of his career. He spent more than 25 years with the Gannett company, including the Poughkeepsie Journal, USA TODAY, and Gannett Digital. He is currently senior vice president for content and product development for a publishing and events firm and lives and works in the Washington, D.C., area

Chapter 1: Creating Your First Database and Table 
Chapter 2: Beginning Data Exploration with SELECT 
Chapter 3: Understanding Data Types 
Chapter 4: Importing and Exporting Data 
Chapter 5: Basic Math and Stats with SQL 
Chapter 6: Joining Tables in a Relational Database 
Chapter 7: Table Design That Works for You 
Chapter 8: Extracting Information by Grouping and Summarizing

Notes:
Chapter 1: Creating Your First Database and Table 
- SQL is more than just a means for extracting knowledge from data. It’s also a language for defining the structures that hold data so we can organize relationships in the data. Chief among those structures is the table.
- Database builders prefer to organize data using separate tables for each main entity the database manages in order to reduce redundant data. In the example, we store each student’s name and date of birth just once. Even if the student signs up for multiple classes—as Davis Hernandez did—we don’t waste database space entering his name next to each class in the student_enrollment table. We just include his student ID.
- The statement ends with a semicolon, which signals the end of the command.
- SQL requires no special formatting to run, so you’re free to use your own psychedelic style of uppercase, lowercase, and random indentations. But that won’t win you any friends when others need to work with your code (and sooner or later someone will). For the sake of readability and being a good coder, it’s best to follow these conventions: 
	- Uppercase SQL keywords, such as SELECT. Some SQL coders also uppercase the names of data types, such as TEXT and INTEGER. I use lowercase characters for data types in this book to separate them in your mind from keywords, but you can uppercase them if desired. 
	- Avoid camel case and instead use lowercase_and_underscores for object names, such as tables and column names (see more details about case in Chapter 7).
	- Indent clauses and code blocks for readability using either two or four spaces. Some coders prefer tabs to spaces; use whichever works best for you or your organization.
Chapter 2: Beginning Data Exploration with SELECT 
- Think of interviewing data as a process akin to interviewing a person applying for a job. You want to ask questions that reveal whether the reality of their expertise matches their resume.
- In SQL, interviewing data starts with the SELECT keyword, which retrieves rows and columns from one or more of the tables in a database. A SELECT statement can be simple, retrieving everything in a single table, or it can be complex enough to link dozens of tables while handling multiple calculations and filtering by exact criteria.
- Note that the id column (of type bigserial) automatically fills with sequential integers, even though you didn’t explicitly insert them. Very handy. This auto-incrementing integer acts as a unique identifier, or key, that not only ensures each row in the table is unique, but also will later give us a way to connect this table to other tables in the database.
- In a table, it’s not unusual for a column to contain rows with duplicate values. In the teachers table, for example, the school column lists the same school names multiple times because each school employs many teachers.
- Comparison operators are fairly straightforward, but LIKE and ILIKE deserve additional explanation. First, both let you search for patterns in strings by using two special characters: 
	- Percent sign (%) A wildcard matching one or more characters 
	- Underscore (_) A wildcard matching just one character
- The difference? The LIKE operator, which is part of the ANSI SQL standard, is case sensitive. The ILIKE operator, which is a PostgreSQLonly implementation, is case insensitive. Listing 2-8 shows how the two keywords give you different results. The first WHERE clause uses LIKE ➊ to find names that start with the characters sam, and because it’s case sensitive, it will return zero results. The second, using the case-insensitive ILIKE ➋, will return Samuel and Samantha from the table:
- Over the years, I’ve gravitated toward using ILIKE and wildcard operators in searches to make sure I’m not inadvertently excluding results from searches. I don’t assume that whoever typed the names of people, places, products, or other proper nouns always remembered to capitalize them. And if one of the goals of interviewing data is to understand its quality, using a case-insensitive search will help you find variations

Chapter 3: Understanding Data Types 
- Whenever I dig into a new database, I check the data type specified for each column in each table. If I’m lucky, I can get my hands on a data dictionary: a document that lists each column; specifies whether it’s a number, character, or other type; and explains the column values. Unfortunately, many organizations don’t create and maintain good documentation, so it’s not unusual to hear, “We don’t have a data dictionary.” In that case, I try to learn by inspecting the table structures in pgAdmin.
- Insert the double colon in between the name of the column and the data type you want to convert it to.

Chapter 4: Importing and Exporting Data 

Chapter 5: Basic Math and Stats with SQL 
- If your data includes any of the number data types we explored in Chapter 3—integers, decimals, or floating points—sooner or later your analysis will include some calculations. For example, you might want to know the average of all the dollar values in a column, or add values in two columns to produce a total for each row. SQL handles calculations ranging from basic math through advanced statistics
Chapter 6: Joining Tables in a Relational Database 
- The values in this column refer to values in the departments table’s primary key. We call this a foreign key, which you add as a constraint ➌ when creating the table. A foreign key constraint requires a value entered in a column to already exist in the primary key of the table it references. So, values in dept_id in the employees table must exist in dept_id in the departments table; otherwise, you can’t add them. Unlike a primary key, a foreign key column can be empty, and it can contain duplicate values. 
- Second, cramming unrelated data into one table makes managing the data difficult.
- JOIN Returns rows from both tables where matching values are found in the joined columns of both tables. Alternate syntax is INNER JOIN.
- LEFT JOIN Returns every row from the left table plus rows that match values in the joined column from the right table. When a left table row doesn’t have a match in the right table, the result shows no values from the right table.
- RIGHT JOIN Returns every row from the right table plus rows that match the key values in the key column from the left table. When a right table row doesn’t have a match in the left table, the result shows no values from the left table.
- FULL OUTER JOIN Returns every row from both tables and matches rows; then joins the rows where values in the joined columns match. If there’s no match for a value in either the left or right table, the query result contains an empty row for the other table.
- CROSS JOIN Returns every possible combination of rows from both tables.
- You’d use either of these join types (right or left) in a few circumstances: You want your query results to contain all the rows from one of the tables. You want to look for missing values in one of the tables; for example, when you’re comparing data about an entity representing two different time periods. When you know some rows in a joined table won’t have matching values.
- Being able to reveal missing data from one of the tables is valuable when you’re digging through data. Any time you join tables, it’s wise to vet the quality of the data and understand it better by discovering whether all key values in one table appear in another. There are many reasons why a discrepancy might exist, such as a clerical error, incomplete output from the database, or some change in the data over time. All this information is important context for making correct inferences about the data.
- Part of the science (or art, some may say) of joining tables involves understanding how the database designer intends for the tables to relate, also known as the database’s relational model. The three types of table relationships are one to one, one to many, and many to many.
Chapter 7: Table Design That Works for You 
- When you organize data into a finely tuned, smartly named set of tables, the analysis experience becomes more manageable. In this chapter, I’ll build on Chapter 6 by introducing best practices for organizing and tuning SQL databases, whether they’re yours or ones you inherit for analysis. You already know how to create basic tables and add columns with the appropriate data type and a primary key. Now, we’ll dig deeper into table design by exploring naming rules and conventions, ways to maintain the integrity of your data, and how to add indexes to tables to speed up queries.
- Some prefer to use camel case, as in berrySmoothie, where words are strung together and the first letter of each word is capitalized except for the first word. Pascal case, as in BerrySmoothie, follows a similar pattern but capitalizes the first letter of the first word too. With snake case, as in berry_smoothie, all the words are lowercase and separated by underscores. So far, I’ve been using snake case in most of the examples, such as in the table us_counties_2010.
	-  i use snake case
- Using quotation marks also permits characters not otherwise allowed in an identifier, including spaces. But be aware of the negatives of using this method: for example, you might want to throw quotes around "trees planted" and use that as a column name in a reforestation database, but then all users will have to provide quotes on every subsequent reference to that column. Omit the quotes and the database will respond with an error, identifying trees and planted as separate columns missing a comma between them. A more readable and reliable option is to use snake case, as in trees_planted.
- For table names, use plurals. Tables hold rows, and each row represents one instance of an entity. So, use plural names for tables, such as teachers, vehicles, or departments. 
- Mind the length. The maximum number of characters allowed for an identifier name varies by database application: the SQL standard is 128 characters, but PostgreSQL limits you to 63, and the Oracle system maximum is 30. If you’re writing code that may get reused in another database system, lean toward shorter identifier names.
- When making copies of tables, use names that will help you manage them later. One method is to append a YYYY_MM_DD date to the table name when you create it, such as tire_sizes_2017_10_20. An additional benefit is that the table names will sort in date order.
- With the foreign key constraint, SQL very helpfully provides a way to ensure data in related tables doesn’t end up unrelated, or orphaned. A foreign key is one or more columns in a table that match the primary key of another table. But a foreign key also imposes a constraint: values entered must already exist in the primary key or other unique key of the table it references. If not, the value is rejected. This constraint ensures that we don’t end up with rows in one table that have no relation to rows in the other tables we can join them to.
- Second, the reverse applies when we delete data. To maintain referential integrity, the foreign key constraint prevents us from deleting a row from licenses before removing any related rows in registrations, because doing so would leave an orphaned record. We would have to delete the related row in registrations first, and then delete the row in licenses. However, ANSI SQL provides a way to handle this order of operations automatically using the ON DELETE CASCADE keywords, which I’ll discuss next.
- We can also ensure that a column has a unique value in each row by using the UNIQUE constraint. If ensuring unique values sounds similar to the purpose of a primary key, it is. But UNIQUE has one important difference. In a primary key, no values can be NULL, but a UNIQUE constraint permits multiple NULL values in a column
Chapter 8: Extracting Information by Grouping and Summarizing
- Both max() and min() work the same way: you use a SELECT statement followed by the function with the name of a column supplied. Listing 8-6 uses max() and min() on the 2014 table with the visits column as input. The visits column records the number of annual visits to the library agency and all of its branches. Run the code, and then we’ll review the output.
- When you use the GROUP BY clause with aggregate functions, you can group results according to the values in one or more columns. This allows us to perform operations like sum() or count() for every state in our table or for every type of library agency.
- So far, we’ve combined grouping with aggregate functions, like count(), on columns within a single table to provide results grouped by a column’s values. Now let’s expand the technique to include grouping and aggregating across joined tables using the 2014 and 2009 libraries data. Our goal is to identify trends in library visits spanning that five-year period. To do this, we need to calculate totals using the sum() aggregate function.
- You also learned that data doesn’t always come perfectly packaged. The use of negative values in columns as an indicator rather than as an actual numeric value forced us to filter out those rows. Unfortunately, data sets offer those kinds of challenges more often than not. In the next chapter, you’ll learn techniques to clean up a data set that has a number of issues. In subsequent chapters, you’ll also discover more aggregate functions to help you find the stories in your data.