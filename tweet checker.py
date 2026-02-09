tweet = input("enter your tweet:")
max_chars = 140
char_count = len(tweet)

if len(tweet) < max_chars:
    print(f"Your {char_count} word tweet is valid for twitter")
else:
    print(f"Your {char_count} word tweet is {char_count - max_chars} to long")