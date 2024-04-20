
import requests
import dash
import pandas as pd
from dash import Dash, html, dcc

# Replace 'YOUR_RAPIDAPI_KEY' with your actual RapidAPI key
api_key = '29c4f831cfmsh52dc9590010758dp119888jsn6df53e96b996'

# Endpoint and headers for the API request
url = 'https://netflix54.p.rapidapi.com/search/'
headers = {
    'X-RapidAPI-Key': '29c4f831cfmsh52dc9590010758dp119888jsn6df53e96b996',
    'X-RapidAPI-Host': 'netflix54.p.rapidapi.com'
}

# Parameters for the API request
params = {
    'query': 'stranger',
    'offset': '0',
    'limit_titles': '50',
    'limit_suggestions': '20',
    'lang': 'en'
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response into a Python dictionary
    netflix_data = response.json()
    # For the purposes of this example, let's assume 'titles' is a key in the JSON response
    # This will depend on the actual structure of the response you receive
    titles = netflix_data.get('titles', [])
else:
    print(f"Failed to fetch data: {response.status_code}")
    titles = []

# Convert the data into a pandas DataFrame
titles_df = pd.DataFrame(titles)

# Initialize a Dash app
app = Dash(__name__)

# Define the layout of the app using the DataFrame
app.layout = html.Div([
    html.H1('Netflix Search Results for "Stranger"'),
    dcc.Graph(
        id='netflix-titles-bar-chart',
        figure={
            'data': [
                {'x': titles_df['name'], 'y': titles_df['year'], 'type': 'bar', 'name': 'Titles'},
            ],
            'layout': {
                'title': 'Netflix Titles Related to "Stranger" by Year'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
