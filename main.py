from apachelogs import LogParser
import ipaddress
import sys

parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
f = open('/var/log/' + sys.argv[1] + '/access.log', 'r')
a = f.readlines()
for line in a:
    entry = parser.parse(line)
    ip = entry.remote_host
    if 'wp-login' in entry.directives['%r']:
       v = ipaddress.ip_address(ip)
       print(ip + " " + entry.directives['%r'] + " IPv" + str(v.version))
    elif 'admin/' in entry.directives['%r']:
       v = ipaddress.ip_address(ip)
       print(ip + " " + entry.directives['%r'] + " IPv" + str(v.version))
    elif 'xmlrpc' in entry.directives['%r']:
       v = ipaddress.ip_address(ip)
       print(ip + " " + entry.directives['%r'] + " IPv" + str(v.version))
