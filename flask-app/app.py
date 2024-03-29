from flask import Flask
import os
from dotenv import load_dotenv
from farcaster import Warpcast

load_dotenv()

client = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))

for cast in client.stream_casts():
    print(cast.text)