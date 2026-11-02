#!/usr/bin/python3
"""Returns the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return subscriber count, or 0 if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get("data").get("subscribers")
