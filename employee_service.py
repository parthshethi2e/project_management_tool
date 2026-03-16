import sqlite3

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