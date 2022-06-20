import asyncio
from pytgcalls import idle
from ELLIOT.Database import db

import os
import sys
import random
import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2
from pyrogram import Client
from pytgcalls import PyTgCalls
from ELLIOT.main import *



loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
