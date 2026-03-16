import sqlite3
from database import conn

DB_PATH = "employees.db"



def get_employees_by_role(role):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    try:
        cursor = conn.cursor()

        query = """
        SELECT name, email, allocation
        FROM employees
        WHERE designation = ?
        ORDER BY allocation ASC
        """

        cursor.execute(query, (role,))
        rows = cursor.fetchall()

        employees = []
        for row in rows:
            employees.append({
                "name": row[0],
                "email": row[1],
                "allocation": row[2]
            })

        return employees
    finally:
        conn.close()
        
        
def get_employee_by_email(email):

    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name FROM employees
    WHERE email = ?
    """, (email,))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return "Developer"