# Edge AI based perasonal safety system and threat prevention
A real-time Edge AI-personal safety system that detects threats using live video, generates alerts, and visualizes incident locations on an interactive map.

---

## 📌 Project Overview

This project aims to enhance personal safety by using Artificial Intelligence and real-time monitoring. The system captures live video, detects suspicious activities, stores alerts in a database, and displays them on a dashboard along with location tracking.

---

## 🚀 Features

- 🎥 Live video streaming using OpenCV
- 🤖 Real-time threat detection (AI/ML based)
- 🚨 Automatic alert generation
- 🗺️ Live threat location visualization using Leaflet + OpenStreetMap
- 📊 Dashboard for monitoring alerts
- 🔄 Auto-refreshing system (real-time updates)
- 🧑‍🤝‍🧑 Members page for project details

---

## 🛠️ Technologies Used

- Python  
- Flask  
- OpenCV  
- Machine Learning (Scikit-learn / TensorFlow / Keras)  
- MySQL / SQLite  
- HTML, CSS, JavaScript  
- Leaflet.js  
- OpenStreetMap  

---

## 🧠 System Architecture


Camera → Edge AI Detection → Flask Backend → Database → Dashboard + Map

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d585e567-08d9-41c9-acc6-6acf63d44b0b" />



---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/navjot6/Edge-AI-based-personal-safety-system-and-threat-prevention.git
cd Edge-AI-based-personal-safety-system-and-threat-prevention
2️⃣ Install dependencies
pip install flask opencv-python numpy
3️⃣ Setup Database

Create database and tables:

CREATE DATABASE personal_safety;
USE personal_safety;

CREATE TABLE alert (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
4️⃣ Run the application
python app.py
5️⃣ Open in browser
http://127.0.0.1:5000/
📊 Project Structure
├── app.py
├── detection.py
├── database.py
├── templates/
│   ├── dashboard.html
│   ├── combined.html
│   ├── members.html
├── static/
├── README.md
🔄 How It Works
Camera captures live video
AI model processes frames
Threat is detected
Alert is stored in database
Data is sent to frontend
Dashboard displays alerts
Map shows threat location 📍
🗺️ Map Integration
Implemented using Leaflet.js
Uses OpenStreetMap (free, no API key required)
Displays real-time alert locations
Auto-refresh every 5 seconds
📸 Screenshots

(Add your project screenshots here)

🎯 Advantages
Real-time monitoring
Low cost (no paid APIs)
Easy to deploy
Scalable system
🔮 Future Scope
📍 Live GPS tracking
📱 SMS alerts using Twilio
📊 Heatmap for crime analysis
📲 Mobile application
🤖 Advanced AI models
👩‍💻 Author

Navjot Kaur
BCA Graduate | Aspiring ML Engineer

📜 License

This project is for educational purposes.
