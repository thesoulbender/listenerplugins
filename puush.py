import urllib2
import random
from util import hook


def make_string():
    stuff = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    string = random.choice("123")
    for x in range(4):
        string += random.choice(stuff)
    return string


def check_url(code):
    try:
        x = urllib2.urlopen(make_url(code))
        return True
    except:
        return False  # sorry <3


def make_url(code):
    return "http://puu.sh/" + code


@hook.command(autohelp=False)
def puush(inp):
    """puush -- Returns a random puush entry."""
    out = ""
    num = 0
    if not inp:
        inp = "1"
    if inp[0] not in "123456789":
        out += "Defaulting to one: "
        num = 1
    elif int(inp[0]) > 5:
        out += "Five images max: "
        num = 5
    else:
        num = int(inp[0])
    images = []
    for x in range(num):
        ran = make_string()
        while not check_url(ran):
            ran = make_string()
        images.append(make_url(ran))
    return out + " ".join(images)
