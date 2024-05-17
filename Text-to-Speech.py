import pyttsx3
import tkinter as tk

def speak():
    answer = entry.get()
    if selected_voice.get() == "male":
        engine.setProperty('voice', voices[0].id)
    elif selected_voice.get() == "female":
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', volume_scale.get() / 100)
    engine.say(answer)
    engine.runAndWait()

def set_volume(new_volume):
    engine.setProperty('volume', new_volume / 100)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)

root = tk.Tk()
root.title("Text-to-Speech")
root.geometry("400x300")
bg = tk.PhotoImage(file = "back.png") 
label1 = tk.Label( root, image = bg) 
label1.place(x = 0, y = 0) 

title = tk.Label(root, text="My Text to Speech", font=("Rupee", 20), pady=10, bg="white")
title.pack()

label = tk.Label(root, text="Enter what you want me to say:", pady=10, bg="white")
label.pack()

entry = tk.Entry(root, width=35)
entry.pack(pady=5)

selected_voice = tk.StringVar(root, "male")

male_button = tk.Radiobutton(root, text="Male Voice", variable=selected_voice, value="male", bg="white")
male_button.pack(pady=5)

female_button = tk.Radiobutton(root, text="Female Voice", variable=selected_voice, value="female", bg="white")
female_button.pack(pady=5)

volume_label = tk.Label(root, text="Volume:", bg="white")
volume_label.pack()

volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=set_volume)
volume_scale.set(50)
volume_scale.pack(pady=5)

speak_button = tk.Button(root, text="Speak", command=speak, width=7)
speak_button.pack()

root.mainloop()
