from urllib.request import urlopen
from textblob import TextBlob
import datetime as dt
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter
import geocoder
import pandas as pd
URL_INIT = 'https://twitter.com/'

list_of_states=["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

def parse_url(tweet_user):
    url = URL_INIT+ tweet_user.strip('@')
    return url
    
    
def isValidState(location):
    s=""
    for state in list_of_states:
     if(location.find(state) >= 0): 
       return state;     
    return '' 


geolocator = Nominatim(user_agent="cmpe256")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=3)    

def fetchlocation(user):
 file_state_user_tweet = open('state_user_tweet_'+ user+'.txt','w')
 polarityValue=''
 cols=['user','comment']
 data = pd.read_csv(user + "_tweets.txt", names=cols, header=None,engine="python", sep=',' , error_bad_lines=False)

 for ind in data.index:
        try:
            url = parse_url(str(data['user'][ind]))
            response = urlopen(url)
        except:
            print('Failed while fetching user location')
            continue
        html = response.read()
        soup = BeautifulSoup(html, features="lxml")
        try:
         location = soup.find('span','ProfileHeaderCard-locationText').text.strip('\n').strip()
        except:
         continue
        validState=isValidState(str(location)) 
        if len(validState) <= 0:
         if location and (location.find(',')>=0):
            if ',' in location:
                splitted_location = location.split(',')
            else:
                splitted_location = re.split('|;|-|/|°|#', location)
            try:
                if splitted_location:
                    located_location = geocode(splitted_location[0], timeout=100)
                else:
                    located_location = geocode(location, timeout=100)
                if located_location:
                  if(str(located_location).find('USA')>0 or str(located_location).find('America')>0): 
                    validState=isValidState(str(located_location))
            except GeocoderTimedOut as e:
                print("Error: geocode failed on input %s with message %s"%(location, e))

        if(len(validState) > 0):
           file_state_user_tweet.write(validState + ',' + str(data['user'][ind])+ ',' +str(data['comment'][ind]) +'\n')

 file_state_user_tweet.close()
 

if __name__ == '__main__':
     fetchlocation('BernieSanders')
     fetchlocation('DonaldTrump')

