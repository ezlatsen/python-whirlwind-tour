from urllib2 import Request, urlopen, URLError, HTTPError
import json
import logging
import re

logging.basicConfig()
log = logging.getLogger(__name__)

# http://freegeoip.net
def get_country(ip):
	result = {}
	try:
		url = "http://freegeoip.net/json/%s" % ip
		response = urlopen(url)
		the_page = response.read()
		result = json.loads(the_page)
	except HTTPError as e:
		if e.code == '404':
			log.error('Reached maximum call limit of 10K call per hour')
		else:
			log.error(e.code)
	except URLError as e:
		log.error(e.reason)
	return result 

text_file = open("auth.log")
ips = {}
for line in text_file:
	if "Failed password" in line:
		matches = re.findall(r'from\s(\d+\.\d+\.\d+\.\d+)', line)
		ip = matches[0] if matches else None
		if ip:
			if ip in ips:
				ips[ip] += 1
			else:
				ips[ip] = 1

count = 0
columns = ("IP", "Country", "City", "Latitude", "Longitude", "Count")
print("%15s "*6 % columns)
print('-'*110)
for ip in ips.keys():
    try:
    	data = get_country(ip)
    	if data:
        	print("%15s "*6 % (ip, data['country_name'], data['city'], data['latitude'], data['longitude'], ips[ip]))
        	count += ips[ip]
    except UnicodeDecodeError as e:
        log.error(e)
print("Total number of attack attempts: %s" % count)
