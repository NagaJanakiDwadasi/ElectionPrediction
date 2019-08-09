from twitterscraper import query_tweets
import datetime as dt

def queryTweets(user):    
    file = open(user + '_tweets.txt','w')        
    for tweet in query_tweets("#" + user,150000,dt.date(2017, 12, 10),dt.date(2019, 8, 5)):
        tweetText=str(tweet.text)
        tweetText=tweetText.replace(',','')
        tweetText=tweetText.replace('\n',' ')
        file.write(tweet.user + ',' + tweetText+'\n')
    file.close()
if __name__ == '__main__':    
    queryTweets('BernieSanders')
    queryTweets('DonaldTrump')
