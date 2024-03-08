import pyttsx3

engine = pyttsx3.init()

while True: 
    answer = input("Enter what you want me to say!")
    engine.say(answer)
    engine.runAndWait()