import os
from dotenv import load_dotenv
from farcaster import Warpcast
from openai import OpenAI
import requests
import json

load_dotenv()
# url = 'http://localhost:3000/api/multiply'
# data = {'number': 5}

warpcastClient = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))
openaiClient = OpenAI(api_key=os.environ.get("OPENAI_ENV_VAR"))
context = 'You are a translation bot that only responds when "@translate <language>" is mentioned. If no language is present, return "🤨"'

for cast in warpcastClient.stream_casts():
    # CHANGE TO JUST @TRANSLATE LATER
    if cast and "@translate chinese" in cast.text:
        if cast.parent_hash is not None:
            parentCastText = warpcastClient.get_cast(cast.parent_hash).cast.text
            # SEND USER FID TO DB TO CHECK IF IT'S OVER 10 USES
            # response = requests.post(url=url, json=data)
            # print(response.json()['result'])


            # SEND PARENT CAST TEXT TO OPENAI, GET RESPONSE
            completion = openaiClient.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": cast.text + ": " + parentCastText}
                ])
            print(completion.choices[0].message)
            # response = warpcastClient.post_cast(text="🦉: {}".format(parentCastText), parent={
            #     "fid": 397823,
            #     "hash": cast.hash
            #  })