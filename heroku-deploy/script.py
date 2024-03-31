import os
from dotenv import load_dotenv
from farcaster import Warpcast

load_dotenv()

client = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))
# TEST COMMENT
for cast in client.stream_casts():
    # CHANGE TO JUST @TRANSLATE LATER
    if cast and "@translate chinese" in cast.text:
        if cast.parent_hash is not None:
            parentCastText = client.get_cast(cast.parent_hash).cast.text
            # SEND PARENT CAST TEXT TO OPENAI, GET RESPONSE
            response = client.post_cast(text="🦉: {}".format(parentCastText), parent={
                "fid": 397823,
                "hash": cast.hash
             })