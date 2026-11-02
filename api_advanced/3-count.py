#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot titles."""
    if counts is None:
        counts = {}
    words = [w.lower() for w in word_list]
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    params = {"limit": 100, "after": after}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return
    data = res.json().get("data")
    for post in data.get("children"):
        for word in post.get("data").get("title").lower().split():
            if word in words:
                counts[word] = counts.get(word, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)
    totals = {}
    for word, num in counts.items():
        totals[word] = num * words.count(word)
    for word, num in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, num))
