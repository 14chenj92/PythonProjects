import pyttsx3
import tkinter as tk

def speak():
    answer = entry.get()
    if selected_voice.get() == "male":
        engine.setProperty('voice', voices[0].id)
    elif selected_voice.get() == "female":
        engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')

root = tk.Tk()
root.title("Text-to-Speech")

label = tk.Label(root, text="Enter what you want me to say:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

selected_voice = tk.StringVar(root, "male")

male_button = tk.Radiobutton(root, text="Male Voice", variable=selected_voice, value="male")
male_button.pack()

female_button = tk.Radiobutton(root, text="Female Voice", variable=selected_voice, value="female")
female_button.pack()

speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack()

root.mainloop()
