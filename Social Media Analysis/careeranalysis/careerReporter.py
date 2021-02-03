import tweepy 
import re,string
import csv
from sklearn import metrics
import csv
import pickle 
import joblib
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
from statistics import mode
#FUNCTION TO GET THE Career VALUE BY ANALYSING THE TWEET OR THE TEXT ENTERED IN THE TEXT BOX ALONE
# tf1 = joblib.load('vocab.pkl')
# Tfidf_vect = TfidfVectorizer(max_features = 5000, vocabulary = tf1)
consumer_key = "7LpNzY0vxJLJ6G3urHqWf2aOV"
consumer_secret = "pVTsVgrpFDMWO23ieJeb4Y3Fezs9bLLssk4PeZds4K7VUsaIYR"
access_token = "1224024091943829504-yt4GWoJfJQz18ocgjfg9AfwQE8BaIW"
access_token_secret = "ZRRv9Ch6MVHG6MPKKuPoI4dVPBxD3rVyxaZC0tdYHqVwx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)
Tfidf_vect = joblib.load('vocab.pkl')
NB = joblib.load('nbcareer.pkl')
def getCareerbyTweet(test):
	test = test.lower()
	test = word_tokenize(test)
	tag_map = defaultdict(lambda : wn.NOUN)
	tag_map['J'] = wn.ADJ
	tag_map['V'] = wn.VERB
	tag_map['R'] = wn.ADV
	words=[]
	word_Lemmatized = WordNetLemmatizer()
	for word, tag in pos_tag(test):
		if word not in stopwords.words('english') and word.isalpha():
			word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
			words.append(word_Final)

	words_fit=Tfidf_vect.transform(words)
	answer=NB.predict(words_fit)
	print(answer)
	n=mode(answer)
	if n==1:
		return "random"
	elif n==2:
		return "pilot"
	elif n==3:
		return "architect"
	elif n==4:
		return "photographer"
	elif n==5:
		return "finance"
# FUNCTION TO GET THE Career VALUE BASED ON NUMEROUS TWEETS FROM A TWITTER HANDLE

def getCareerbyId(username):
	alltweets=[]
	try:
		tweets=api.user_timeline(screen_name=username,count=200)#,tweet_mode="extended"
	except tweepy.TweepError:
		print("invalid")
	for tweet in tweets:
		if tweet.lang == "en":
			alltweets.append(tweet.text)
            
	text=[]
	for i in alltweets:
		i=re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", "", i)
		i=re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", "",i)
		text.append(i)
	result=pd.DataFrame(text,columns=['Text'])
	result.to_csv('user.csv',index=False)
	result=pd.read_csv(r"user.csv",encoding='latin-1')
	result['Text'].dropna(inplace=True)# Step - b : Change all the text to lower case. This is required as python interprets 'dog' and 'DOG' differently
	result['Text'] = [entry.lower() for entry in result['Text']]# Step - c : Tokenization : In this each entry in the corpus will be broken into set of words
	result['Text']= [word_tokenize(entry) for entry in result['Text']]# Step - d : Remove Stop words, Non-Numeric and perfom Word Stemming/Lemmenting.# WordNetLemmatizer requires Pos tags to understand if the word is noun or verb or adjective etc. By default it is set to Noun
	tag_map = defaultdict(lambda : wn.NOUN)
	tag_map['J'] = wn.ADJ
	tag_map['V'] = wn.VERB
	tag_map['R'] = wn.ADV
	for index,entry in enumerate(result['Text']):
    # Declaring Empty List to store the words that follow the rules for this step
		Final_words = []
    # Initializing WordNetLemmatizer()
		word_Lemmatized = WordNetLemmatizer()
    # pos_tag function below will provide the 'tag' i.e if the word is Noun(N) or Verb(V) or something else.
		for word, tag in pos_tag(entry):
        # Below condition is to check for Stop words and consider only alphabets
			if word not in stopwords.words('english') and word.isalpha():
				word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
				Final_words.append(word_Final)
    # The final processed set of words for each iteration will be stored in 'text_final'
		result.loc[index,'text_final'] = str(Final_words)
#     print(result['text_final'])
	res_fit=Tfidf_vect.transform(result['text_final'])
#     print(res_fit)
	answer=NB.predict(res_fit)
	print(answer)
	n=mode(answer)
	if n==1:
	    return "random"
	elif n==2:
	    return "pilot"
	elif n==3:
	    return "architect"
	elif n==4:
	    return "photographer"
	elif n==5:
	    return "finance"