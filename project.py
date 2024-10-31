import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import random

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning! How can I help you?")
    elif 12 <= hour < 18:
        speak("Good afternoon! How can I assist you?")
    else:
        speak("Good evening! What would you like me to do?")

def listen():
    """Listens to the user's voice input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that. Please say it again.")
        return "None"
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the internet.")
        return "None"
    return command.lower()

def tell_time():
    """Tells the current time."""
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time_now}")

def open_website(url):
    """Opens a given website."""
    speak(f"Opening {url}")
    webbrowser.open(url)

def tell_joke():
    """Tells a random joke."""
    jokes = [
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why do programmers prefer dark mode? Because the light attracts bugs!"
    ]
    speak(random.choice(jokes))

def respond_to_command(command):
    """Performs actions based on the command received."""
    if "time" in command:
        tell_time()
    elif "open youtube" in command:
        open_website("https://www.youtube.com")
    elif "open google" in command:
        open_website("https://www.google.com")
    elif "joke" in command:
        tell_joke()
    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I am sorry, I don't have that function yet. Please try something else.")

# Main program starts here
if __name__ == "__main__":
    greet_user()
    while True:
        speak("Please tell me a command.")
        command = listen()
        if command != "None":
            respond_to_command(command)
