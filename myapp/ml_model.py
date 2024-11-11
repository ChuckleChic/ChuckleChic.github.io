from textblob import TextBlob

# Analyze the sentiment of the diary entry
def analyze_sentiment(content):
    analysis = TextBlob(content)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

# Generate content suggestions based on sentiment
def generate_suggestions(sentiment):
    suggestions = {
        "positive": ["Keep up the positive mindset!", "Check out this motivational quote."],
        "neutral": ["Reflect more on today's events.", "Try adding more details to your entry."],
        "negative": ["Here’s an article on coping strategies.", "Consider listing what you’re grateful for."]
    }
    return suggestions.get(sentiment, [])
