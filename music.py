import pygame
from tkinter import filedialog, Label, Scale, HORIZONTAL
from tkinter.ttk import Button, Style
from ttkthemes import ThemedTk  # For themed tkinter window
from mutagen.mp3 import MP3  # To get the duration of the MP3 file
import time
import threading

# Initialize pygame mixer
pygame.mixer.init()

# Initialize themed Tkinter window with "Azure" theme
root = ThemedTk(theme="azure")
root.title("Python Music Player")
root.geometry("380x380")

# Set up style for buttons and other widgets
style = Style(root)
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TLabel", font=("Helvetica", 9))
style.configure("TScale", sliderlength=20)

# Global variables
music_file = None
is_playing = False
song_length = 0

# Load Music Function
def load_music():
    global music_file, song_length
    music_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if music_file:
        song_label.config(text="Loaded: " + music_file.split("/")[-1])
        # Get the length of the song using mutagen
        song = MP3(music_file)
        song_length = song.info.length
        update_time_labels(0, song_length)

# Play Music Function
def play_music():
    global is_playing
    if music_file:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        is_playing = True
        status_label.config(text="Playing")
        update_playback_time()

# Pause Music Function
def pause_music():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False
    status_label.config(text="Paused")

# Resume Music Function
def resume_music():
    global is_playing
    pygame.mixer.music.unpause()
    is_playing = True
    status_label.config(text="Playing")
    update_playback_time()

# Stop Music Function
def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    status_label.config(text="Stopped")
    update_time_labels(0, song_length)

# Volume Control Function
def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# Update Time Labels
def update_time_labels(current_time, total_time):
    current_time_label.config(text=f"Current Time: {time.strftime('%M:%S', time.gmtime(current_time))}")
    duration_label.config(text=f"Duration: {time.strftime('%M:%S', time.gmtime(total_time))}")

# Update Playback Time Function
def update_playback_time():
    def update_time():
        while is_playing:
            current_time = pygame.mixer.music.get_pos() / 1000  # get_pos returns milliseconds
            update_time_labels(current_time, song_length)
            time.sleep(1)

    threading.Thread(target=update_time, daemon=True).start()

# GUI Widgets
load_button = Button(root, text="Load Music", command=load_music)
load_button.pack(pady=10)

play_button = Button(root, text="Play", command=play_music)
play_button.pack(pady=5)

pause_button = Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

resume_button = Button(root, text="Resume", command=resume_music)
resume_button.pack(pady=5)

stop_button = Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5)

# Volume Control Slider
volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume, label="Volume")
volume_slider.set(50)  # Set initial volume to 50%
volume_slider.pack(pady=10)

song_label = Label(root, text="No song loaded", wraplength=300)
song_label.pack(pady=5)

status_label = Label(root, text="Status: Stopped", wraplength=300)
status_label.pack(pady=5)

# Time Labels
current_time_label = Label(root, text="Current Time: 00:00")
current_time_label.pack(pady=5)

duration_label = Label(root, text="Duration: 00:00")
duration_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()