from tkinter import *
import wikipedia
#  pip install wikipedia

def get_data():
    entry_value = entry.get()  # Get user input from entry field
    answer.delete(1.0, END)    # Clear previous results in text box
    try:
        # Fetch summary from Wikipedia
        answer_value = wikipedia.summary(entry_value, sentences=3)  # Limit to 3 sentences for better readability
        answer.insert(INSERT, answer_value)
    except wikipedia.exceptions.DisambiguationError as e:
        # Handles cases where the query is ambiguous
        answer.insert(INSERT, f"Error: {entry_value} may refer to multiple things:\n{e.options}")
    except wikipedia.exceptions.PageError:
        # Handles cases where the page doesn't exist
        answer.insert(INSERT, "Error: Page not found.")
    except Exception as e:
        # Handle any other exceptions
        answer.insert(INSERT, f"Error: {str(e)}")

# GUI Setup
win = Tk()
win.title("Wikipedia Search")

# Entry field and button for search
topframe = Frame(win)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text="Search", command=get_data)
button.pack()
topframe.pack(side=TOP)

# Scrollable Text Box for displaying results
bottomframe = Frame(win)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

# Answer box with word wrapping
answer = Text(bottomframe, width=50, height=20, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

# Start the Tkinter loop
win.mainloop()

