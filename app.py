from flask import Flask, render_template, request
from model import SentimentAnalyzer

app = Flask(__name__)
sentiment_analyzer = SentimentAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        prediction, confidence = sentiment_analyzer.predict(text)
        # The nlptown/bert-base-multilingual-uncased-sentiment model returns predictions from 0 to 4
        sentiment_labels = ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']
        sentiment = sentiment_labels[prediction]
        return render_template('index.html', text=text, sentiment=sentiment, confidence=confidence)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
