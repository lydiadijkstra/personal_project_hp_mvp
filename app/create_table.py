"""
File to create tables in the Harmonic-Parent-Database
"""
import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()


# Database connection
db_params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}
DATABASE_URL = os.getenv("DATABASE_URL")


# SQL command to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS tips (
    tip_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    child_id INTEGER NOT NULL REFERENCES children(child_id),
    content TEXT NOT NULL,
    problem_type VARCHAR(255),
    send_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


try:
    # Connect to the PostgreSQL database
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            # Execute the CREATE TABLE statement
            cur.execute(create_table_query)
            print("Table 'tips' created successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
