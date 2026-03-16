import sqlite3

# Create connection
conn = sqlite3.connect("employees.db", check_same_thread=False)
cursor = conn.cursor()

# Drop existing table to start fresh (optional: comment out if you want to keep existing data)
cursor.execute("DROP TABLE IF EXISTS employees")

# Create employees table with UNIQUE constraint on email
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    designation TEXT NOT NULL,
    skills TEXT,
    allocation INTEGER DEFAULT 0
)
""")

conn.commit()

# Use INSERT OR IGNORE to prevent duplicate entries on re-runs
cursor.execute("""
INSERT OR IGNORE INTO employees (name, email, designation, skills, allocation)
VALUES
('Parth Sheth','parth.sheth58@gmail.com','iOS Developer','ios,swift',60),
('Saurav Singh','parth.ycmou2015@gmail.com','Android Developer','kotlin',60),
('Bhavya','parthsandeepsheth@gmail.com','Web Developer','react,node',30)
""")

conn.commit()

# Verify inserted data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Employees in database:")
for row in rows:
    print(row)

conn.close()
print("\nDatabase setup complete.")