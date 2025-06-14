import os

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com/")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
TIMEOUT = int(os.getenv("TIMEOUT", "10000"))

