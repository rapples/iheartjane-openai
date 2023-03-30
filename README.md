<h1>Cannabis Menu Review Script</h1>

This is a Python script that reads from a CSV file of cannabis stores. It queries the online store's api and uses OpenAI to extract information about the cannabis strains and create a review of the cannabis menu.

<h3>Libraries Used </h3>

requests: Used to make HTTP requests to the Algolia API

re: Used to extract relevant data from the Algolia API response

base64: Used to encode data

csv: Used to read the CSV files

io: Used to handle input and output

openai: Used to make requests to the OpenAI API

string: Used to remove punctuation from the input

time: Used to measure the response time of the OpenAI API

concurrent.futures: Used to manage concurrent API requests



 <h3>Usage:</h3>


This is example code. Use of this code is at your own risk.

Get Permission to poll the servers you're connecting to.

Be reasonable about the number and size of your requests.

Openai's model is currently accepts 2000 tokens per transaction.

Clone the repository and navigate to the project directory.

Install the required libraries with pip.

Add a CSV file named flowers3 with the THC value you want to search for.

Add a CSV file named stores2 with the store IDs and addresses.

Run the script with python3 -W ignore ml_thisjane35.py  (>reviews.txt to save to a file)

The script will temporarily generate a text file named ml_jane.txt with the extracted data for each store.

The script will then use the OpenAI API to generate a cannabis menu review for each data file's contents.

The reviews will be printed to the console, usually this would be redirected to a file. 


 <h3>License </h3>
This project is licensed under the terms of the MIT license.
