# 🌎 Translate Bot
Demo video: [link](https://youtu.be/yFIRuzAXdOA)
<br>
Bot: [Warpcast profile](https://warpcast.com/translate)
<br>
API repo: [GitHub link](https://github.com/MattWong-ca/translate-bot-nextjs) (for fetching AI responses)
<br>
<!-- INSERT IMAGE HERE -->

# 🤖 About
A translation bot removing language barriers on the Farcaster client, Warpcast. Use `@translate <language>` to get an instant AI translation in any language!
<br>
<br>
Examples:
<br>
    - `@translate spanish`
    <br>
    - `@translate to English`
    <br>
    - `@translate what is translate bot?`
    <br>
    - `@translate what languages can you translate?`
    <br>
    <br>
<!-- INSERT IMAGE HERE -->


# ❓ Problem
Language barriers currently result in a poor user experience for both international and English-speaking users, as they need to switch apps to Google Translate for translations. 
<br>
<br>
Many users having been asking for a translation feature, which is why I built Translate Bot. It's currently live, try it out! 🌎🚀
<!-- INSERT IMAGE HERE -->
<br>
<!-- INSERT IMAGE HERE -->

# 🛠️ Tech Stack
➔ farcaster-py: for detecting recent casts with the `"@translate"` keyword, and posting cast responses
<br>
➔ OpenAI: for translating the actual text into the desired language
<br>
➔ FLock.io: for answering questions about the bot itself, like what it does and what languages it translates
<br>

When a user tags `@translate`, the farcaster-py SDK will detect the cast. This cast has a `cast.text` property, and the `cast.parent_hash` property can be used to retrieve the parent cast's text. Both of these are either passed into OpenAI's API or FLock's API. 
<br>
If it's a question about the bot itself, like "what is translate bot?" or "what languages can you translate?", the AI model I created through FLock will have enough context to answer accurately. I send a request to this API by using Axios in the [Nextjs repo](https://github.com/MattWong-ca/translate-bot-nextjs). If it's a translation query, OpenAI's API will translate the text and provide a response. 
<br>
Once I get the response back, I again use the farcaster-py SDK to help post an instant reply. If the text is over 320 characters, I set it to return a default phrase.

# 🗺️ Road Map
