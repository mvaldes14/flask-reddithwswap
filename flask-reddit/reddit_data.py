import praw
from .config import reddit_password, reddit_username, client_id, client_secret
import re

# Country POSTS
COUNTRY_CODE = "[US]"

# Reddit Functions
def bot_login():
    reddit = praw.Reddit(
        username=reddit_username,
        password=reddit_password,
        client_id=client_id,
        client_secret=client_secret,
        user_agent="HWSearch App v1.0",
    )
    return reddit


def get_from_reddit(item):
    results = {}
    reddit = bot_login()
    reddit_posts = reddit.subreddit("hardwareswap").search(
        item, sort="new", time_filter="week"
    )
    for item in reddit_posts:
        if item.link_flair_text is "Closed":
            continue
        location = re.findall("^\[US\w\s?\-?\w+\]", item.title)
        results[item.title] = {
            "location": str(location).strip("[]").strip("'").strip("[]"),
            "type": item.link_flair_text,
            "text": item.selftext,
            "url": item.url,
        }
    return results
