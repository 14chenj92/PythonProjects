from tkinter import *
import wikipedia

# Fetch and display data from Wikipedia
def get_data():
    entry_value = search_var.get()  # Use StringVar for entry
    answer.delete(1.0, END)         # Clear previous results
    try:
        answer_value = wikipedia.summary(entry_value, sentences=3)
        answer.insert(INSERT, answer_value)
    except wikipedia.exceptions.DisambiguationError as e:
        answer.insert(INSERT, f"Error: '{entry_value}' may refer to multiple things:\n{e.options}")
    except wikipedia.exceptions.PageError:
        answer.insert(INSERT, "Error: Page not found.")
    except Exception as e:
        answer.insert(INSERT, f"Error: {str(e)}")

# GUI Setup
win = Tk()
win.title("Wikipedia Search")

# Use StringVar for entry
search_var = StringVar()

# Entry field and button
topframe = Frame(win)
entry = Entry(topframe, textvariable=search_var)  # Bind to StringVar
entry.pack()
button = Button(topframe, text="Search", command=get_data)
button.pack()
topframe.pack(side=TOP)

# Scrollable Text Box for results
bottomframe = Frame(win)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

answer = Text(bottomframe, width=50, height=20, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

# Start Tkinter event loop
win.mainloop()
