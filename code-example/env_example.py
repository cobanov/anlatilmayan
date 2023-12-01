import logging
import os
import sys

from dotenv import load_dotenv
from rich.logging import RichHandler

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level="NOTSET", format=LOG_FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

load_dotenv()

TOKEN = os.getenv("TOKEN")
logging.info(f"Token: {TOKEN}")

try:
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    logging.info("OPENAI_API_KEY retrieved successfully.")
except KeyError:
    logging.error("Environment variables for OPENAI_API_KEY not set properly.")
    sys.exit(1)
