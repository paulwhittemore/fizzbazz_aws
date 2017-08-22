#!/usr/bin/python

import time
import urllib2

def read_url(url):
    # url = "http://127.0.0.1:5000/fizzbuzz/{:d}".format(i)
    # print url
    r = urllib2.urlopen(url).read()
    return r

if __name__ == '__main__':

    # Parameters
    host = '127.0.0.1'
    num_tries = 16
    num_per_sec = 4
    delay_sec = 60

    # Query site
    print 'host: %s' % host

    for i in range(1, num_tries):
        url = "http://{:s}:5000/fizzbuzz/{:d}".format(host, i)
        r = read_url(url)
        print '%s: %s' % (i, r)
        if (i % num_per_sec) == 0:
            time.sleep(delay_sec)
