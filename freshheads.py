import praw
import re
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
  flair = str(submission.link_flair_text)

  if ("[FRESH" in fresh.upper()) or ("[FRESH" in flair):
    pretty = re.sub('(\[FRESH\])|(\[FRESH ALBUM\])|(\[FRESH EP\])|(\[FRESH VIDEO\])|(\[FRESH PERFORMANCE\])|(\[FRESH STREAM\])|(\[FRESH/ORIGINAL\])', '\b', fresh, flags=re.IGNORECASE)
    subName = submission.subreddit.display_name
    score = submission.score

    if subName == "hiphopheads":
      print("HHH: ", pretty, " (", score, ")")
    elif subName == "indieheads":
      print("IND: ", pretty, " (", score, ")")
    else:
      print("POP: ", pretty, " (", score, ")")

print(20*'-')
