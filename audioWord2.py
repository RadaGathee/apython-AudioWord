import whisper
import tkinter as tk
from tkinter import filedialog


def transcribe_audio(file_path):
    # whisper model size: tiny(75mb uses 390mbRAM), base(142mb uses 510mbRAM), small(466MB 1.2gb RAM), medium, large(3.2gb uses 4.2GB RAM))
    model = whisper.load_model("base")

    result = model.transcribe(file_path)
    return result['text']


def browse_file():
    """
    Opens a file dialog to select an audio file and returns the file path.
    """
    root = tk.Tk()
    root.withdraw()  # Hides the main window
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("Audio Files", "*.mp3;*.wav;*.m4a")]
    )
    return file_path


if __name__ == "__main__":
    audio_file = browse_file()

    if audio_file:
        try:
            transcription = transcribe_audio(audio_file)
            print("\nTranscription:\n")
            print(transcription)

            #save the transcription to a file
            output_file = "transcription.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(transcription)
            print(f"\nTranscription saved to {output_file}")

        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No file selected.")
