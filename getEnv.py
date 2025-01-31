import os
from dotenv import load_dotenv
load_dotenv()

name=os.getenv("Name")
pw=os.getenv("password")
lc=os.getenv("location")
print(name)
print(pw)
print(lc)