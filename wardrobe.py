#dig wardrobe
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("wardrobe.db")
cursor = conn.cursor()

# Create a table to store clothing items
cursor.execute("""
    CREATE TABLE IF NOT EXISTS wardrobe (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        color TEXT,
        size TEXT
    )
""")
conn.commit()

def add_item():
    name = input("Enter item name: ")
    category = input("Enter category (e.g., shirt, pants, dress): ")
    color = input("Enter color: ")
    size = input("Enter size: ")

    cursor.execute("INSERT INTO wardrobe (name, category, color, size) VALUES (?, ?, ?, ?)",
                   (name, category, color, size))
    conn.commit()
    print("Item added successfully!")

def view_items():
    cursor.execute("SELECT * FROM wardrobe")
    items = cursor.fetchall()
    if items:
        print("\nWardrobe Items:")
        for item in items:
            print(f"ID: {item[0]}, Name: {item[1]}, Category: {item[2]}, Color: {item[3]}, Size: {item[4]}")
    else:
        print("No items in the wardrobe.")

def main():
    while True:
        print("\nDigital Wardrobe Application")
        print("1. Add Item")
        print("2. View Items")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()
    print("Thank you for using the Digital Wardrobe Application!")

if' _name_' == "_main_":
    main()
