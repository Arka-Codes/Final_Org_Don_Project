import sqlite3
from geopy.distance import geodesic

# Connect to SQLite database
db_path = "E:\Important\Coding\Python\OrgDonProj3\organ_matching.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Function to fetch donor and recipient data from the database
def fetch_data_from_db():
    cursor.execute("SELECT * FROM donors")
    donors = [
        {
            "id": row[0],
            "organ_type": row[1],
            "blood_type": row[2],
            "body_size": row[3],
            "gps_lat": row[4],
            "gps_long": row[5],
            "tissue_type": row[6],
            "health_score": row[7],
        }
        for row in cursor.fetchall()
    ]

    cursor.execute("SELECT * FROM recipients")
    recipients = [
        {
            "id": row[0],
            "organ_type": row[1],
            "blood_type": row[2],
            "body_size": row[3],
            "gps_lat": row[4],
            "gps_long": row[5],
            "tissue_type": row[6],
            "medical_urgency": row[7],
            "time_on_list": row[8],
            "organ_score": row[9],
        }
        for row in cursor.fetchall()
    ]

    return donors, recipients

# Function to calculate match score
def calculate_match_score(donor, recipient):
    score = 0

    # Match organ type
    if donor["organ_type"] != recipient["organ_type"]:
        return 0  # Skip if organ types don't match

    # 1. Blood Type Match
    if donor["blood_type"] == recipient["blood_type"]:
        score += 50
    else:
        return 0  # Incompatible blood type

    # 2. Tissue Type Match
    if donor["tissue_type"] == recipient["tissue_type"]:
        score += 20

    # 3. Organ Health and Compatibility
    score += donor["health_score"] * 0.4  # Weight of donor organ health
    score += recipient["organ_score"] * 0.6  # Weight of recipient's organ-specific score

    # 4. Medical Urgency
    score += recipient["medical_urgency"] * 5

    # 5. Body Size Compatibility (Body Size - body weight/body surface area/height)
    size_diff = abs(donor["body_size"] - recipient["body_size"])
    if size_diff <= 10:
        score += 15 - size_diff

    # 6. Geographical Proximity
    donor_location = (donor["gps_lat"], donor["gps_long"])
    recipient_location = (recipient["gps_lat"], recipient["gps_long"])
    distance = geodesic(donor_location, recipient_location).kilometers
    if distance <= 500:
        score += 10
    elif distance <= 1000:
        score += 5

    # 7. Time on Waiting List
    score += recipient["time_on_list"] / 100

    return score

# Matching algorithm
def match_donors_to_recipients(donors, recipients):
    matches = []

    for donor in donors:
        best_match = None
        highest_score = 0

        for recipient in recipients:
            # Ensure both are compatible in organ type
            if donor["organ_type"] == recipient["organ_type"]:
                score = calculate_match_score(donor, recipient)
                if score > highest_score:
                    highest_score = score
                    best_match = recipient

        if best_match:
            matches.append({"donor_id": donor["id"], "recipient_id": best_match["id"], "score": highest_score})
            recipients.remove(best_match)  # Prevent duplicate matching

    return matches
