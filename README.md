# Sentiment Analysis Web Application

This project is a simple web application that classifies text as positive, negative, or neutral using a pre-trained BERT model.

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Enter text in the text box and click "Analyze" to see the sentiment and confidence score.

## Files

- `app.py`: The main Flask application.
- `model.py`: The module for loading the pre-trained model and performing predictions.
- `templates/index.html`: The HTML template for the web interface.
- `static/style.css`: The CSS file for styling the web interface.
- `requirements.txt`: The list of dependencies.
- `README.md`: The project documentation.

## License

This project is licensed under the MIT License.
