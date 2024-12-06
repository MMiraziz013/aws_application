from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="schedule-db.ch86cum4k2aa.us-east-1.rds.amazonaws.com",
            user="admin",
            password="qiourefsc19fjcsm",
            database="schedule_db"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def fetch_data():
    database = connect_to_database()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM aws_table")
    table_data = cursor.fetchall()
    database.close()

    return render_template('table.html', table_data=table_data)

if __name__ == "__main__":
    app.run(debug=True)