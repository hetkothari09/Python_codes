import regex as re

url="https://www.google.com"

regex1= re.search("((http|https)://)(www.).*\.[a-z]{1,3}",url)
if regex1:
    print("true")
else:
    print("False")

email="hetkothari@gmail.com"
regex2=re.search("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}", email)
if regex2:
    print("TRUE")
else:
    print("FALSE")


num=9829999999
ess="[0-9]{10}"
regex3=re.search(ess, num)

if regex3:
    print("TRUEEEEEE")
else:
    print("FALSEEEEEE")

