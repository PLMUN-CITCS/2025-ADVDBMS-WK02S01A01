import mysql.connector
import os
import time

def connect_to_db():
    """Establish connection to TiDB."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", "4000")),
            database=os.getenv("DB_NAME", "TEST_DB"),
            user=os.getenv("DB_USER", "root"),
            password="",
            autocommit=True  # TiDB does not support transactions in DDL
        )
        print("✅ Successfully connected to TiDB.")
        return conn
    except Exception as e:
        print(f"❌ Error connecting to TiDB: {e}")
        return None

def execute_sql_script(conn, script_path):
    """Execute an SQL script from a file."""
    with open(script_path, "r") as file:
        sql_script = file.read()

    try:
        cur = conn.cursor()
        for statement in sql_script.split(";"):  # Handle multiple statements
            if statement.strip():
                cur.execute(statement)
        cur.close()
        print(f"✅ Successfully executed {script_path}")
        return True
    except Exception as e:
        print(f"❌ Error executing script {script_path}: {e}")
        return False

def test_table_exists(conn, table_name):
    """Check if a table exists in TiDB."""
    cur = conn.cursor()
    query = f"""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = '{os.getenv("DB_NAME", "TEST_DB")}' 
        AND TABLE_NAME = '{table_name}';
    """
    cur.execute(query)
    exists = cur.fetchone()[0] > 0
    cur.close()
    return exists

def check_student_exists(conn, name, email, phone):
    """Check if a specific student exists."""
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
    conn = None
    max_retries = 5
    for attempt in range(max_retries):
        conn = connect_to_db()
        if conn:
            break
        print(f"🔄 Retrying connection... ({attempt + 1}/{max_retries})")
        time.sleep(5)

    if not conn:
        print("❌ Unable to connect to TiDB. Exiting.")
        exit(1)

    # Execute scripts
    sql_scripts = ["scripts/01_create_tables.sql", "scripts/02_insert_data.sql"]
    for script in sql_scripts:
        if execute_sql_script(conn, script):
            if script.endswith("01_create_tables.sql"):
                if test_table_exists(conn, "tblStudents"):
                    print("✅ Table 'tblStudents' exists.")
                else:
                    print("❌ Table 'tblStudents' not found.")
                    exit(1)
            elif script.endswith("02_insert_data.sql"):
                print("✅ Data inserted successfully.")
        else:
            print(f"❌ Failed to execute {script}.")
            exit(1)

    # Check students
    students_to_check = [
        ("John Doe", "johndoe@gmail.com", "123-456-7890"),
        ("Jane Doe", "janedoe@gmail.com", "123-456-7890")
    ]

    for name, email, phone in students_to_check:
        if check_student_exists(conn, name, email, phone):
            print(f"✅ Student {name} exists in the database.")
        else:
            print(f"❌ Student {name} NOT found in the database.")

    conn.close()
    print("✅ Connection closed.")
