#!/usr/bin/python3
"""Queries the Reddit API for the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the hot posts of a subreddit and report the result."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    params = {"limit": 10}
    requests.get(url, headers=headers, params=params,
                 allow_redirects=False)
    print("OK", end="")
