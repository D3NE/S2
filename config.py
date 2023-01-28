import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu0vpr6XiSLHU_IU2Xfh5k_deK_HolHlsTZQFpIu1onrgxenNaajQ5mseJRDIOlP8geB9JMbs1XQljH85tDI39HNjLgdDKqAvuX_fA7r8qfsANzFpdXwamafxusT4yUT6L-CDuuHY8WNBCGIx6rOqeVuQYrlZJ1KEB_fsHKk-IbWp8GyWeQjzYqLfdsBNG4qb0iyJIy7zr1F1RM3S6Prn-ML_moCSsh83OmxRFqHbc9a7cFSIQ-aotSaPvt6vKM9GqHIHUS2SOC5DumTaStLQdHS6FVb2RslcLpHwKnl5NHy6cvRyOIcqI7yUcv0toDBwi_5wBBQ00I7yWKdgIKIuN_8=")
BOT_TOKEN = getenv("BOT_TOKEN", "5844765918:AAFwDxLifMXFhEFkyCeujtXxjjQtSWAOYr8")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID", "23559116")
API_HASH = getenv("API_HASH","ac878ed19ca558e9a23e891098e328af")
OWNER_NAME = getenv("OWNER_NAME", "5179721996")
ALIVE_NAME = getenv("ALIVE_NAME", "- ديـنار .𐇲 ")
BOT_USERNAME = getenv("BOT_USERNAME", "sjjsshdbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "sjjsshdbot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "jddjdjkc")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "I404P")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5179721996").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/06b651dc0d827b6887764.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
