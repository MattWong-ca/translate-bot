# 🌎 Translate Bot
Demo video: [link](https://youtu.be/yFIRuzAXdOA)
<br>
Bot: [Warpcast profile](https://warpcast.com/translate)
<br>
API repo: [GitHub link](https://github.com/MattWong-ca/translate-bot-nextjs) (for fetching AI responses)
<br>
<br>
<img width="1440" alt="Translate Bot" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/5307e8a5-d1cb-4335-96e9-7cbf52074c5e">

# 🤖 About
A translation bot removing language barriers on the Farcaster client, Warpcast. Use `@translate <language>` to get an instant AI translation in any language!
<br>
<br>
Examples:
- `@translate spanish`
- `@translate to English`
- `@translate what is translate bot?`
- `@translate what languages can you translate?`
    <br>
    <br>

<img width="1440" alt="Features" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/f638e426-21dd-4b48-8e1b-3b7acf35d29f">
<img width="1440" alt="Users" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/b0d68150-4e3b-47ab-a104-20850c850874">

# ❓ Problem
Language barriers currently result in a poor user experience for both international and English-speaking users, as they need to switch apps to Google Translate for translations. 
<br>
<br>
Many users having been asking for a translation feature, which is why I built Translate Bot. It's currently live, try it out! 🌎🚀
<br>
<br>
<img width="1440" alt="Problem 1" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/ee04dcc3-e754-4422-80bb-52bcd11549cd">
<img width="1440" alt="Problem 2" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/e506285e-08fd-4a5e-9a30-bf72028244b2">

# 🛠️ Tech Stack
➔ farcaster-py: for detecting recent casts with the `"@translate"` keyword, and posting cast responses
<br>
➔ OpenAI: for translating the actual text into the desired language
<br>
➔ FLock.io: for answering questions about the bot itself, like what it does or what languages it translates
<br>

When a user tags `@translate`, the farcaster-py SDK will detect the cast. This cast has a `cast.text` property, and the `cast.parent_hash` property can be used to retrieve the parent cast's text. Both of these are either passed into OpenAI's API or FLock's API. 
<br>
<br>
If it's a question about the bot itself, like "what is translate bot?" or "what languages can you translate?", the AI model I created through FLock will have enough context to answer accurately. I send a request to this API by using Axios in the [Next.js repo](https://github.com/MattWong-ca/translate-bot-nextjs). If it's a translation query, OpenAI's API will translate the text and provide a response. 
<br>
<br>
Once I get the response back, I again use the farcaster-py SDK to help post an instant reply. If the text is over 320 characters, I set it to return a default phrase.

<img width="1440" alt="Tech stack" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/8223af69-465c-4330-b60b-74cec0884c75">

# 🗺️ Road Map
1. Cast Actions: using the recently-released cast actions to make the bot a 2-click UX
2. Neynar APIs: use their webhooks and APIs for easier bot maintenance, and use Frames to gamify the UX
3. OpenAI/FLock: finetune the AI models and provide better data/prompts for more accurate responses
<img width="1440" alt="Roadmap" src="https://github.com/MattWong-ca/translate-bot/assets/66754344/2c547227-0ece-40c2-8402-6d1511da9bdd">

