#!/usr/bin/python

__author__ = 'james'

import urllib2
from BeautifulSoup import BeautifulSoup
from gi.repository import Notify
import time
from datetime import datetime

def get_ip():
    req = urllib2.Request("http://checkip.dyndns.org/")
    webpage = urllib2.urlopen(req).read()
    webpage_text = (BeautifulSoup(webpage)).find('body').text
    return webpage_text.split("Current IP Address: ")[1]

def notify(ip_address):
    notify_message = "Current ip address: {0}".format(ip_address)
    Notify.init("ip address notification")
    notification = Notify.Notification.new(notify_message)
    notification.show()

def log(ip_address):
    file = open('logs/ip_address', 'a+')
    timestamp = int(time.time())
    file.write("{0}|{1}|{2}\n".format(datetime.fromtimestamp(timestamp), str(timestamp), ip_address))

ip_address = get_ip()
log(ip_address)
notify(ip_address)