# Basic Text To Speech With Python

This simple project uses the `pyttsx3` library to convert written text to audio in .mp3 format.

## Project Contents

- **audio/**: Directory that will store the audio file generated from the text.
- **1_available_voices.py**: Find the Path of the voices available on your device.
- **2_text_to_voice.py**: Main script that converts text to speech.
- **3_type_your_text_here.txt**: File where you can write or paste texts so that they are later converted to audio in .mp3 format.
- **requirements.txt**: File listing project dependencies.

## Setup and Usage

1. Ensure you have Python installed on your system.
2. Create a virtual environment using the `requirements.txt` file:

    ```bash
    python -m venv env
    source env/bin/activate   # For Unix-based systems
    # or
    .\env\Scripts\activate    # For Windows-based systems
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the scripts in order of appearance:

    ```bash
    python 1_available_voices.py
    ```
    This script will generate a file named `available_voices.txt` with the path available for the voices on your computer.

    In the script `2_text_to_voice.py`, replace the empty string `voice = ""` with the path obtained from `available_voices.txt`. You can find the specific location in the comments within the script.

    Type your text in `3_type_your_text_here.txt` file, and execute the script.

    ```bash
    python 2_text_to_voice.py
    ```
    

## Contributions

Feel free to contribute to the project. You can open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
