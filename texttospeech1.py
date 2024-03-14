import elevenlabs

audio = elevenlabs.generate(
    text="Hi, I'm from the future!",
    voice = "Adam"
)

elevenlabs.play(audio)