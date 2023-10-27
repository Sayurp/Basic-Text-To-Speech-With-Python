import pyttsx3


def read_text_from_file(file_path):
    """
    Reads text from a file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Content of the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def text_to_speech(voice_id=None, output_file="audio/text_voice.mp3", default_message="Type your text in the file: 3_type_your_text_here.txt"):
    """
    Converts text to speech and saves the result to an audio file.

    Args:
        voice_id (str): Path of the voice to use. Can be None to use the default voice.
        output_file (str): Path of the output audio file.
        default_message (str): Default message if no text is found in the file.
    """
    # Read text from the file
    text = read_text_from_file("3_type_your_text_here.txt")

    # Use default message if no text is found
    if text is None or text.strip() == "":
        text = default_message

    engine = pyttsx3.init()

    if voice_id:
        engine.setProperty('voice', voice_id)

    engine.save_to_file(text, output_file)
    engine.runAndWait()


if __name__ == "__main__":
    # Paste the available voice path here:
    voice = ""

    text_to_speech(voice_id=voice)
