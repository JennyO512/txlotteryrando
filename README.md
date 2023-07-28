# Python Lottery Prediction Project

This Python project aims to scrape the Texas Lottery website, extract relevant data, and use the Python `random` library to generate a prediction for the next lottery drawing.

## Dependencies

The project uses the following Python libraries:

- `requests`
- `BeautifulSoup`
- `re`
- `random`

## Functions

The project consists of three main functions:

### `scrape_website(url, output_file)`

This function takes a URL and an output file name as arguments. It sends a GET request to the specified URL, parses the HTML content of the page using BeautifulSoup, and extracts the text from all `<td>` tags. The extracted data is then written to the output file.

### `extract_numbers(input_file, output_file)`

This function takes an input file name and an output file name as arguments. It reads the data from the input file, uses a regular expression to find all matches of a specific pattern (representing lottery numbers), and writes the matches to the output file. If no matches are found, it prints an error message.

### `predict_next_numbers(filename)`

This function takes a filename as an argument. It calls the `extract_numbers` function to get the lottery numbers from the file, calculates the frequency of the last two digits of each number, and uses the `random` library to generate a prediction for the next lottery drawing. The predicted numbers are returned as a string.

## Usage

The functions are used in the following order:

1. `scrape_website('https://www.texaslottery.com/export/sites/lottery/Games/Lotto_Texas/index.html#PastResults', 'output.txt')`
2. `extract_numbers('output.txt', 'output2.txt')`
3. `predicted_numbers = predict_next_numbers('output2.txt')`
4. `print('The predicted numbers are:', predicted_numbers)`

The final print statement will output the predicted numbers for the next lottery drawing.

## Note

This project is a work in progress and the prediction method is based on random selection, so the accuracy of the predictions is not guaranteed.

## Home Page | List of Past Results 
![txlotteryscreen1](https://github.com/JennyO512/txlotteryrando/blob/main/txlotteryscreen1.png)

## Predictive Numbers | using python random library, generating the computers next best guess based on the past results list from above ^
![txlotteryscreen2](https://github.com/JennyO512/txlotteryrando/blob/main/txlotteryscreen2.png)


