# Lab 2 - Log file analysis

## Background

Let’s imagine that you have an Apache web server running in production, and you would like to analyze the access logs of the web server and gather some usage statistics; things like user activity, most popular browsers, popular URLs, etc. Your task is to write a Python script that will read an example log file, and produce the stats outlined below.

## Format of the log

Each line in the log file is equal to one visit, or hit. The log is a tab-delimited file with 6 columns of data. It will be necessary to extract data from a specific column and break it down further. The columns in the log file are in the order below, and contain the following data: 
 
1. IP address of the visitor.
2. Username of the visitor
3. Date and time the user visited.
4. The access method, resource, and protocol used.
5. URL accessed by the user.
6. The ‘User Agent’ string containing browser and other system information from the user.

Downoad the zipped log file here: [example.log](../resources/example.log.zip?raw=true)

## Requirments

At a minimum, write a script that will calculate and output the following:

1. Date range of the log. This would be the first (oldest) and last (newest) date in the file.
2. Total number of hits. 1 hit = 1 line
3. Total number of unique visitors. A unique visitor = a unique IP address.
4. Top 10 users, and the number of times each visited.
5. Top 10 visited URLs, and the number of times each was visited.
6. Number of visitors using any version of Internet Explorer
  - break down by version if you like
7. Number of people using any version of Firefox
  - break down by version if you like

## Example output

```
Access log for date’s XX/May/20xx to xx/May/20xx 

Total # of hits: 999999 
Total # of unique visitors: 999 

Top 5 Users:
   9999 user116
   9999 user0
   9999 user54
   9999 user177
   9999 user56

Top 5 most vistited URL's:
 100000 http://www.example.com/index.html
  60000 http://www.example.com/index.html?HomeRefreshInterval=120
   7000 http://www.example.com/NoAuth/RichText/editor/fckeditor.html
   5000 http://www.example.com/index.html?HomeRefreshInterval=300
   4000 http://www.example.com/index.html?HomeRefreshInterval=600 

Browser Statistics:
 100000 MSIE 6.0
 100000 MSIE 7.0
  10000 MSIE 8.0 
   2000 Firefox/3.6.3
   1000 Firefox/3.5.9
   1000 Firefox/3.6.3
   1000 Firefox/3.0.19
   1000 Other Browsers
```
