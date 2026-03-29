import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now...")

        # 🔥 Improve accuracy
        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=5,          # wait max 5 sec to start speaking
            phrase_time_limit=7 # max speaking duration
        )

    try:
        text = recognizer.recognize_google(audio, language='en-IN')
        print("Recognized:", text)
        return text.lower()

    except sr.UnknownValueError:
        return "ERROR"

    except sr.RequestError:
        return "API error"


