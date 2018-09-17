def get_words(str):
    return str.split()

word_weights = {"Thanks": 1.0, "history": 0.5, "paychecks": 0.8, "taxes": -1.0}

def get_average_word_weight(list_of_words):
    number_of_words = len(list_of_words)
    sum_of_word_weights = 0.0
    for w in list_of_words:
        if w in word_weights:
            sum_of_word_weights += word_weights[w]

    return sum_of_word_weights / number_of_words
tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
words = get_words(tweet_string)
avg_tweet_weight = get_average_word_weight(words)

print ("There weight of the tweet is " + str(avg_tweet_weight))

if avg_tweet_weight > 0:
    print ("What a presidential thing to say! HUGE!")
else:
    print ("Surely you're joking, Mr. Trump! SAD!")