import sys

try:
    # Import pyttsx3 module for text-to-speech functionality
    import pyttsx3
except ImportError:
    # If pyttsx3 module is not installed, inform the user about the installation process
    print('This program requires the pyttsx3 module for text-to-speech functionality.')
    print('To install, on Windows, open Command Prompt and run: pip install pyttsx3')
    print('On macOS and Linux, open Terminal and run: pip3 install pyttsx3')
    sys.exit()

# Initialize the Text-to-Speech (TTS) engine
tts = pyttsx3.init()

print('Text To Speech Talker')
print('Experience text-to-speech using the pyttsx3 module, which employs')
print('NSSpeechSynthesizer (macOS), SAPI5 (Windows), or eSpeak (Linux) engines.')
print('The TTS engine, provided by pyttsx3, converts text into spoken words.')
print('It supports multiple platforms, utilizing different underlying speech engines.')
print()
print('Enter the text to be spoken, or type QUIT to exit.')
while True:
    # Prompt user to input text
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Thanks for using the Text-to-Speech Talker!')
        sys.exit()

    # Add the text for the TTS engine to say
    tts.say(text)
    
    # Make the TTS engine say the provided text
    tts.runAndWait()
