import sqlite3

# Connect to SQLite database
db_path = "organ_matching.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Sample data for donors
donors_data = [
    ("kidney", "A+", 70.0, 28.7041, 77.1025, "HLA-A", 85.0),
    ("liver", "O+", 65.0, 34.0522, -118.2437, "HLA-B", 90.0),
    ("heart", "B+", 75.0, 40.7128, -74.0060, "HLA-A", 80.0),
]

# Sample data for recipients
recipients_data = [
    ("liver", "O+", 68.0, 34.0522, -118.2437, "HLA-B", 10, 200, 30.0),
    ("heart", "B+", 74.0, 39.9042, 116.4074, "HLA-A", 8, 150, 40.0),  
    ("kidney", "A+", 72.0, 28.6139, 77.2090, "HLA-A", 5, 100, 25.0),   
]


def populate_data():
    # Insert data into donors table
    cursor.executemany("""
    INSERT INTO donors (organ_type,blood_type, body_size, gps_lat, gps_long, tissue_type, health_score)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, donors_data)

    # Insert data into recipients table
    cursor.executemany("""
    INSERT INTO recipients (organ_type,blood_type, body_size, gps_lat, gps_long, tissue_type, medical_urgency, time_on_list, organ_score)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, recipients_data)

    # Commit and close connection
    conn.commit()
    conn.close()

print("Sample data inserted successfully.")
