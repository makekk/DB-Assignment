import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create Product_Category table
cursor.execute('''
    CREATE TABLE Product_Category (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create Product table with a foreign key constraint
cursor.execute('''
    CREATE TABLE Product (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Product_Category(id)
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()


# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create Product_Category table
cursor.execute('''
    CREATE TABLE Product_Category (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create Product table with a foreign key constraint
cursor.execute('''
    CREATE TABLE Product (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Product_Category(id)
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
