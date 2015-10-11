#-*- coding:utf-8 -*-
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
 
 
api = tweepy.API(giris)
 
twit = raw_input(">> ")
api.update_status(status=twit)