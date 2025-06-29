#!/usr/bin/env python3
"""
Script to create the 'alx_book_store' database
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (adjust user/password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # Replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: uncomment to confirm closing
            # print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
