import pyttsx3
import tkinter as tk

root = tk.Tk()

label = tk.Label(root,
                 text="Omer's text to speech",
                 font=("Arial", 18),
                 pady=15)

label.pack()

root.geometry("400x300")
root.configure(bg="#CBC3E3")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
selected_voice = tk.StringVar(root, "male") 
volume = 50

def speak():
    answer = entry.get()
    if selected_voice.get() == "male":
        engine.setProperty('voice', voices[0].id)
    elif selected_voice.get() == "female":
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', volume / 100) 
    engine.say(answer)
    engine.runAndWait()

def set_volume(new_volume):
    volume_label.config(text=str(new_volume))
    engine.setProperty('volume', new_volume / 100)

def increase_volume():
    global volume
    if volume < 100:
        volume += 10
        set_volume(volume)

def decrease_volume():
    global volume
    if volume > 0:
        volume -= 10
        set_volume(volume)

entry = tk.Entry(root, width=20)
entry.pack()

guide_voice = tk.Radiobutton(root, text="Male voice", variable=selected_voice, value="male")
guide_voice.pack(pady=10)

girl_voice = tk.Radiobutton(root, text="Female voice", variable=selected_voice, value="female")
girl_voice.pack(pady=0)

button = tk.Button(
    root,
    text="Speak",
    pady=5,
    width=15,
    command=speak
)
button.pack()

volume_frame = tk.Frame(root)
volume_frame.pack(pady=20)

UP_button = tk.Button(
    volume_frame,
    text="+",
    width=2,
    command=increase_volume
)
UP_button.pack(side=tk.LEFT)

volume_label = tk.Label(volume_frame, text="50")
volume_label.pack(side=tk.LEFT, padx=0)

Down_button = tk.Button(volume_frame, text="-", width=2, command=decrease_volume)
Down_button.pack(side=tk.LEFT, padx=0)

root.mainloop()
