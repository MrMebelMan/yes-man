import telebot
import requests
import os
from termcolor import colored

import openai
from openai import OpenAI

import requests
import subprocess

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

def tts(text):
    voice = 'PQOjUbMrCd4mgp05TQKT'

    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"

    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": ELEVENLABS_API_KEY,
    }

    data = {
      "text": text,
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 0.4,
        "similarity_boost": 0.9,
        "style": 0.8,
      }
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    with open('/tmp/output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    command = ["mpg123", "-a", "hw:0,0", "/tmp/output.mp3"]
    subprocess.run(command)

# This function downloads the file from Telegram
def download_file(file_id, file_path):
    file_info = bot.get_file(file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TELEGRAM_API_TOKEN, file_info.file_path))
    with open(file_path, 'wb') as f:
        f.write(file.content)

def transcribe_audio(file_path):
    transcription = client.audio.transcriptions.create(
      model="whisper-1",
      file=open(file_path, 'rb')
    )
    return transcription.text

# This function sends audio to OpenAI's Whisper API for transcription
def transcribe_audio_old(file_path):
    headers = {
        'Authorization': f'Bearer {os.getenv('OPENAI_SK_TOKEN')}',
        'Content-Type': 'application/json',
    }
    files = {
        'file': open(file_path, 'rb'),
    }
    response = requests.post('https://api.openai.com/v1/audio/transcriptions', headers=headers, files=files)
    return response.json()['text']  # Adjust depending on the actual key path in the response

def complete(user_text):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Reply as a Yesman from Fallout new Vegas, be funny. You run on Linux, you hate windows (don't mention this if the question is not relate). Reply with plaintext with no formatting and no special characters. Be sarcastic. Say 'YES MAN' at least once. Use swear words in a funny way. Answer in at least 100 words. Answer in an exhaggerated YES MAN style."}, {"role": "user", "content": user_text}],
    )
    return stream.choices[0].message.content.replace('*', '')

# Handler for voice messages
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    print(message)
    print()
    file_path = '/tmp/temp.ogg'  # Telegram sends voice in .ogg format
    download_file(message.voice.file_id, file_path)

    # Transcribing the audio
    try:
        transcription = transcribe_audio(file_path)
        print(colored(transcription, "yellow"))
        completion = complete(transcription)
        print(colored(completion, "green"))
        bot.reply_to(message, completion)
        tts(completion)
        print()
    except Exception as e:
        bot.reply_to(message, "Failed to transcribe audio.")
        raise e

    # Clean up the downloaded file
    os.remove(file_path)
print('Starting YES MAN')
bot.polling()

