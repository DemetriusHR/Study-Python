import json
import nltk

from nltk.stem.porter import *

stemmer = PorterStemmer()

def get_words(str):
    return nltk.word_tokenize(str)

def load_json(json_file):
	with open(json_file) as f:
		return json.load(f)


def get_average_word_weight(list_of_words):  
    number_of_words = len(list_of_words)
    sum_of_word_weights = 0.0  
    if number_of_words == 0:
        return 0.0
    for w in list_of_words:
        stemmed_word = stemmer.stem(w)
        if stemmed_word in word_weights:
            sum_of_word_weights += word_weights[stemmed_word]
        #else:
           #print ('"' + stemmed_word + '": 0.0,')

    return sum_of_word_weights / number_of_words

def analyse_tweet(tweet_string, word_weights):
    words = get_words(tweet_string)
    avg_tweet_weight = get_average_word_weight(words)
    print ("The weight of the tweet is " + str(avg_tweet_weight))

    if avg_tweet_weight > 0:
        print ("What a presidential thing to say! HUGE!")
    else:
        print ("Surely you're joking, Mr. Trump! SAD!")

tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
word_weights = load_json("word_weights.json")
analyse_tweet(tweet_string, word_weights)