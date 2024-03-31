import os
from dotenv import load_dotenv
from farcaster import Warpcast
from openai import OpenAI

load_dotenv()

warpcastClient = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))
openaiClient = OpenAI(api_key=os.environ.get("OPENAI_ENV_VAR"))

for cast in warpcastClient.stream_casts():
    # CHANGE TO JUST @TRANSLATE LATER
    if cast and "@translate chinese" in cast.text:
        if cast.parent_hash is not None:
            parentCastText = warpcastClient.get_cast(cast.parent_hash).cast.text
            # SEND PARENT CAST TEXT TO OPENAI, GET RESPONSE
            response = warpcastClient.post_cast(text="🦉: {}".format(parentCastText), parent={
                "fid": 397823,
                "hash": cast.hash
             })