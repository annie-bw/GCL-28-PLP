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

# ----- VIEW ALL BUSINESSES -----

def view_businesses():
    print("\nThe Following Are Available Businesses")
    print("-------------------------")
    conn = sqlite3.connect("local_connect.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name, category, location, contact, avg_rating FROM businesses")
    businesses = cursor.fetchall()
    if businesses:
        for b in businesses:
            business_id = b[0]
            avg_rating = get_avg_rating(business_id)
            print(
                f"ID: {b[0]} | Name: {b[1]} | Category: {b[2]} | Location: {b[3]} | Contact: {b[4]} | ⭐ {avg_rating}")
    else:
        print("❌ No businesses found.")
    conn.close()

# ----- SEARCH BUSINESSES -----


def search_businesses():
    print("\nYou have selected: Search for Businesses")
    print("-------------------------------------")

    while True:
        location = input("Enter location (city or area): ").strip().lower()
        if location:
            break
        print("❌ Location cannot be empty.")
    filter_category = input(
        "Would you like to filter by category? (Y/N): ").strip().lower()

    conn = sqlite3.connect("local_connect.db")
    cursor = conn.cursor()
    if filter_category == 'y':
        while True:
            category = input(
                "Enter category (e.g., Salon, Restaurant): ").strip().lower()
            if category:
                break
            print("❌ Category cannot be empty.")
        cursor.execute("""
        SELECT id, name, category, location, contact, avg_rating
        FROM businesses
        WHERE LOWER(location) LIKE ? AND category LIKE ?""",
                       (f"%{location}%", f"%{category}%"))
    else:
        cursor.execute("""
        SELECT id, name, category, location, contact, avg_rating
        FROM businesses
        WHERE LOWER(location) LIKE ?""", (f"%{location}%",))

    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for b in results:
            print(
                f"ID: {b[0]} | Name: {b[1]} | Category: {b[2]} | Location: {b[3]} | Contact: {b[4]} | ⭐ {b[5]:.1f}")
    else:
        print("❌ No businesses found.")
    conn.close()
    print()
