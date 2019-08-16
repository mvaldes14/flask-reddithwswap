import praw
import config
import re

# Country POSTS
COUNTRY_CODE = "[US]"

# Reddit Functions
def bot_login():
    reddit = praw.Reddit(
        username=config.reddit_username,
        password=config.reddit_password,
        client_id=config.client_id,
        client_secret=config.client_secret,
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
        if item.link_flair_text is "Closed" or (COUNTRY_CODE in item.link_flair_text):
            continue
        location = re.findall("^\[US\w\s?\-?\w+\]", item.title)
        results[item.title] = {
            "location": str(location).strip("[]").strip("'").strip("[]"),
            "type": item.link_flair_text,
            "text": item.selftext,
            "url": item.url,
        }
    return results
