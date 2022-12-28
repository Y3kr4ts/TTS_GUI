import customtkinter
from customtkinter import END
import pyttsx3


def talk():
    tts_talk = pyttsx3.init()
    tts_talk.setProperty('rate', 125)
    voices = tts_talk.getProperty('voices')
    tts_talk.setProperty('voice', voices[1].id)
    tts_talk.say(entry.get())
    tts_talk.runAndWait()
    entry.delete(0, END)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.title("-TTS-")
root.geometry("600x190")
root.iconbitmap("icon.ico")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Text To Speech app created by y3krats")
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Text...", font=("Helvetic", 28), width=550)
entry.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame, text="Speak", command=talk)
button_1.pack(pady=12, padx=10)

root.mainloop()






