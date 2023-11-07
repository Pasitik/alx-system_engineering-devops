#!/usr/bin/python3
"""top 10 redits"""
import requests


def top_ten(subreddit):
    """get top 10 titles of reddits"""

    if subreddit is None:
         print("None")
         return 
    
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    headers = {'User-agent': 'yourbotname'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    children = data['data']['children']
    for child in children:
            print(child['data']['title'])
