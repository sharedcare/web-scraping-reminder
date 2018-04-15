#!/usr/bin/env python
"""Scrapes the web data from url and reminds user.

This is the main function of web scraping reminder,
all global variables are changable to meet different purposes.
Note: You must not share your password with others.
"""
__author__ = 'Tony(Yizhen) Chen'
__version__ = '0.1.0'
__email__ = 'tony@sharedcare.io'

from __future__ import print_function

from datetime import datetime
from email_server import EmailServer
from web_search import WebSearch
from periodic_task import PeriodicTask

# Define email address you want to send from
from_addr = '<sender-address>'
# Define email address you want to send to
to_addr = '<receiver-address>'
# Define your user id of SMTP server 
# (Mostly, this should be same as your from_addr)
userid = '<user-id>'

# Define your password of SMTP server
psw = '<password>'
# Define time interval between every two requests
# in second. Default is 60 seconds
time_period = 60

# Define your url to search
url = '<url>'
keyword = '<word-to-search>'    # The keyword to match

url_params = {'s': 'basics',
              'submit': 'search'}
# Your SMTP server to send email
SMTP_server = {'address': '<smtp-server>',
               'port': '<smtp-server-port>'}    # <-- integer
# Your message content
email_msg = {'subject': '<subject>', 
             'body': '<body>'}

if __name__ == '__main__':  # Run the remainder

    email_server = EmailServer(from_addr, to_addr, email_msg, SMTP_server, userid, psw)
    web_search = WebSearch(url, url_params, keyword)
    data = web_search.scrape_data()
    text = data.decode('utf-8')
    task = PeriodicTask(interval=time_period, callback=web_search.check_keyword, daemon=False, text=text, email_server=email_server)
    task.run()
    