"""
1.) Date range of the log. This would be the first (oldest) and last (newest) date in the file.
2.) Total number of hits. 1 hit = 1 line
3.) Total number of unique visitors. A unique visitor = a unique IP address.
4.) Top 10 users, and the number of times they visited.
5.) Ten most visited URLs, and the number of time accessed.
6.) Number of visitors using Internet Explorer
7.) Number of people using Firefox
"""

import re
import operator
import zipfile

start_date = None
end_date = None
total_hits = 0
unique_visitors = {}
urls = {}
ie_count = 0
firefox_count = 0


with zipfile.ZipFile('example.log.zip', 'r') as zip_ref:
    with zip_ref.open("example.log") as f:
        for line in f:
            total_hits += 1
            fields = line.split('	')

            if total_hits == 1:
            	start_date = fields[2]

            if fields[1] in unique_visitors:
            	unique_visitors[fields[1]] += 1
            else:
            	unique_visitors[fields[1]] = 1

            if fields[4] in urls:
            	urls[fields[4]] += 1
            else:
            	urls[fields[4]] = 1

            if 'MSIE' in fields[5]:
            	ie_count += 1
            elif 'Firefox' in fields[5]:
            	firefox_count += 1
    	end_date = fields[2]

unique_visitor_counts = sorted(unique_visitors.items(), reverse=True, key=operator.itemgetter(1))
urls_counts = sorted(urls.items(), reverse=True, key=operator.itemgetter(1))

print("Start date: %s" % start_date)
print("End date: %s" % end_date)
print("Hits: %d" % total_hits)
print("Top 10 Users:\n")
for x in unique_visitor_counts[0:9]:
    print("%10s %10s" % (x[0], x[1]))
print("Top 10 URLs:\n")
for x in urls_counts[0:9]:
    print("%110s %10s" % (x[0], x[1]))
print("IE count: %d" % ie_count)
print("Firefox count: %d" % firefox_count)
