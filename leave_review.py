# ----- LEAVE A REVIEW -----


def leave_review():
    while True:
        reviewer_name = input(
            "Enter your name as a reviewer: ").strip().title()
        if reviewer_name:
            break
        print("❌ Reviewer name cannot be empty.")

    while True:
        name = input("Enter the business name: ").strip().lower()
        if name:
            break
        print("❌ Business name cannot be empty.")
    while True:
        location = input("Enter the business location: ").strip().lower()
        if location:
            break
        print("❌ Location cannot be empty.")

    conn = sqlite3.connect("local_connect.db")
    c = conn.cursor()

    # Find business with matching name and location
    c.execute("""
        SELECT id, name, location FROM businesses
        WHERE lower(name) LIKE ? AND lower(location) LIKE ?
    """, ('%' + name + '%', '%' + location + '%'))

    result = c.fetchone()

    if result:
        print(f"\nFound: {result[1].title()} located in {result[2].title()}")
        confirm = input(
            "Is this the business you want to review? (Y/N): ").strip().lower()

        if confirm == 'y':
            business_id = result[0]

            try:
                while True:
                    rating = int(input("Enter your rating (1-5): "))
                    if not rating:
                        print("❌ Rating cannot be empty.")
                        continue
                    if rating < 1 or rating > 5:
                        print("Rating must be between 1 and 5.")
                        continue
                    break
                while True:
                    comment = input("Enter your comment: ").strip()
                    if comment:
                        break
                    print("❌ Comment cannot be empty.")

                # Insert the review WITH reviewer_name
                c.execute("""
                INSERT INTO reviews (business_id, reviewer_name, rating, comment)
                VALUES (?, ?, ?, ?)
                """, (business_id, reviewer_name, rating, comment))
                # commit the review
                conn.commit()
                #  Update avg_rating in the businesses table
                avg_rating = get_avg_rating(business_id)
                c.execute("UPDATE businesses SET avg_rating = ? WHERE id = ?",
                          (avg_rating, business_id))

                # Commit the avg_rating update
                conn.commit()
                print("✅ Thank you, {}! Your review has been added.".format(
                    reviewer_name))

            except ValueError:
                print(f"❌ Invalid input")
        else:
            print("ℹ️ Review cancelled.")
    else:
        print("❌- No matching business found.")

    conn.close()


def get_avg_rating(business_id):
    conn = sqlite3.connect("local_connect.db")
    c = conn.cursor()
    c.execute("SELECT AVG(rating) FROM reviews WHERE business_id = ?",
              (business_id,))
    result = c.fetchone()[0]
    conn.close()
    return round(result, 1) if result else "No Ratings yet"


