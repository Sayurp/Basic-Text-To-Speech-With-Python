import pyttsx3


def available_voices():
    """
    Verifies the available voices on the device and saves the information to a text file.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    with open("available_voices.txt", "w", encoding="utf-8") as file:
        for v_property in voices:
            voice_id = v_property.id.replace("/", "\\")
            line = f"Available Voice: {v_property.name}\nCopy this language path: {voice_id}\n\n"
            file.write(line)
            print(line)


if __name__ == "__main__":
    available_voices()
