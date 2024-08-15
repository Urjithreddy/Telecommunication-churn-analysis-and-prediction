def analyze_sentiment_spanish(text):
    """Performs a very basic sentiment analysis on Spanish text."""
    # Skip processing if text is NaN or not a string
    if pd.isnull(text) or not isinstance(text, str):
        return "Cannot determine"
    text = text.lower()  # Convert text to lowercase
    
    # Basic sentiment scoring based on keyword matching
    sentiment_score = 0
    positive_words = ['excelente', 'bueno', 'positivo', 'maravilloso', 'fantástico']
    negative_words = ['malo', 'pobre', 'negativo', 'terrible']
    
    for word in positive_words:
        if word in text:
            sentiment_score += 1
    for word in negative_words:
        if word in text:
            sentiment_score -= 1

    # Determine sentiment category
    if sentiment_score > 0:
        return 1  # Positive
    elif sentiment_score < 0:
        return 0  # Negative
    else:
        return -1  # Neutral or cannot determine

