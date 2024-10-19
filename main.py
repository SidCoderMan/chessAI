import os
import berserk
from flask import Flask
import requests
from dotenv import load_dotenv



#****DATA COLLECTION FOR AI****


# Load environment variables from .env file
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
print(os.getenv('API_TOKEN'))
session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

def test_token(token):
    url = "https://lichess.org/api/account"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Token is valid!")
        print(response.json())  # Account details should print here
    else:
        print(f"Error: {response.status_code}")

# Replace 'your_lichess_api_token' with your actual token

test_token(API_TOKEN)

def fetch_lichess_games(username, token, max_games):
    # Lichess API endpoint to get user games
    url = f"https://lichess.org/api/games/user/{username}"
    
    # Headers for authentication
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    # Parameters for the API request (format: pgn, number of games)
    params = {
        'max': max_games,    # Limit number of games
        'pgnInJson': 'true', # Request PGNs in JSON format
        'moves': 'true',     # Include moves in the response
        'pgn': 'true'        # Return PGN (Portable Game Notation)
    }
    
    # Send a GET request to fetch games
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.text  # This will be the PGN of the games
    else:
        print(f"Error: {response.status_code}")
        return None

# Usage

username = "sadisticTushi"

max_games = 5

api_token = API_TOKEN

pgn_data = fetch_lichess_games(username, api_token, max_games)

if pgn_data:
    print(pgn_data)  # You can now use this PGN data for your chess AI