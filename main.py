from IOTbase import voicerecognize as vr
import tkinter as tk

def main():
    end_program = False
    while not end_program:
        audio = vr.capture_voice_input()
        text = vr.convert_voice_to_text(audio)
        end_program = vr.process_voice_command(text)

if __name__ == "__main__":
    main()
