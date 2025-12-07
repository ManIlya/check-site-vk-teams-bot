# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TEAMS_BOT_TOKEN = os.getenv("TEAMS_BOT_TOKEN")