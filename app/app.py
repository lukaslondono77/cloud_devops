from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to RDS
def get_db_connection():
    conn = psycopg2.connect(
        host="your-rds-endpoint",
        database="your-db",
        user="your-user",
        password="your-password"
    )
    return conn

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks;')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
