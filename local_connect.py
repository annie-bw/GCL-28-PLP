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

    while True:
        name = input("Enter business name: ").strip()
        if name:
            break
        print("❌ Business name cannot be empty.")

    while True:
        category = input("Enter category (e.g., Restaurant, Salon): ").strip()
        if category:
            break
        print("❌ Category cannot be empty.")

    while True:
        location = input("Enter location (city or area): ").strip().lower()
        if location:
            break
        print("❌ Location cannot be empty.")

    while True:
        contact = input("Enter contact (Phone or Email): ").strip()
        if contact:
            break
        print("❌ Contact cannot be empty.")

    while True:
        website = input("Enter website: ").strip()
        if website:
            break
        print("❌ website cannot be empty.")

    conn = sqlite3.connect("local_connect.db")
    cursor = conn.cursor()
    # Check for exact duplicate
    cursor.execute('''
        SELECT * FROM businesses
        WHERE name = ? AND location = ? AND category = ? AND contact = ? AND website = ?
    ''', (name, location, category, contact, website))

    if cursor.fetchone():
        print("❌ Business already exists with the same details. Try again.")
        conn.close()
        return
    # Insert new business
    cursor.execute('''
        INSERT INTO businesses (name, location, category, contact, website)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, location, category, contact, website))
    conn.commit()
    conn.close()
    print(f"✅ {name} has been added successfully!\n")

