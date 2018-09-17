tweet_string = "Thanks to the history TAX CUTS that I signed into law, you paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!"
tweet_words = tweet_string.split()
number_of_words = len(tweet_words)

number_of_good_words = 0
number_of_bad_words = 0

good_words = ["Thanks", "historic", "paychecks"]
bad_words = ["taxes"]

for w in tweet_words:
    print(w)
    if w in good_words:
        number_of_good_words += 1
    elif w in bad_words:
        number_of_bad_words += 1

print ("There are " + str(number_of_good_words) + " good words in the tweet")
print ("There are " + str(number_of_bad_words) + " bad words in the tweet")

if number_of_good_words > number_of_bad_words:
    print("What a presidential thing to say! HUGE!")
else:
    print("Surely you're joking, Mr. Trump! SAD!")