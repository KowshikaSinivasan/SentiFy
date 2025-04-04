
# 🎭 SentiFY - ReactJS + ML Sentiment Analysis  

SentiFY is a **ReactJS + Machine Learning** project that predicts whether a comment is **Negative** or **Positive**. It uses a **Bagging SVM Model** with **73% accuracy** for sentiment analysis.  

---

## 🚀 Features  
✅ **Real-time sentiment prediction**  
✅ **ReactJS frontend & Flask backend**  
✅ **Bagging SVM Model with 73% accuracy**  
✅ **Easy deployment**  

---

## 🛠 Tech Stack  

- **Frontend:** React.js  
- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-learn, NumPy, Pickle  
- **Deployment:** GitHub, Netlify (Frontend), Render/GCP (Backend)  

---

## ⚡ Installation  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/KowshikaSinivasan/SentiFY.git
cd SentiFY
```

### 2️⃣ Install Dependencies  

#### 🔹 Backend (Flask)  
```bash
cd backend
pip install -r requirements.txt
```

#### 🔹 Frontend (React)  
```bash
cd frontend
npm install
```

---

## 🎯 Usage  

### Start the Backend Server  
```bash
cd backend
python app.py
```
API runs at: **http://localhost:5000**  

### Start the Frontend  
```bash
cd frontend
npm start
```
Frontend runs at: **http://localhost:3000**  

---

## 📬 API Endpoint  

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/predict` | Sends text input and returns sentiment prediction |

**Example Request:**  
```json
{
  "text": "I love this project!"
}
```

**Example Response:**  
```json
{
  "prediction": "Positive"
}
```

---

## 🚀 Deployment  

### **Backend (Render/GCP)**  
1. Push backend code to GitHub  
2. Deploy using **Render** or **Google Cloud**  
3. Use **Gunicorn** for running Flask app  

### **Frontend (Netlify/Vercel)**  
1. Push frontend code to GitHub  
2. Deploy using **Netlify** or **Vercel**  
3. Set **build command**: `npm run build`  

---

## OUTPUT

![Screenshot 2025-04-04 205652](https://github.com/user-attachments/assets/0ceedf96-bb58-4801-b284-9417c516c876)![Uploading Screenshot 2025-04-04 205652.png…]()



---

## 📜 License  

This project is **open-source** under the MIT License.  

---

This README is **clean, structured, and professional**. Let me know if you need any tweaks! 🚀🔥
