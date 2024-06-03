import mysql.connector

# Database connection configuration
config = {
    'user': 'root',
    'password': '123456',
    'host': '127.0.0.1',
    'database': 'new'
}

# Establishing the connection
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Create a table
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    )
    """)
    conn.commit()

# Insert a record
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()

# Read records
def read_users():
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

# Update a record
def update_user(user_id, name, age):
    cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, user_id))
    conn.commit()

# Delete a record
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()

# Usage
create_table()          # Create the table if it doesn't exist
create_user('Alice', 30)  # Insert a new user
create_user('Bob', 25)    # Insert another user
read_users()            # Read and print all users
update_user(1, 'Alice', 31)  # Update user with id 1
delete_user(2)          # Delete user with id 2
read_users()            # Read and print all users again

# Closing the connection
cursor.close()
conn.close()
