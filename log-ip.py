#!/usr/bin/python
import subprocess

__author__ = 'james'

import urllib2
from BeautifulSoup import BeautifulSoup
from gi.repository import Notify
import time
from datetime import datetime
import os

def get_ip():
    req = urllib2.Request("http://checkip.dyndns.org/")
    webpage = urllib2.urlopen(req).read()
    webpage_text = (BeautifulSoup(webpage)).find('body').text
    return webpage_text.split("Current IP Address: ")[1]

def notify(ip_address, ssid):
    notify_message = "Current ip address: {0} from {1}".format(ip_address, ssid)
    Notify.init("ip address notification")
    notification = Notify.Notification.new(notify_message)
    notification.show()

def log(ip_address, ssid):
    log_file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs', 'ip_address')
    file = open(log_file_name, 'a+')
    timestamp = int(time.time())
    file.write("{0}|{1}|{2}|{3}\n".format(datetime.fromtimestamp(timestamp), str(timestamp), ip_address, ssid))

def get_ssid():
    return subprocess.check_output(["iwgetid", "-r"]).replace("\n", "");

ip_address = get_ip()
ssid = get_ssid()
log(ip_address, ssid)
notify(ip_address, ssid)