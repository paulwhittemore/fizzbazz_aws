#!/usr/bin/python

# For usage:
# % python load_generator.py --h
# % python load_generator.py --help

import argparse
import time
import urllib2

def read_url(url):
    # url = "http://127.0.0.1:5000/fizzbuzz/{:d}".format(i)
    # print url
    r = urllib2.urlopen(url).read()
    return r

if __name__ == '__main__':

    # Command Line Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Provide hostname of ELB providing FizzBuzz service.")
    parser.add_argument("--maxreq", help="Max number of requests to scale up.", default=2000)
    parser.add_argument("--batchreq", help="Number of requests, per minute, to scale up.", default=500)
    args = parser.parse_args()

    if args.host:
        # Query site
        host = args.host
        print 'host: %s' % host
    else:
        print "Error: require host to continue."
        print "Error: Example: python load_generator.py --host=myhost."
        exit(1)

    max_requests = args.maxreq
    batch_requests = args.batchreq

    delay_sec = 60

    print
    print 'Initial - ELB has two server nodes minimum, and will scale to a maximum of 4 nodes.'

    print
    print 'Scale up -- increase load so that Request Count on ELB is greater than 100 per second.'

    for i in range(1, max_requests):
        url = "http://{:s}:5000/fizzbuzz/{:d}".format(host, i)
        r = read_url(url)
	if ((i % 250) == 0):
            print '%s: %s' % (i, r)
        if (i % batch_requests) == 0:
            time.sleep(delay_sec)

    print
    print 'Scale down -- decrease load so that Request Count on ELB is less than 10 per second.'

    max_requests = 16
    batch_requests = 4
    for i in range(1, max_requests):
        url = "http://{:s}:5000/fizzbuzz/{:d}".format(host, i)
        r = read_url(url)
        print '%s: %s' % (i, r)
        if (i % batch_requests) == 0:
            time.sleep(delay_sec)

