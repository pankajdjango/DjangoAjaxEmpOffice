from django.test import TestCase
# import sys,date
# # Create your tests here.
# argv = sys.argv
# print('argv',argv)
# if argv:
#     date=argv[0]
#     print("date",date)
# else:
    #  t_date=date.today()
#     print("t_date",t_date)
import hashlib

password = "MD5Online"
db_password = "d49019c7a78cdaac54250ac56d0eda8a"
encode = hashlib.md5(password.encode())
decode = hashlib.md5(password.encode()).hexdigest()



print("encode= ",encode)
print("decode= ",decode)

if (hashlib.md5(password.encode()).hexdigest() == db_password):
   print("Authentication success")
else:
   print("Bad login or password")

import requests

#Initialization
url = "https://www.md5online.org/api.php"
key = "YOUR_API_KEY"
md5 = "d3c8e06e57cc1af7ebdba01427e62bc2"

#Request
result = requests.get(url+"?p="+key+"&h="+md5)
print(result.response)