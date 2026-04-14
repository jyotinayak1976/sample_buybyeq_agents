from db.connection import Database

def init_db():
    conn = Database.get_instance().get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            restaurant_id TEXT PRIMARY KEY,
            name TEXT,
            type TEXT,
            location TEXT,
            rating REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            restaurant_id TEXT,
            amount REAL
        )
    """)

    cursor.execute("DELETE FROM restaurants")
    cursor.execute("DELETE FROM orders")

    cursor.executemany("INSERT INTO restaurants VALUES (?, ?, ?, ?, ?)", [
        ("001", "Klove", "Fine Dine", "Bangalore", 4.5),
        ("002", "Spice Hub", "Casual Dining", "Dhenkanal", 4.2),
        ("003", "Fat boy", "Casual Dining", "Cuttack", 4.2) 
    ])

    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
        ("O1", "001", 1200),
        ("O2", "001", 800),
        ("O3", "002", 500)
    ])

    conn.commit()
