from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Sample training data
texts = [
    "I love this product!", "This is amazing", "So happy with it",
    "This is okay", "Not bad", "It’s fine",
    "I hate this", "Very disappointed", "Terrible experience"
]
labels = ["positive", "positive", "positive", "neutral", "neutral", "neutral", "negative", "negative", "negative"]

# Create pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

# Train
pipeline.fit(texts, labels)

# Save model
joblib.dump(pipeline, "model/sentiment_model.pkl")
print("Model saved.")
