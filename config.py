# @ImJanindu
# @Infinity_Bots

import os

BOTTOKEN = os.environ.get("BOTTOKEN", "1357892639:AAFz-ke7RIJmLcaO31ZKz3CmsZaDmS0STkc")
APIID = int(os.environ.get("APIID", "1795096"))
APIHASH = os.environ.get("APIHASH", "5ae7ae34532c5596aa1a43c51d92c04c")
DOWNLOADPATH = os.environ.get("DOWNLOADPATH", "Downloads/")
USERNAME = os.environ.get("USERNAME", "@hedwigdittomaltruvantbot")

"""
If you using VPS, first fork repo, remove upper strings and edit like this:

BOTTOKEN = "" # your bot token frpm @BotFather
APIID =      # your api id from https://my.telegram.org/
APIHASH = "" # your api hash from https://my.telegram.org/
DOWNLOADPATH = "Downloads/" # don't change
USERNAME = "" # put your bot username here
"""
