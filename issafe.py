"""
issafe.py

Check the Google Safe Browsing list to see a website's safety rating.

Created By:
    - Foxlet <http://furcode.tk/>

License:
    GNU General Public License (Version 3)
"""
import re
import types
import requests
from urllib.parse import urlparse
from . import ListenerPlugin

API_SB = "https://sb-ssl.google.com/safebrowsing/api/lookup"

class IsSafe(ListenerPlugin):
    def __init__(self):
        super(IsSafe, self).__init__()
        self._matches = ['issafe',]
        self.dev_key = None

    # FIXME: this API is not permenant
    def set_bot(self, bot):
        self.bot = bot
        try:
            self.dev_key = self.bot.config.get("api_keys", {}).get("google_dev_key", None)
        except Exception as e:
            print(e)

    def call(self, regex_command, string_argument, done=None):
        if regex_command in self._matches:
            result = issafe(string_argument, self.dev_key)
            if isinstance(done, types.FunctionType):
                done()
            done = True
            return result, done

def issafe(text, dev_key=None):
    """<website> -- Checks the website against Google's Safe Browsing List."""
    if urlparse(text).scheme not in ['https', 'http']:
        return "Check your URL (it should be a complete URI)."

    parsed = requests.get(API_SB, params={"url": text, "client": "cloudbot", "key": dev_key, "pver": "3.1", "appver": str(cloudbot.__version__)})

    if parsed.status_code == 204:
        condition = "\x02{}\x02 is safe.".format(text)
    else:
        condition = "\x02{}\x02 is known to contain: {}".format(text, parsed.text)
    return condition
