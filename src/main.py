import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

# Initialize recognizer and Text-to-Speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("[INFO] Trying to recognize using Google Web Speech API...")
            # Try with Google API (Online)
            text = recognizer.recognize_google(audio)
            print(f"[Google Recognized]: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            # If Google can't recognize speech
            print("[ERROR] Google could not understand audio.")
        
        except sr.RequestError:
            # If Google API is unreachable (No Internet)
            print("[ERROR] Google API request failed. No Internet or Server issue.")

        # Now fallback to Sphinx (Offline)
        try:
            print("[INFO] Switching to Offline Mode: Using CMU Sphinx...")
            text = recognizer.recognize_sphinx(audio)
            print(f"[Sphinx Recognized]: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            print("[ERROR] Sphinx could not understand audio.")
            speak("Sorry, I could not understand.")
            return None


def perform_task(command):
    if command is None:
        return

    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad.exe")

    elif "open chrome" in command:
        speak("Opening Chrome")
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(path)

    elif "search" in command:
        speak("What should I search?")
        search_text = recognize_speech()
        if search_text:
            url = f"https://www.google.com/search?q={search_text}"
            webbrowser.open(url)
            speak(f"Here is what I found for {search_text}")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        speak(f"The time is {current_time}")

    elif "date" in command:
        today = datetime.date.today()
        print(f"Today's Date: {today}")
        speak(f"Today's date is {today}")

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Exiting, Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand the command.")

# Main loop
if __name__ == "__main__":
    speak("Voice Assistant Started. How can I help you?")
    while True:
        command = recognize_speech()
        perform_task(command)
