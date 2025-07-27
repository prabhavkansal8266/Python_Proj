import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 by Prabhav")
    print("Enter you want me to say. Type 'q' to quit.")

    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == 'q':
            speak("Goodbye, my friend.")
            break
        speak(user_input)
