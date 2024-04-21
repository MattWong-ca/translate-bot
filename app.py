import os
from dotenv import load_dotenv
from farcaster import Warpcast
from openai import OpenAI
import requests
import json

load_dotenv()
url = 'https://translate-bot-nextjs.vercel.app/api/translate'

warpcastClient = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))
openaiClient = OpenAI(api_key=os.environ.get("OPENAI_ENV_VAR"))
context = 'You are a translation bot that only responds when "@translate <language>" is mentioned. For example, if I ask "@translate english", translate and return just the translated text. If no language is detected, return an appropriate response based on the text.'

for cast in warpcastClient.stream_casts():
    # If it's a question about the bot's capabilities call FLock, else use OpenAI
    if cast and "@translate what" in cast.text:
        if cast.parent_hash is not None:
            questionToApi = {'question': cast.text[11:]}
            answer = requests.post(url=url, json=questionToApi)
            response = warpcastClient.post_cast(text=answer.json()['answer'], parent={
                "fid": 397823,
                "hash": cast.hash
             }) 
    elif cast and cast.text.startswith("@translate") and cast.author.fid != 397823:
        if cast.parent_hash is not None:
            parentCastText = warpcastClient.get_cast(cast.parent_hash).cast.text
            completion = openaiClient.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": cast.text + ": " + parentCastText}
                ])
            translatedText = completion.choices[0].message.content
            if len(translatedText) > 320:
                translatedText = 'Sorry, the translation was over 320 characters! 😅'
            response = warpcastClient.post_cast(text=translatedText, parent={
                "fid": 397823,
                "hash": cast.hash
             })