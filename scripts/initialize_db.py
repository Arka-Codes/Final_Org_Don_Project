import sqlite3

# Path to the SQLite database
db_path = "organ_matching.db"

def create_tables():
    """
    Function to create the necessary tables in the SQLite database.
    """
    # Connect to SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL commands to create tables
    create_donors_table = """
    CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        organ_type TEXT NOT NULL,
        blood_type TEXT NOT NULL,
        body_size REAL NOT NULL,
        gps_lat REAL NOT NULL,
        gps_long REAL NOT NULL,
        tissue_type TEXT NOT NULL,
        health_score REAL NOT NULL
    );
    """

    create_recipients_table = """
    CREATE TABLE IF NOT EXISTS recipients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        organ_type TEXT NOT NULL,
        blood_type TEXT NOT NULL,
        body_size REAL NOT NULL,
        gps_lat REAL NOT NULL,
        gps_long REAL NOT NULL,
        tissue_type TEXT NOT NULL,
        medical_urgency INTEGER NOT NULL,
        time_on_list INTEGER NOT NULL,
        organ_score REAL NOT NULL
    );
    """
    # Execute SQL commands
    cursor.execute(create_donors_table)
    cursor.execute(create_recipients_table)

    # Commit and close connection
    conn.commit()
    conn.close()

create_tables()


print("Database tables created successfully.")