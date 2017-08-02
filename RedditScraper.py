import praw

# authorise Reddit API - fill these parameters with your own access details 
reddit = praw.Reddit(client_id="############",
                     client_secret="###########",
                     password="############",
                     username="#############",
                     user_agent="############")

# replace the argument with the name of a subreddit 
subreddit = reddit.subreddit('jokes')


def blonde_jokes_data(timestampfrom, timestampto, date):
    authors = []
    unique_users = 0
    blonde_count = 0
    joke_count = 0
    for submission in subreddit.submissions(stampfrom,stampto):
        sub_author = submission.author
        if sub_author not in authors:
            authors.append(sub_author)
        title = submission.title
        text = submission.selftext
        # the following variable store the entire joke
        joke = submission.title + " " + submission.selftext
        # include any words to be checked for in this list
        wordcheck = ["blonde", "Blonde", "blond", "Blond"]
        if any(x in joke for x in wordcheck):
            blonde_count += 1
            print (blonde_count)
        joke_count += 1

    unique_users = len(authors)

    print (date)
    print ("Joke count = " + str(joke_count))
    print (str(unique_users) + " unique users contributed to this subreddit")
    print (str(blonde_count) + " jokes contained the word \'blonde\'")
    print (100 * float(blonde_count)/float(joke_count))
    
# calls the method - the first two arguments can be replaced with other epoch timestamps to record data for different periods of time
blonde_jokes(1230768000, 1262303999, "2009")
