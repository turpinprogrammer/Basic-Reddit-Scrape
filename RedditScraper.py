import praw

reddit = praw.Reddit(client_id="CGBFvuKHEYGYMA",
                     client_secret="U6GaeSTHdGdKsAQg1rNufIJZcsY",
                     password="F1nalFanta5y",
                     username="benturpin",
                     user_agent="benturpin")

subreddit = reddit.subreddit('jokes')

jan15 = [1420070400, 1422748799, "Jan 2015"]

jan16 = [1451606400, 1454284799, "Jan 2016"]
feb16 = [1454284800, 1456703999, "Feb 2016"]
mar16 = [1456790400, 1459468799, "March 2016"]
apr16 = [1459468800, 1462060799, "April 2016"]
may16 = [1462060800, 1464739199, "May 2016"]
jun16 = [1464739200, 1467331199, "June 2016"]
jul16 = [1467331200, 1470009599, "July 2016"]
aug16 = [1470009600, 1472687999, "August 2016"]
sep16 = [1472688000, 1475279999, "September 2016"]
oct16 = [1475280000, 1477958399, "October 2016"]
nov16 = [1477958400, 1480550399, "November 2016"]
dec16 = [1480550400, 1483228799, "December 2016"]

jan17 = [1483228800, 1485907199, "Jan 2017"]

year2016 = [jan16, feb16, mar16, apr16, may16, jun16, jul16, aug16, sep16, oct16, nov16, dec16]


def blonde_jokes(stampfrom, stampto, date):
    authors = []
    unique_users = 0
    blonde_count = 0
    joke_count = 0
    for submission in subreddit.submissions(stampfrom,stampto):
        subid = submission.id
        sub_author = submission.author
        if sub_author not in authors:
            authors.append(sub_author)
        title = submission.title
        text = submission.selftext
        joke = submission.title + " " + submission.selftext
        if "blonde" in joke or "Blonde" in joke or "blond" in joke or "Blond" in joke:
            blonde_count += 1
            print (blonde_count)
        joke_count += 1

    unique_users = len(authors)

    print (date)
    print ("Joke count = " + str(joke_count))
    print (str(unique_users) + " unique users contributed to this subreddit")
    print (str(blonde_count) + " jokes contained the word \'blonde\'")
    print (100 * float(blonde_count)/float(joke_count))

def muslim_jokes(stampfrom, stampto, date):
    authors = []
    unique_users = 0
    blonde_count = 0
    joke_count = 0
    for submission in subreddit.submissions(stampfrom,stampto):
        subid = submission.id
        sub_author = submission.author
        if sub_author not in authors:
            authors.append(sub_author)
        title = submission.title
        text = submission.selftext
        joke = submission.title + " " + submission.selftext
        if "muslim" in joke or "Muslim" in joke or "Islam" in joke or "islam" in joke:
            blonde_count += 1
            #print (blonde_count)
        joke_count += 1

    unique_users = len(authors)

    print (date)
    print ("Joke count = " + str(joke_count))
    print (str(unique_users) + " unique users contributed to this subreddit")
    print (str(blonde_count) + " jokes contained the words \'muslim\' or \'islam\'")
    print (100 * float(blonde_count)/float(joke_count))

#for month in year2016:
 #   muslim_jokes(*month)
muslim_jokes(1230768000, 1262303999, "2009")
muslim_jokes(1451606400, 1483228799, "2016")
