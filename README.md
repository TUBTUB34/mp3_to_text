# Audio to Text Converter

This script converts audio from a `.wav` file to text using Google Speech Recognition and saves the text in a `.docx` file. It’s useful for transcribing speech from audio files into editable text documents.

## Features
- Converts speech from `.wav` audio files to text.
- Saves transcribed text into a `.docx` document.
- Uses Google Speech Recognition via the `speech_recognition` Python library.

## Requirements
- Python 3.6+
- The following Python packages:
  - `speech_recognition`
  - `python-docx`

You can install the dependencies by running:
```bash
pip install speechrecognition python-docx
```
## Usage
1. - Place your .wav audio file in the same directory as the script, or provide the path to the file.

2. - Run the script with the following command:

```bash
python script.py <audio_file_path>
```

Replace <audio_file_path> with the path to your .wav file.

The script will convert the audio to text and save it as a .docx file in the same directory with the same name as the audio file (with a .docx extension).

## Example
```bash
python script.py audio_sample.wav
```
After successful execution, you’ll see a message like:

```vbnet
Text extracted and saved as audio_sample.wav.docx
```

## File Structure
```bash
.
├── script.py            # Main script file
└── README.md            # Documentation for the repository
```

## Error Handling
Checks if the audio file path is provided and valid.
Displays a message if the file is not found.
