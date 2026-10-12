# Import entire module
import random
import datetime

from anyio import current_time

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

number

choice

today = datetime.datetime.today()

print(today)

current_time = datetime.datetime.now().time()

print(current_time)

import os
current_dir = os.getcwd()
print(current_dir)

import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)



# Web requests
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)