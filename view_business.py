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

