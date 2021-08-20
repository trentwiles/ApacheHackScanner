from apachelogs import LogParser
import ipaddress
import sys
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def report(addy):
   url = 'https://api.abuseipdb.com/api/v2/report'
   params = {
      'ip': addy,
      'categories':'14',
      'comment':'Wordpress Scan/Hack'
   }
   
   #key = config["api"]
   
   headers = {
     'Accept': 'application/json',
     'Key': os.getenv("api")
   }
   response = requests.request(method='POST', url=url, headers=headers, params=params)

parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
f = open('/var/log/' + sys.argv[1] + '/access.log', 'r')
a = f.readlines()
for line in a:
    entry = parser.parse(line)
    ip = entry.remote_host
    if 'wp-login' in entry.directives['%r']:
       v = ipaddress.ip_address(ip)
       print(ip + " " + entry.directives['%r'] + " IPv" + str(v.version))
       if sys.argv[2] == "true":
          report(ip)
    elif 'admin/' in entry.directives['%r']:
       v = ipaddress.ip_address(ip)
       print(ip + " " + entry.directives['%r'] + " IPv" + str(v.version))
       if sys.argv[2] == "true":
          report(ip)
    elif 'xmlrpc' in entry.directives['%r']:
       v = ipaddress.ip_address(ip)
       print(ip + " " + entry.directives['%r'] + " IPv" + str(v.version))
       if sys.argv[2] == "true":
          report(ip)
