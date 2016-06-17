# Lab 3 - Calling REST Services

## Background

Let’s imagine that you still have the same Apache web server from lab2 - still running in production. You have been alerted to some suspisious activity, and suspect that system accounts are being attacked. Your task is to write a Python script that will read an example auth log file, look for failed login attempts, and leverage a free RESTful web-service to Geo-locate the IP the login attempt came from.

## Format of the log

The log file you will be using is a generic Linux auth.log file, and the lines you are looking for look something like this:

```
Apr 13 20:11:18 homer sshd[2910]: Failed password for root from 61.174.51.211 port 1826 ssh2
```

Downoad the zipped log file here: [auth.log](../resources/auth.log.zip?raw=true)

## Requirements

1. Download the auth.log.zip file above, and upzip. You can unzip manually or from within your script
1. Find each failed login attempt in the file
2. Record the source IP address for each attempt, and the number of attempts from each IP
3. Lookup each IP via [freegeoip.net](http://freegeoip.net), and record the following for each IP:
  - Country
  - City
  - Latitude
  - Longitude
4. Output a table-like structure that shows the data for each IP

## Example output

```
             IP         Country            City        Latitude       Longitude           Count 
--------------------------------------------------------------------------------------------------------------
 116.10.191.220           China         Nanning         22.8167        108.3167             223 
 116.10.191.226           China         Nanning         22.8167        108.3167              33 
 58.254.132.132           China       Guangzhou         23.1167          113.25              38 

... ETC ...
```

## Tips

- Try using the builtin [__urllib2__](https://docs.python.org/2/library/urllib2.html) module.
- The [__requests__](http://docs.python-requests.org/en/master/) module is a very popular 3rd party option that abstracts away the complexities you may have with __urllib2__
