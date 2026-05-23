import os
import sys
import requests
import json
from rich import print as rpint
import time

def ptt(message):
    rpint(f"{message}".encode('utf-16', 'surrogatepass').decode('utf-16'))

def fetch_request(username):
    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url, timeout=10).json()

    with open("response.json", "w") as f:
        json.dump(response, f, indent=2)

    with open("response.json", 'r') as f:
        data = json.load(f)
        return data

def error_message(*messages):
    for message in messages:
        clear_screen()
        print(message)
        time.sleep(1)
    time.sleep(2)
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def all_activity(username):
    data = fetch_request(username)
    
    rpint(f"\tListing all activities for GitHub user: [bold green]{username.upper()}[/bold green]")
    for info in data:
        print("-"*50)
        ptt(info['type'])
    

def main():
    if len(sys.argv) < 2:
        error_message("To use this application, enter the GitHub username of the persons GitHub events you would like to see", "Usage: github-activity.py 'username'")
        
    if len(sys.argv) == 2:
        all_activity(sys.argv[1])

if __name__ == "__main__":
    main()