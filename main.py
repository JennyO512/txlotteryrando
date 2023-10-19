from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re
import random
import pandas as pd
import os

app = Flask(__name__)


###########################################################
## THIS IS A WORKING PROJECT TO SCRAPE THE TX LOTTERY WEBSITE, 
# THEN USING THE PYTHON RANDOM LIBRARY GENERATE A PREDICTION FOR THE NEXT LOTTERY DRAWING
###########################################################


def scrape_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load page")
    soup = BeautifulSoup(response.content, 'html.parser')
    td_tags = soup.find_all('td')
    data = [tag.get_text() for tag in td_tags]
    return data

def extract_numbers(data):
    pattern = r'\b\d?\d\s*\-\s*\d{2}\s*\-\s*\d{2}\s*\-\s*\d{2}\s*\-\s*\d{2}\s*\-\s*\d{2}\b'
    matches = re.findall(pattern, ' '.join(data))
    if not matches:
        print("No matches found")
    return matches
"""
def predict_next_numbers(numbers):
    last_digits = [int(n[-2:]) for n in numbers]
    freq = [last_digits.count(i) for i in range(100)]
    prob = [f / len(numbers) for f in freq]
    next_numbers = random.sample(range(1, 53), 6)
    next_numbers = [str(num).zfill(2) for num in next_numbers]
    return " - ".join(next_numbers)
"""

#this was added on 10/19 to do a statistical analysis of the data 
def predict_next_numbers(numbers):
    last_digits = [int(n[-2:]) for n in numbers]
    freq = [last_digits.count(i) for i in range(100)]
    prob = [f / len(numbers) for f in freq]
    next_numbers = pd.Series(range(1, 53)).sample(n=6, weights=prob, replace=False)
    next_numbers = [str(num).zfill(2) for num in next_numbers]
    return " - ".join(next_numbers)

"""
We import the pandas library and the random module.
We replace the line that generates random numbers with a line that uses the sample method of a pandas Series object to generate the next numbers. The sample method takes three arguments:
n: The number of samples to draw.
weights: The probability weights associated with each element of the series. In this case, we use the prob list that we calculated earlier.
replace: Whether to sample with replacement. We set this to False to ensure that we don’t get duplicate numbers.
We convert the resulting series of numbers back to a list of strings and join them together with hyphens.

"""
#this was added on 10/19 to do a statistical analysis of the data 


@app.route('/')
def home():
    url = 'https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/index.html#PastResults'
    data = scrape_website(url)
    numbers = extract_numbers(data)
    return render_template('home.html', numbers=numbers)

@app.route('/predictions')
def predictions():
    url = 'https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/index.html#PastResults'
    data = scrape_website(url)
    numbers = extract_numbers(data)
    predicted_numbers = predict_next_numbers(numbers)
    return render_template('predictions2.html', predicted_numbers=predicted_numbers)

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
