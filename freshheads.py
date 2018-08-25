import praw
from reddit_credentials import client_id, client_secret, user_agent, username, password

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

multireddit = reddit.multireddit('freshheads', 'freshheads')

print(20*'-')

for submission in multireddit.hot(limit=200):
  fresh = submission.title
  if "FRESH" in fresh.upper():
    print(fresh)

print(20*'-')
