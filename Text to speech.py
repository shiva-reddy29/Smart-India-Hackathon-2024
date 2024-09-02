from gtts import gTTS
import os

# Text you want to convert to speech
hindi_text = "आपका दिन शुभ हो"

# Create a gTTS object, set the language to Hindi ('hi')
tts = gTTS(text=hindi_text, lang='hi')

# Save the audio file
tts.save("hindi_speech.mp3")

# Play the audio file
os.system("start hindi_speech.mp3")  # On Windows