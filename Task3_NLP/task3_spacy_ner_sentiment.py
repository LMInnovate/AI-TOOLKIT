import spacy

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Sample Amazon reviews
reviews = [
    "I love my new Samsung Galaxy phone. Battery life is amazing!",
    "This Apple Watch is terrible. It stopped working after a week.",
    "The Sony headphones are decent for the price.",
    "I hate this cheap charger, it's useless."
]

def simple_sentiment(text):
    positive_words = ["love", "amazing", "great", "good", "excellent", "decent"]
    negative_words = ["terrible", "stopped", "hate", "useless", "bad", "poor"]

    text_lower = text.lower()
    if any(word in text_lower for word in positive_words):
        return "Positive"
    elif any(word in text_lower for word in negative_words):
        return "Negative"
    else:
        return "Neutral"

for review in reviews:
    doc = nlp(review)
    print(f"\nReview: {review}")
    print("Entities:")
    for ent in doc.ents:
        print(f" - {ent.text} ({ent.label_})")
    
    sentiment = simple_sentiment(review)
    print(f"Sentiment: {sentiment}")
