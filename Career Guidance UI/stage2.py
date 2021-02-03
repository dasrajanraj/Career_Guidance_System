from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import time
import tweepy
import csv
import data


consumer_key = '3twKJ34s9NWj2kGV8WCyi5gCe'
consumer_secret = 't3ZJbDfvOYEwi2ioX7O4D8S2Z8xNBGuKqIgLlQrm1gcki5RZon'
access_token = '1222580048634343424-K9GQ0zVkfwQ31RnDHZWafUPgBl3Row'
access_token_secret = '71XSMKZzUNzC6x9NNc0xJmGpYdQ7lprLNnDznXUttGnW1'



def Occupation_count(id_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

    ids = []
    page_count = 0
    for page in tweepy.Cursor(api.friends_ids, id=id_name, count=30).pages():
        page_count += 1
        print ('Getting page {} for friends ids'.format(page_count))
        ids.extend(page)
        if page_count==2:
            break
    print(ids)
    ids=str(ids)
    ids=ids[1:-1]
    print(ids) 


    # TAKE IDs AND CONVERT TO HANDLES COMMA SEPARATED
     

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
     
    # SET OBJECT AND AUTHENTICATE
    api = tweepy.API(auth)
     
    # Prompt for usernames
    print('Format input like this userid1,userid2,userid3')
    print('Eg. Provide a comma separated list that looks like: 92454545,555787894,65656478')
     
    myIds = ids
     
    #Check for valid input
    if myIds:
        # Clear the input, prepare for lookup
        myIds = myIds.replace(' ','')
        myIds = myIds.split(',')
        # Set a new list object
        myHandleList = []
        i = 0
        # Loop trough the list of usernames
        for idnumber in myIds:
            u = api.get_user(myIds[i])#Tweepy model class instance. This will 
            #contain the data returned from Twitter which we can then use inside our application. 
            uid = u.screen_name
            myHandleList.append(uid)
            i = i+1
            if i==30:
                break
        # Print the lists
        print('Twitter-Ids',myIds)
        print('\n')
        print('Usernames',myHandleList)
    #        #set a filename based on current time
    #    csvfilename = "csvoutput.csv"
    #    print('We also outputted a CSV-file named '+csvfilename+' to your file parent directory')
    #    with open(csvfilename, 'w') as myfile:
    #        wr = csv.writer(myfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #        wr.writerow(['username','twitter-id'])
    #        j = 0
    #        for handle in myHandleList:
    #            writeline = myHandleList[j],myIds[j]
    #            wr.writerow(writeline)
    #            j = j+1
    else:
        print('The input was empty')

    names=["ImRo45","mVkohli","ImRaina","imjadeja","ImZaheer","RobbieSavage8","themichaelowen","starstryder","TeachtoLead"]
    '''
    for name in names:
        myHandleList.append(name)
    '''
    total=data.main(myHandleList)
    return total

name=input("Enter the twitter ID!")
count_occ=Occupation_count(name)
print(count_occ)

# =============================================================================
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# auth_api = API(auth)
# account_list = myHandleList
# if len(account_list) > 0:
#   for target in account_list:
#     print("Getting data for " + target)
#     item = auth_api.get_user(target)
#     for friend in tweepy.Cursor(auth_api.friends).items():
#         # Process the friend here
#         print(process_friend(friend))
#     print("name: " + item.name)
#     print("screen_name: " + item.screen_name)
#     print("description: " + item.description)
#     
# =============================================================================
    
