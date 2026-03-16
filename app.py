from flask import Flask, render_template
import threading
from detection import detect_threat
from database import get_db_connection

app = Flask(__name__)

@app.route("/")
def dashboard():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY id DESC")
    alerts = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("dashboard.html", alerts=alerts)

@app.route("/start")
def start_system():
    t = threading.Thread(target=detect_threat)
    t.start()
    return "Monitoring Started"

if __name__ == "__main__":
    app.run(debug=True)
