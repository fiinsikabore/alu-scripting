#!/usr/bin/python3
"""Recursively returns a list of all hot post titles of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return list of hot titles, or None if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    params = {"limit": 100, "after": after}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get("data")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
