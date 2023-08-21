import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
sia = SentimentIntensityAnalyzer()

# Define some sample response templates
response_templates = {
    'greeting': ['Hello!', 'Hi there!', 'Hey, how can I assist you?'],
    'goodbye': ['Goodbye!', 'Take care!', 'Have a great day!'],
    'thanks': ['You\'re welcome!', 'Glad I could help!', 'No problem!']
}

# Define a function to analyze sentiment
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    sentiment = 'positive' if sentiment_scores['compound'] > 0 else 'negative' if sentiment_scores['compound'] < 0 else 'neutral'
    return sentiment

# Define a function to generate a response
def generate_response(user_input):
    tokens = word_tokenize(user_input)
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
    
    sentiment = analyze_sentiment(user_input)
    if sentiment == 'positive':
        response_type = 'thanks'
    elif sentiment == 'negative':
        response_type = 'goodbye'
    else:
        response_type = 'greeting'
    
    response_candidates = response_templates[response_type]
    response = response_candidates[0]  # Select the first response template for simplicity
    
    return response