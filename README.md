# 🏡 House Price Prediction API

This is a RESTful API built using **FastAPI** that predicts house prices based on input features such as number of rooms, square footage, age of the house, and location score. The prediction is powered by a simple machine learning model trained using `scikit-learn`.

# 💬 Sentiment Analysis API

A RESTful API built with **FastAPI** that analyzes the sentiment of a given text input (positive, negative, or neutral). The prediction is powered by a logistic regression model trained on simple labeled text data using `scikit-learn`.

## 🛠️ Tech Stack

- **FastAPI** – Modern, fast web framework for APIs
- **Uvicorn** – Lightweight ASGI server
- **Scikit-learn** – Machine learning pipeline
- **Joblib** – Model serialization
- **Pydantic** – Data validation

## 📦 Features

- 📊 Predict sentiment with /api/predict
- ❤️ Health check via /api/
- ⚡ Loads pre-trained ML model at startup
- 🛡️ Data validation using pydantic models

## 🧩 Project Structure

```bash
sentiment-api
 ├── model/
 │   └── sentiment_model.pkl
 ├── schemas/
 │   └── sentiment.py
 ├── scripts/
 │   └── train_model.py
 ├── main.py
 └── requirements.txt
```

## 🧠 Model Details

The model is a `LogisticRegression` pipeline trained with the following components:

- **TfidfVectorizer** – Converts input text into TF-IDF features

- **LogisticRegression** – Classifies input as positive, neutral, or negative

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/melos-simeneh/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Train and Save the Model

```bash
python scripts/train_model.py
```

Or use the provided `model/sentiment_model.pkl` directly.

### 4. Run the API

```bash
uvicorn main:app --reload
```

- [http://127.0.0.1:8000](http://127.0.0.1:8000) – API Root
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – Swagger UI
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) – ReDoc

## 📮 API Endpoints

### ✅ Health Check

```http
GET /api/
```

**Response:**

```json
{
  "message": "Sentiment Analysis API is running."
}
```

### 🎯 Predict Sentiment

```http
POST /api/predict
```

**Request Body:**

```json
{
  "text": "I absolutely love this!"
}
```

**Response:**

```json
{
  "sentiment": "positive"
}
```

## 🐳 Docker Support

### 1. Build the Docker Image

```bash
docker build -t sentiment-api .
```

### 2. Run the Docker Container

```bash
docker run -d -p 8000:8000 sentiment-api
```

This runs the container in detached mode (`-d`) and maps port 8000 on your local machine to port 8000 inside the container. The API will be accessible at [http://localhost:8000](http://localhost:8000).

## ☁️ Deployment Options

You can easily deploy this API using platforms like:

[![Deploy on Railway](https://img.shields.io/badge/Deploy_to-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/new/template?template=https://github.com/melos-simeneh/sentiment-analysis-api)
[![Deploy to Render](https://img.shields.io/badge/Deploy_to-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/deploy?repo=https://github.com/melos-simeneh/sentiment-analysis-api)

## 📬 Contact

Made with 💚 by **MELOS**

For questions or suggestions, open an issue or contact [melos.simeneh@gmail.com](mailto:melos.simeneh@gmail.com).
