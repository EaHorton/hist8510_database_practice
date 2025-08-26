# Divorce Petitions Database

## Data Model Summary

This SQLite3 database is built from 19th-century divorce petition records. It is designed to normalize and organize the data for analysis and querying. The database consists of four main tables:

### 1. County
- **Purpose:** Stores unique counties and their states, with a count of records per county.
- **Fields:**
  - `county_id` (INTEGER, PRIMARY KEY): Unique identifier for each county.
  - `county` (TEXT): Name of the county.
  - `state` (TEXT): State in which the county is located.
  - `record_count` (INTEGER): Number of records associated with the county.

### 2. Petitioner
- **Purpose:** Stores each unique parcel number and the relation of the petitioner.
- **Fields:**
  - `parcel_number` (TEXT, PRIMARY KEY): Unique identifier for each petition.
  - `relation_of_petitioner` (TEXT): Relation of the petitioner (e.g., husband, wife).

### 3. Relation
- **Purpose:** Stores each unique relation of petitioner, with a count of how many times each relation appears.
- **Fields:**
  - `relation_id` (INTEGER, PRIMARY KEY): Unique identifier for each relation.
  - `relation_of_petitioner` (TEXT): The relation (e.g., husband, wife).
  - `relation_count` (INTEGER): Number of times this relation appears in the data.

### 4. Reasoning
- **Purpose:** Stores each unique reasoning term (split by commas in the CSV), with a count of how many times each term appears.
- **Fields:**
  - `reasoning_id` (INTEGER, PRIMARY KEY): Unique identifier for each reasoning term.
  - `reasoning_term` (TEXT): The reasoning term (e.g., cruelty, desertion).
  - `reasoning_count` (INTEGER): Number of times this term appears in the data.

---

## Schema Diagram

```
+----------------+        +-------------------+
|    County      |        |    Petitioner     |
+----------------+        +-------------------+
| county_id (PK) |<--+    | parcel_number (PK)|
| county         |   |    | relation_of_      |
| state          |   |    | petitioner        |
| record_count   |   |    +-------------------+
+----------------+   |
                     |
+----------------+   |
|   Relation     |   |
+----------------+   |
| relation_id(PK)|   |
| relation_of_   |---+
| petitioner     |
| relation_count |
+----------------+

+----------------+ 
|   Reasoning    |
+----------------+
| reasoning_id(PK)|
| reasoning_term  |
| reasoning_count |
+----------------+
```

- **County** and **Petitioner** are linked conceptually by the data but not by a foreign key in this schema.
- **Relation** and **Reasoning** are lookup tables for normalized values and counts.

---

## Usage
- The database is created by running `build_divorce_db.py`.
- The resulting file is `divorce_petitions.db`.
- You can query the tables using any SQLite3 client.
