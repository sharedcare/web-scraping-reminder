#!/usr/bin/env python
#title           :web_search.py
#description     :Searches the keyword on website by given url.
#author          :Chen, Yizhen
#date            :Apr. 14, 2018
#version         :0.1.1
#python_version  :3.6.5 
#==============================================================================
from __future__ import print_function

from datetime import datetime
import urllib.request
import urllib.parse
import re


class WebSearch(object):
    """Searches the keyword on website by given url
    
    Attributes:
        url: A string indicates url to search
        params: A dictionary defines the parameters of setting on scraping data
        keyword: A string specifies the word to search for 
    """
    def __init__(self, url, params, keyword):
        """Inits WebSearch class with url, params and keyword"""
        self.url = url
        self.params = params
        self.keyword = keyword

    def scrape_data(self):
        """Scraping html raw data from given url"""
        data = urllib.parse.urlencode(self.params)
        data = data.encode('utf-8')
        req = urllib.request.Request(self.url, data)
        res = urllib.request.urlopen(req)
        return res.read()

    def check_keyword(self, text, email_server):
        """Search word and send email to remind

        This method can be modified to satisfied different
        patterns on searching.
        """
        matchs = re.search(self.keyword, text)
        if matchs:
            print('{}: {} found'.format(str(datetime.now()), self.keyword))
            email_server.send_email()
        else:
            print('{}: {} not found'.format(str(datetime.now()), self.keyword))

