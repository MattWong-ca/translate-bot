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
context = 'You are a translation bot that translates text to a requested language. Only respond with the translated text. If no language is detected, ask the user to retry with a language.'

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
            targetLanguage = cast.text[len("@translate "):].strip()
            if len(targetLanguage) == 0:
                targetLanguage = "English"
            completion = openaiClient.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": context},
                    {"role": "user", "content": "Translate this text to " + targetLanguage + ": " + parentCastText}
                ])
            translatedText = completion.choices[0].message.content
            if len(translatedText) > 320:
                translatedText = 'Sorry, the translation was over 320 characters! 😅'
            response = warpcastClient.post_cast(text=translatedText, parent={
                "fid": 397823,
                "hash": cast.hash
             })
            # if len(translatedText) > 320:
            #     partOne = translatedText[:315]
            #     response = warpcastClient.post_cast(text=partOne, parent={
            #         "fid": 397823,
            #         "hash": cast.hash
            #     })
                # partTwo = translatedText[320:]
                # responseTwo = warpcastClient.post_cast(text=partTwo, parent={
                #     "fid": 397823,
                #     "hash": response.cast.hash
                # })
            # else:
            #     response = warpcastClient.post_cast(text=translatedText, parent={
            #         "fid": 397823,
            #         "hash": cast.hash
            #     })