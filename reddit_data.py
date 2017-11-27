import praw
import config


# Reddit Functions
def bot_login():
    reddit = praw.Reddit(username=config.reddit_username,
                         password=config.reddit_password,
                         client_id=config.client_id,
                         client_secret=config.client_secret,
                         user_agent="HWSearch App v1.0")
    return reddit


def get_from_reddit(item):
    results = {}
    reddit = bot_login()
    reddit_posts = reddit.subreddit('hardwareswap').search(
        item,
        sort='new',
        time_filter='week')
    for items in reddit_posts:
        if items.link_flair_text == 'Closed':
            continue

        results[items.title] = [{'type': items.link_flair_text},
                                {'text': items.selftext},
                                {'url': items.url}]
    return results
