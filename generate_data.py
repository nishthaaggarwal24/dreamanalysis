import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

TOTAL_DREAMS = 12845

def generate_dreams():
    print("Generating enriched dataset for Dream Intelligence Platform V2...")
    
    dream_samples = [
        {
            "text": "I was flying over a vast blue ocean and felt extremely happy and free.",
            "title": "Flying Over Glowing Ocean",
            "symbols": ["flying", "ocean", "water", "sky"],
            "activity": "Flying",
            "cluster_id": 3,
            "cluster_name": "Flight & Escape",
            "anxiety": "Identity Transformation",
            "base_emotion": "Joy"
        },
        {
            "text": "A monster was chasing me through a dark forest. I was terrified and running as fast as I could.",
            "title": "Chased Through Dark Forest",
            "symbols": ["monster", "forest", "chased", "running", "shadow"],
            "activity": "Running",
            "cluster_id": 0,
            "cluster_name": "Performance Anxiety",
            "anxiety": "Loss of Control",
            "base_emotion": "Fear"
        },
        {
            "text": "I was sitting in an empty cold room crying because I lost something incredibly important to me.",
            "title": "Empty Room & Lost Object",
            "symbols": ["room", "crying", "lost", "death", "empty"],
            "activity": "Observing",
            "cluster_id": 1,
            "cluster_name": "Existential Transformation",
            "anxiety": "Social Isolation",
            "base_emotion": "Sadness"
        },
        {
            "text": "I found myself in a beautiful garden talking peacefully to an old friend I haven't seen in years.",
            "title": "Garden Reunion with Friend",
            "symbols": ["garden", "family", "partners", "talking", "flowers"],
            "activity": "Talking",
            "cluster_id": 2,
            "cluster_name": "Relational Connection",
            "anxiety": "Relationship Instability",
            "base_emotion": "Joy"
        },
        {
            "text": "I was falling from a tall glass skyscraper and woke up right before hitting the pavement below.",
            "title": "Falling From Glass Skyscraper",
            "symbols": ["falling", "building", "skyscraper", "heights"],
            "activity": "Falling",
            "cluster_id": 3,
            "cluster_name": "Flight & Escape",
            "anxiety": "Loss of Control",
            "base_emotion": "Fear"
        },
        {
            "text": "I was taking an unexpected final exam in a huge hall but realized I hadn't studied or opened the book once.",
            "title": "Unprepared Final Exam",
            "symbols": ["exams", "schools", "test", "classroom"],
            "activity": "Observing",
            "cluster_id": 0,
            "cluster_name": "Performance Anxiety",
            "anxiety": "Academic Pressure",
            "base_emotion": "Fear"
        },
        {
            "text": "My teeth suddenly started crumbling and falling out out of nowhere while I was looking in a mirror.",
            "title": "Unexpected Dental Loss in Mirror",
            "symbols": ["teeth", "falling", "mirror", "body"],
            "activity": "Observing",
            "cluster_id": 1,
            "cluster_name": "Existential Transformation",
            "anxiety": "Identity Transformation",
            "base_emotion": "Fear"
        },
        {
            "text": "I was driving a vehicle down a steep winding mountain path but the brakes completely stopped working.",
            "title": "Vehicular Brake Failure on Mountain",
            "symbols": ["trains", "car", "brakes", "mountain", "speed"],
            "activity": "Running",
            "cluster_id": 0,
            "cluster_name": "Performance Anxiety",
            "anxiety": "Career Uncertainty",
            "base_emotion": "Fear"
        },
        {
            "text": "I met my favorite artist at an intimate coffee shop and we had a deep philosophical conversation.",
            "title": "Celebrity Coffee Shop Dialogue",
            "symbols": ["coffee", "talking", "celebrity", "friend"],
            "activity": "Talking",
            "cluster_id": 2,
            "cluster_name": "Relational Connection",
            "anxiety": "Social Isolation",
            "base_emotion": "Surprise"
        },
        {
            "text": "I was desperately late for an critical career presentation and kept getting lost in endless maze-like corridors.",
            "title": "Lost in Maze Before Presentation",
            "symbols": ["exam", "schools", "maze", "late", "corridors"],
            "activity": "Running",
            "cluster_id": 0,
            "cluster_name": "Performance Anxiety",
            "anxiety": "Career Uncertainty",
            "base_emotion": "Anger"
        }
    ]
    
    seasons = ['Winter', 'Spring', 'Summer', 'Fall']
    emotions_pool = ['Joy', 'Fear', 'Sadness', 'Anger', 'Surprise', 'Neutral']
    
    start_date = datetime(2025, 8, 1)
    end_date = datetime(2026, 8, 15)
    total_days = (end_date - start_date).days
    
    data = []
    
    # Generate dates and sort them
    random_dates = [start_date + timedelta(days=random.randint(0, total_days), hours=random.randint(0, 23)) for _ in range(TOTAL_DREAMS)]
    random_dates.sort()
    
    for i in range(TOTAL_DREAMS):
        sample = random.choice(dream_samples)
        dream_text = sample["text"]
        title = sample["title"]
        
        # Word count variation
        word_count = len(dream_text.split()) + random.randint(-3, 8)
        
        # Emotion & sentiment setup
        if random.random() < 0.7:
            emotion = sample["base_emotion"]
        else:
            emotion = random.choice(emotions_pool)
            
        if emotion in ['Joy', 'Surprise']:
            sentiment = 'Positive'
            sentiment_score = round(random.uniform(0.4, 0.98), 2)
        elif emotion in ['Fear', 'Sadness', 'Anger']:
            sentiment = 'Negative'
            sentiment_score = round(random.uniform(-0.95, -0.15), 2)
        else:
            sentiment = 'Neutral'
            sentiment_score = round(random.uniform(-0.1, 0.3), 2)
            
        season = random.choice(seasons)
        activity = sample["activity"]
        cluster = sample["cluster_id"]
        cluster_name = sample["cluster_name"]
        anxiety_category = sample["anxiety"]
        symbols_str = ", ".join(sample["symbols"])
        lucid = 'Yes' if random.random() > 0.82 else 'No'
        date_str = random_dates[i].strftime("%Y-%m-%d")
        
        data.append([
            dream_text, title, sentiment, sentiment_score, emotion,
            word_count, season, activity, cluster, cluster_name,
            lucid, date_str, symbols_str, anxiety_category
        ])
        
    cols = [
        'Dream', 'Title', 'Sentiment', 'Sentiment_Score', 'Emotion',
        'Word_Count', 'Season', 'Dominant_Activity', 'Cluster', 'Cluster_Name',
        'Lucid', 'Date', 'Symbols', 'Anxiety_Category'
    ]
    
    df = pd.DataFrame(data, columns=cols)
    
    output_path = os.path.join(os.path.dirname(__file__), 'dreams_with_clusters.csv')
    df.to_csv(output_path, index=False)
    
    # Also save as datamin_dreams.csv for backward compatibility
    legacy_path = os.path.join(os.path.dirname(__file__), 'datamin_dreams.csv')
    df.to_csv(legacy_path, index=False)
    
    print(f"Dataset saved to {output_path} ({len(df)} rows)")

if __name__ == "__main__":
    generate_dreams()
