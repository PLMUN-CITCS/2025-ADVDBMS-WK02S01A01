import psycopg2
import os

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def execute_student_script(conn, script_path):
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
    cur.execute(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = '{table_name}');")
    return cur.fetchone()[0]

# ... (Add more test functions for columns, data, views, queries) ...

if __name__ == "__main__":
    conn = connect_to_db()
    if not conn:
        exit(1)

    # Get student's SQL scripts (assuming they are in the 'sql_scripts' directory)
    student_scripts_dir = ["scripts/01_create_tables.sql", "scripts/02_insert_data.sql"] 
    for filename in student_scripts_dir:
        if filename.endswith(".sql"):
            if execute_student_script(conn, filename):
                print(f"{filename} executed successfully.")
                # Run tests and generate feedback
                # ... (Call test functions and print results) ...
            else:
                print(f"Error executing {filename}.")

    conn.close()