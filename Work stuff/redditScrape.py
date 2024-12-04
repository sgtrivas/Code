import requests
import requests.auth
import json
import os

# Reddit API credentials
clientId = "cHke8sgMY95XbEryeQWEkQ"
clientSecret = "JiUsMpGbS5P_IvScNPCX9kqasEBPWQ"
redditUser = "SyrupKey8255"
redditPass = "PA$$word30"
headers = {"User-Agent": "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"}
site1 = "https://www.reddit.com/api/v1/access_token"

# Token request
def tokenRequest(id, secret):
    client_auth = requests.auth.HTTPBasicAuth(id, secret)
    return client_auth

def userData(user, password):
    post_data = {"grant_type": "password", "username": user, "password": password}
    return post_data

def redditResponse(auth1, data1, header1):
    response = requests.post(site1, auth=auth1, data=data1, headers=header1)
    return response.json()

def redditScrape(token, subreddit):
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"
    }
    pageScrape = requests.get(f"https://oauth.reddit.com/r/{subreddit}/top", headers=headers)
    return pageScrape.json()

# Function calls to get the token
clientResponse = tokenRequest(clientId, clientSecret)
userResponse = userData(redditUser, redditPass)
tokenResponse = redditResponse(clientResponse, userResponse, headers)
print("Access Token:", tokenResponse['access_token'])

# Read subreddits from file
with open("subreddits.txt", "r") as file:
    subreddits = [line.strip() for line in file if line.strip()]

# Iterate through each subreddit and save JSON data
for subreddit in subreddits:
    print(f"Scraping subreddit: {subreddit}")
    scraper = redditScrape(tokenResponse['access_token'], subreddit)

    # Set the filename for each subreddit
    filename = os.path.join(os.getcwd(), f"{subreddit}.json")
    print("Saving file to:", filename)

    try:
        # Save JSON data to file
        with open(filename, "w") as f:
            json.dump(scraper, f)
        print(f"Data saved to {filename}")
    except FileNotFoundError as e:
        print("Error: Could not create file:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

print("Scraping complete!")