import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('attendance_system.db')

# Create a cursor
c = conn.cursor()

# Create a table for employee data
c.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL
)
''')

# Create a table for attendance records
c.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
def add_employee(name, position):
    conn = sqlite3.connect('attendance_system.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, position) VALUES (?, ?)", (name, position))
    conn.commit()
    conn.close()
    print(f"Employee '{name}' added successfully!")
def mark_attendance(employee_id, date, status):
    conn = sqlite3.connect('attendance_system.db')
    c = conn.cursor()
    c.execute("INSERT INTO attendance (employee_id, date, status) VALUES (?, ?, ?)",
              (employee_id, date, status))
    conn.commit()
    conn.close()
    print(f"Attendance marked for Employee ID {employee_id} on {date} as {status}")
def view_attendance():
    conn = sqlite3.connect('attendance_system.db')
    c = conn.cursor()
    c.execute('''
    SELECT e.name, a.date, a.status
    FROM attendance a
    JOIN employees e ON a.employee_id = e.employee_id
    ''')
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(f"Employee: {row[0]}, Date: {row[1]}, Status: {row[2]}")
def view_employees():
    conn = sqlite3.connect('attendance_system.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}")
def menu():
    print("""
    ==== Employee Attendance System ====
    1. Add Employee
    2. Mark Attendance
    3. View Attendance Records
    4. View All Employees
    5. Exit
    """)

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            add_employee(name, position)
        
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter status (Present, Absent, Late): ")
            mark_attendance(employee_id, date, status)
        
        elif choice == '3':
            view_attendance()
        
        elif choice == '4':
            view_employees()
        
        elif choice == '5':
            print("Exiting Attendance System. Goodbye!")
            break
        
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
