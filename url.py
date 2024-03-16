'''''
import re
url = input("Enter url : ")
x = re.search('https://', url)
y = re.search('www.', url)
z = re.search('.com', url)
if x and y and z:
    print('Valid')
else:
    print('Invalid')




''''''


''
import re

email = input('Enter emailid : ')
x = re.search('.com$',email)
y = re.search('@',email)
if x and y:
     print('Valid')
else:
     print('Invalid')

'''




import re
no = input('Enter your number : ')
x = re.search('\d{10}',no)
y = re.search('^8' or '^7' or '^9',no)
if x and y:
     print('Valid')
else:
    print('Invalid')

