import mysql.connector
import os

def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", "4000")),
            database=os.getenv("DB_NAME", "TEST_DB"),
            user=os.getenv("DB_USER", "root"),
            password=""
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_sql_script(conn, script_path):
    with open(script_path, "r") as file:
        sql_script = file.read()
    try:
        cur = conn.cursor()
        for statement in sql_script.split(";"):  # Split to handle multiple statements
            if statement.strip():
                cur.execute(statement)
        conn.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error executing script: {e}")
        return False

def test_table_exists(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"SHOW TABLES LIKE '{table_name}'")
    exists = cur.fetchone() is not None
    cur.close()
    return exists

def check_student_exists(conn, name, email, phone):
    cur = conn.cursor()
    query = """
        SELECT COUNT(*) FROM tblStudents 
        WHERE student_name = %s AND student_email = %s AND student_phone = %s;
    """
    cur.execute(query, (name, email, phone))
    exists = cur.fetchone()[0] > 0
    cur.close()
    return exists

if __name__ == "__main__":
    conn = connect_to_db()
    if not conn:
        exit(1)

    student_scripts_dir = ["scripts/01_create_tables.sql", "scripts/02_insert_data.sql"]
    for filename in student_scripts_dir:
        if filename.endswith(".sql"):
            if execute_sql_script(conn, filename):
                print(f"{filename} executed successfully.")
                if filename == "scripts/01_create_tables.sql":
                    if test_table_exists(conn, "tblStudents"):
                        print("Table 'tblStudents' created successfully.")
                    else:
                        print("Table 'tblStudents' not created.")
                        exit(1)
                elif filename == "scripts/02_insert_data.sql":
                    print("Data inserted successfully.")
                    exit(1)
            else:
                print(f"Error executing {filename}.")
                print("Please check the SQL syntax and try again.")
                exit(1)

    # Check if specific students exist
    students_to_check = [
        ("John Doe", "johndoe@gmail.com", "123-456-7890"),
        ("Jane Doe", "janedoe@gmail.com", "123-456-7890")
    ]
    
    for name, email, phone in students_to_check:
        if check_student_exists(conn, name, email, phone):
            print(f"Student {name} exists in the database.")
        else:
            print(f"Student {name} does NOT exist in the database.")

    conn.close()
