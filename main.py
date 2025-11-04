"""
#typing with nails extension on is sooooo annoying 
"""

import os
import requests
import bs4 
import pypandoc
import re
import argparse
import pyperclip

apiV2_url = "https://www.wattpad.com/apiv2/"
api_V3_url = "https://www.wattpad.com/apiv3/"
error_msg = "ERROR:check the url, for valid id"

def get_chap_id(url):
    search_id = re.compile(r'\d{5,}')
    id_match = search_id.search(url)
    if id_match:
        return id_match.group()
    return None

def download_webpage(url):
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        return res.text
    except requests.exceptions.RequestException as esx:
        print("There was a problem: %s % (exc)")
        return None

    