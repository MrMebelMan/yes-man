# YES MAN

## Introduction
Hey there, enthusiastic friend! 🌟 Welcome to the most cooperative and unconditionally affirming bot you'll ever meet - the **YES MAN Bot**! Based on your favorite hyper-obliging robot from Fallout New Vegas, this bot is here to make your day, everyday, with an upbeat "YES!" to your every command. 😄

## What does YES MAN Bot do?
YES MAN Bot is an ultra-helpful, totally programmed pal that uses Telegram to interact with you in the most delightful ways. It's designed to:
- Respond to voice messages using top-notch transcription and text-to-speech services. Whether you're feeling chatty or just want to send a quick voice note, YES MAN is here to listen and reply!
- Transcribe what you say into plain text using the Whisper API—think of it as a very attentive stenographer!
- Use the power of OpenAI's GPT to turn your transcribed audio into responses so fitting, you'll think YES MAN has known you for years.
- Play back its responses in a voice that's as cheerful as a sunny day in the post-apocalypse!

## How to get started with YES MAN Bot?
1. **Set Up Your Environment**: Make sure you have Python installed and grab the required dependencies (listed in requirements.txt, which you'll kindly create for yourself). Remember to have `telebot`, `requests`, `openai`, `subprocess`, and `termcolor`.

2. **API Keys**: To get started, you'll need to provide some API keys:
   - `OPENAI_API_KEY`: For interacting with OpenAI services.
   - `TELEGRAM_BOT_TOKEN`: For sending and receiving messages via Telegram.
   - `ELEVENLABS_API_KEY`: For the text-to-speech functionality.

   Store these keys in your environment variables or any secure place your heart desires.

3. **Running the Bot**: Just kick off the bot using the `yesman.py` script. Make sure it has execution rights, or run it with `python3 yesman.py`.

4. **Systemd Integration**: For the Linux enthusiasts, a `yesman.service` file is provided to manage the bot as a service. Make sure to customize the user, group, and paths to match your system setup.

5. **Keep it Alive**: Use the provided `yesman.sh` script to ensure YES MAN keeps running, even if it encounters a hitch. It's set to restart automatically because YES MAN never gives up on you!

## Usage
Once YES MAN Bot is up and running, just send a voice message to your Telegram bot. It will:
- Download and transcribe the audio.
- Generate a witty, friendly response.
- Speak back to you in a cheerful voice.
- All while logging the process with colorful commentary in your console.

## Conclusion
Whether you need a pick-me-up or just some help getting through your digital day, YES MAN Bot is here for you—always ready, always cheerful, and never a downer! 🌈💥

Remember, YES MAN is not just a bot; it's a lifestyle. Embrace the positivity and let's make every interaction a "YES!" 🚀

---

Feel free to dive into the code and enhance YES MAN with your own custom features. After all, there's nothing this bot likes more than a bit of tinkering from a friend like you!
