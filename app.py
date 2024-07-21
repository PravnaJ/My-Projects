from flask import Flask, render_template, request
from scraper import extract_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return render_template('index.html', data=None, error="URL is required")

    data = extract_data(url)
    if data:
        return render_template('index.html', data=data, error=None)
    else:
        return render_template('index.html', data=None, error="Failed to retrieve data from the provided URL")

if __name__ == '__main__':
    app.run(debug=True)