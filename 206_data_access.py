###### INSTRUCTIONS ###### 

# An outline for preparing your final project assignment is in this file.

# Below, throughout this file, you should put comments that explain exactly what you should do for each step of your project. You should specify variable names and processes to use. For example, "Use dictionary accumulation with the list you just created to create a dictionary called tag_counts, where the keys represent tags on flickr photos and the values represent frequency of times those tags occur in the list."

# You can use second person ("You should...") or first person ("I will...") or whatever is comfortable for you, as long as you are clear about what should be done.

# Some parts of the code should already be filled in when you turn this in:
# - At least 1 function which gets and caches data from 1 of your data sources, and an invocation of each of those functions to show that they work 
# - Tests at the end of your file that accord with those instructions (will test that you completed those instructions correctly!)
# - Code that creates a database file and tables as your project plan explains, such that your program can be run over and over again without error and without duplicate rows in your tables.
# - At least enough code to load data into 1 of your dtabase tables (this should accord with your instructions/tests)

######### END INSTRUCTIONS #########



# Put all import statements you need here.
import unittest
import itertools
import collections
import tweepy
import twitter_info 
import json
import sqlite3
import requests

# Begin filling in instructions....

#setting up twitter info  
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#setting up twitter authentification 
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

#creating cache file
CACHE_FNAME = "final_project.json"

#setting up cache info 
try:
	cache_file = open(CACHE_FNAME,'r')
	cache_contents = cache_file.read()
	cache_file.close()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}
'''

__________________________-BEGIN INSTRUCTIONS-________________________________________ 
def class get_tweepy_info: 
	def function get_user_tl and make request to api.user_timeline(handle) 

	def function get_followers_user and make request to api.followers(handle)
	(in future class define function to get descriptions of users)

	def function exists_friendship and make request to API.exists_friendship(handlea, handleb)

	In those functions, make request to api, put that into a cache dictionary.
	Open the cache file, put the dictionary value into the cache file, write it, dump, return the api information. 

	invoke get_user_tl into get_fox_tl and get_nyt_tl and get_wsj_tl with handles "nytimes", "foxnews", and "wsj" respectively 
	invoke get_follower_user into get_followers_wsj, get_followers_fox, and get_followers_nyt with handles "nytimes", "foxnews", and "wsj" respectively
	invoke exists_friendship into friendship_wsj_nyt, friendship_nyt_fox, friendship_fox_wsj with respective handles

def class user_databases: 

	'''
	#code for creation of final_project database and creating fox_followers table
def get_user_tl(handle):
	twitter_results = api.user_timeline(handle)
	CACHE_DICTION[handle] = twitter_results
	f = open(CACHE_FNAME, 'w')
	f.write(json.dumps(CACHE_DICTION))
	f.close()
	return twitter_results

get_wsj_tl = get_user_tl("wsj")


conn = sqlite3.connect('final_project.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS tracks')
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'fox_followers (screen_name TEXT PRIMARY KEY, '
table_spec += 'description TEXT, num_fols INTEGER)'
cur.execute(table_spec)

	#creating wsj_followers table
cur.execute('DROP TABLE IF EXISTS tracks')
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'wsj_followers (screen_name TEXT PRIMARY KEY, '
table_spec += 'description TEXT, num_fols INTEGER)'
cur.execute(table_spec)

	#creating nyimes_followers table
cur.execute('DROP TABLE IF EXISTS tracks')
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'nytimes_followers (screen_name TEXT PRIMARY KEY, '
table_spec += 'description TEXT, num_fols INTEGER)'
cur.execute(table_spec)

	#creating wsj_tl table
cur.execute('DROP TABLE IF EXISTS tracks')
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'wsj_tl (user_id INTEGER PRIMARY KEY, '
table_spec += 'screen_name TEXT, tweets TEXT, retweets INTEGER)'
cur.execute(table_spec)

	#creating fox_tl table
cur.execute('DROP TABLE IF EXISTS tracks')
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'fox_tl (user_id INTEGER PRIMARY KEY, '
table_spec += 'screen_name TEXT, tweets TEXT, retweets INTEGER)'
cur.execute(table_spec)

	#creating nyt_tl table
cur.execute('DROP TABLE IF EXISTS tracks')
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'nyt_tl (user_id INTEGER PRIMARY KEY, '
table_spec += 'screen_name TEXT, tweets TEXT, retweets INTEGER)'
cur.execute(table_spec)

	#loading data into wsj_tl table. NOTE: I haven't coded get_wsj_tl yet, but it will contain the invocation of the api request for the home timeline info for wsj, as stated previously in my directions
wsj_tl_list = []
for tweet in wsj_tl_list:
	wsj_tl_id = get_wsj_tl["id_str"]
	wsj_screenname = get_wsj_tl['screen_name']
	wsj_description = get_wsj_tl["text"]
	tuples = (wsj_tl_id, wsj_screenname, wsj_description)
	wsj_tl_list.append(tuples)
statement = 'INSERT OR IGNORE INTO Users VALUES (?, ?, ?)'
for t in wsj_tl_list: 
	cur.execute(statement, t)
conn.commit()
conn.close()
'''
	connect to database, establish cursor, drop if exists and create it not, create database "Final_Project" with tables "fox_followers", "wsj_followers", and "nytimes_followers". 
	In each of those tables, include columns screen_name, description, num_fols


	create tables wsj_tl, nyt_tl, fox_tl with columns user_id, screen_name, tweets, retweets !!!!!!!!!!!!!check on project 3 file if columns are all possible

	create table friendships with columns wsj_nyt, nyt_fox, and fox_wsj 
	execute all tables

	insert tweet info into all database tables 

	query 1 = select all from fox_followers inner join with wsj_followers and nytimes_followers 
	execute query1 with the cursor, then fetchall 

	query2 = select retweets from wsj_tl inner join with nyt_tl and fox_tl 
	execute query2 with the cursor, then fetchall

	query 3 = select tweets from wasj_tl inner join with nyt_tl and fox_tl 
	execute query3 with the cursor, then fetchall
	
	query4 = select all from wsj_nyt inner join from nyt_fox and fox_wsj 
	execute query4 with the cursor, then fetchall

	for a few queries, fetch the query into a list of strings using list comprehension

	finally, use data to create a debrief on the analysis, comparing the three publication's political bias through content of tweets, follower's descriptions (if applicable), and friendships between the respective twitter accounts. 

	__________________________-FINISH INSTRUCTIONS-________________________________________ 
	
'''


# Put your tests here, with any edits you now need from when you turned them in with your project plan.
class Tests(unittest.TestCase):
	def firsttest(self):
		self.assertEqual(type(nyt_tweets),type([]))
	def secondtest(self):
		self.assertEqual(type(get_user_tweets("nytimes")[1]),type({"hi":"bye"}))
	def thirdtest(self):
		cache_test = open("final_project.json","r")
		cache_str = cache_test.read()
		cache_test.close()
		obj = json.loads(cache_str)
		self.assertEqual(type(obj),type({"hi":"bye"}))
	def fourthtest(self):	
		cache_test = open("final_project.json","r").read()
		self.assertTrue("nytimes" in cache_test)
	def fifthtest(self):
		twitter_test = get_user_tweets("nytimes")
		self.assertEqual(type(twitter_test),type(["string",3]))
	def seventhtest(self):
		conn = sqlite3.connect('final_project.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM fox_followers');
		result = cur.fetchall()
		self.assertTrue(len(result[0])==4,"Testing that there are 4 columns in the fox_followers database table")
		conn.close()
	def eigthtest(self):
		conn = sqlite3.connect('final_project.db')
		cur = conn.cursor()
		cur.execute('SELECT nytimes FROM wsj_tl');
		result = cur.fetchall()
		self.assertTrue(len(result)<20,"Testing that there are fewer than 20 retweets in the nytimes column in the wsj_tl table")
		conn.close()

if __name__ == "__main__":
	unittest.main(verbosity=2)

# Remember to invoke your tests so they will run! (Recommend using the verbosity=2 argument.)