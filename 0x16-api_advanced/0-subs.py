#!/usr/bin/python3
"""script to get suscribers"""
import requests


def number_of_subscribers(subreddit):
    """get subscribers of a given subreddit """

    if subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    r = requests.get(url)

    if r.status_code != 200:
        return 0

    data = r.json()["data"]["subscribers"]
    return (data)
