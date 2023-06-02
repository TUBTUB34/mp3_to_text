import os
import speech_recognition as sr
from docx import Document

def convert_audio_to_text(audio_file_path):
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # Load the WAV file
    with sr.AudioFile(audio_file_path) as source:
        # Read the audio data from the file
        audio_data = recognizer.record(source)

        # Perform speech recognition
        text = recognizer.recognize_google(audio_data)

        # Save recognized text to a .docx file
        doc = Document()
        doc.add_paragraph(text)
        doc_path = audio_file_path + '.docx'
        doc.save(doc_path)

        return doc_path

if __name__ == "__main__":
    import sys

    # Check if the audio file path is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <audio_file_path>")
        sys.exit(1)

    # Get the audio file path from the command-line argument
    audio_file_path = sys.argv[1]

    # Check if the audio file exists
    if not os.path.isfile(audio_file_path):
        print("Error: Audio file not found!")
        sys.exit(1)

    # Call the audio-to-text conversion function
    doc_file_path = convert_audio_to_text(audio_file_path)

    # Print success message
    print(f"Text extracted and saved as {doc_file_path}")