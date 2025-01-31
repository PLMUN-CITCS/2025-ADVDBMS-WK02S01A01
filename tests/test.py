import psycopg2
import os

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "TEST_DB"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS", "secured123")
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
        cur.execute(sql_script)
        conn.commit()
    except Exception as e:
        print(f"Error executing script: {e}")
        return False
    return True

def test_table_exists(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables WHERE table_name = '{table_name}'
        );
    """)
    return cur.fetchone()[0]

def check_student_exists(conn, name, email, phone):
    cur = conn.cursor()
    query = """
        SELECT COUNT(*) FROM tblStudents 
        WHERE student_name = %s AND student_email = %s AND student_phone = %s;
    """
    cur.execute(query, (name, email, phone))
    return cur.fetchone()[0] > 0

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
                elif filename == "scripts/02_insert_data.sql":
                    print("Data inserted successfully.")
            else:
                print(f"Error executing {filename}.")
                print("Please check the SQL syntax and try again.")

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
