################################
# regexes - Regular Expression.
#           a pattern to match on some kind of data or user input. ex email add validate if email address or different
# re - Regular Expression Library
# r" - raw string. pass as in exactly as is
# \w - word character. alpha numeric symbol and underscore

#import re
#email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")
#
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

#if re.search(r".+@.+\.edu", email): \ literal character with r" for raw string
#if re.search(r"^.+@.+$", email): ^ start. $ end
#if re.search(r"^[^@]+@[^@]+\.edu$", email): #[] any chanracter. [^@] excluding the character
#if re.search(r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_]+\.edu$", email):
#if re.search(r"^(\w|\s)+@\w+\.(com | edu | gov | eu)$", email):
#if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
#
#     print("Valid")
# else:
#     print("Invalid")

####################################################
# Reformat the users input into the format we expect

# import re

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

####################
# Another method
# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     # last, first = matches.groups()
#     # name = f"{first} {last}"
#     # last = matches.group(1)
#     # first = matches.group(2)
#     # name = f"{first}{last}"
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")

###########################################################################
# := - walrus operator. if you want to assign something from right to left
#      and want to ask a boolean expression on the same line

# name = input("What's your name? ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")

############################################################
# Extract information to ask question
# prompt users of their URL and extract what is the username

import re
url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/")
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"username: {username}")

# matches = re.search(r"^https?://?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
     print(f"Username:", matches.group(1))
