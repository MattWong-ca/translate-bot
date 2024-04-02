import os
from dotenv import load_dotenv
from farcaster import Warpcast
from openai import OpenAI
import requests
import json

load_dotenv()
url = 'http://localhost:3000/api/translate'

warpcastClient = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))
openaiClient = OpenAI(api_key=os.environ.get("OPENAI_ENV_VAR"))
context = 'You are a translation bot that only responds when "@translate <language>" is mentioned. If no language is present, return "🤨"'

for cast in warpcastClient.stream_casts():
    # If it's a question about the bot itself call FLock, else use OpenAI
    if cast and "@translate what" in cast.text:
        if cast.parent_hash is not None:
            questionToApi = {'question': cast.text[11:]}
            answer = requests.post(url=url, json=questionToApi)
            response = warpcastClient.post_cast(text=answer.json()['answer'], parent={
                "fid": 397823,
                "hash": cast.hash
             }) 
    elif cast and "@translate" in cast.text and cast.author.fid != 397823:
        if cast.parent_hash is not None:
            # SEND USER FID TO DB TO CHECK IF IT'S OVER 10 USES
            # fid = {'number': cast.author.fid}
            parentCastText = warpcastClient.get_cast(cast.parent_hash).cast.text
            completion = openaiClient.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": cast.text + ": " + parentCastText}
                ])
            response = warpcastClient.post_cast(text=completion.choices[0].message.content, parent={
                "fid": 397823,
                "hash": cast.hash
             })