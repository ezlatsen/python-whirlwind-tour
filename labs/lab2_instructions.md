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

Downoad the zipped log file here: [example.log](../resources/example.log.zip)

## Requirments

At a minimum, write a script that will calculate and output the following:

1. Date range of the log. This would be the first (oldest) and last (newest) date in the file.
2. Total number of hits. 1 hit = 1 line
3. Total number of unique visitors. A unique visitor = a unique IP address.
4. Top 10 users, and the number of times each visited.
5. Top 10 visited URLs, and the number of times each was visited.
6. Number of visitors using any version of Internet Explorer
7. Number of people using any version of Firefox
