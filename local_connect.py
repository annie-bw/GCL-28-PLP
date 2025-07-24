import sqlite3

# ----- DATABASE SETUP -----


def create_tables():
    conn = sqlite3.connect("local_connect.db")
    cursor = conn.cursor()
    # Table for businesses
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS businesses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        location TEXT NOT NULL,
        contact TEXT NOT NULL,
        website TEXT,
        avg_rating REAL DEFAULT 0
    )
    """)
    # Table for reviews
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        business_id INTEGER,
        reviewer_name TEXT,
        rating INTEGER,
        comment TEXT,
        FOREIGN KEY (business_id) REFERENCES businesses (id)
    )
    """)
    conn.commit()
    conn.close()

# ----- ADD A NEW BUSINESS -----


def add_business():
    print("\nYou have selected: Add a New Business")
    print("-----------------------------------")
    name = input("Enter business name: ")
    category = input("Enter category (e.g., Restaurant, Salon): ")
    location = input("Enter location (city or area): ").lower()
    contact = input("Enter contact (Phone or Email): ")
    website = input("Enter website (optional): ")

    conn = sqlite3.connect("local_connect.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO businesses (name, category, location, contact, website)
    VALUES (?, ?, ?, ?, ?)
    """, (name, category, location, contact, website))
    conn.commit()
    conn.close()
    print(f"✔ {name} has been added successfully!\n")

