import csv
import sqlite3
import os
from collections import Counter, defaultdict

# Paths
CSV_PATH = '/Users/eahorton/Downloads/19th_century_divorce_petitions_clean - Sheet1.csv'
DB_PATH = 'divorce_petitions.db'

# Read CSV and collect data
rows = []
with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)

# --- County Table ---
county_counts = defaultdict(int)
for row in rows:
    key = (row['county'], row['state'])
    county_counts[key] += 1
county_list = []
for idx, ((county, state), count) in enumerate(county_counts.items(), 1):
    county_list.append((idx, county, state, count))

# --- Petitioner Table ---
petitioner_set = set()
petitioner_list = []
for row in rows:
    key = (row['parcel_number'], row['relation_of_petitioner'])
    if key[0] not in petitioner_set:
        petitioner_set.add(key[0])
        petitioner_list.append(key)

# --- Relation Table ---
relation_counter = Counter(row['relation_of_petitioner'] for row in rows)
relation_list = []
for idx, (relation, count) in enumerate(relation_counter.items(), 1):
    relation_list.append((idx, relation, count))

# --- Reasoning Table ---
reason_counter = Counter()
for row in rows:
    reasoning = row.get('reasoning', '')
    if reasoning:
        terms = [t.strip() for t in reasoning.split(',') if t.strip()]
        reason_counter.update(terms)
reason_list = []
for idx, (term, count) in enumerate(reason_counter.items(), 1):
    reason_list.append((idx, term, count))

# --- Create SQLite DB ---
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE County (
    county_id INTEGER PRIMARY KEY,
    county TEXT,
    state TEXT,
    record_count INTEGER
)''')
c.execute('''CREATE TABLE Petitioner (
    parcel_number TEXT PRIMARY KEY,
    relation_of_petitioner TEXT
)''')
c.execute('''CREATE TABLE Relation (
    relation_id INTEGER PRIMARY KEY,
    relation_of_petitioner TEXT,
    relation_count INTEGER
)''')
c.execute('''CREATE TABLE Reasoning (
    reasoning_id INTEGER PRIMARY KEY,
    reasoning_term TEXT,
    reasoning_count INTEGER
)''')

# Insert data
c.executemany('INSERT INTO County (county_id, county, state, record_count) VALUES (?, ?, ?, ?)', county_list)
c.executemany('INSERT INTO Petitioner (parcel_number, relation_of_petitioner) VALUES (?, ?)', petitioner_list)
c.executemany('INSERT INTO Relation (relation_id, relation_of_petitioner, relation_count) VALUES (?, ?, ?)', relation_list)
c.executemany('INSERT INTO Reasoning (reasoning_id, reasoning_term, reasoning_count) VALUES (?, ?, ?)', reason_list)

conn.commit()
conn.close()
print('Database created as', DB_PATH)
