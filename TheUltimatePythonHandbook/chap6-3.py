# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.
text = "hello this is just a sample text and make a lot of money to grt 50 of!!"
if "buy now" or "subscribe this" or "click this" or "make a lot of money" in text:
    print("spam\n")
else:
    print("not a spam\n")