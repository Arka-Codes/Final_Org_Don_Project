from scripts.initialize_db import create_tables
from scripts.populate_db import populate_data
from app.matching_algorithm import fetch_data_from_db, match_donors_to_recipients

def main():
    print("Initializing the system...")

    # Step 1: Create tables if not already created
    create_tables()

    # Step 2: Insert data into the table
    populate_data()

    # Step 3: Fetch the data
    donors, recipients = fetch_data_from_db()
    print("Data collected in donors and recipients.")

    # Step 4: Run the matching algorithm
    print("Running the matching algorithm...")
    matches = match_donors_to_recipients(donors, recipients)

    # Step 5: Display matches
    print("Matching complete. Here are the results:")
    for match in matches:
        print(f"Donor ID {match['donor_id']} matched with Recipient ID {match['recipient_id']}. Score: {match['score']:.2f}")

if __name__ == "__main__":
    main()