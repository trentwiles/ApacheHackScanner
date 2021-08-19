from apachelogs import LogParser
import ipaddress

parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
file1 = open('/var/log/apache2/access.log', 'r')
Lines = file1.readlines()
for line in Lines:
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
