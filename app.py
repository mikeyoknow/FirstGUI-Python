import tkinter as tk
from tkinter import filedialog, Text
import os
import webbrowser

def search_youtube():
    query = entry.get().strip()
    if not query:
        error_label.config(text="Please enter a search query!")
        return
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open_new_tab(url)

root = tk.Tk()
root.title("YouTube Search")

canvas = tk.Canvas(root, height=300, width=300, bg="red")
canvas.pack()



frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

label = tk.Label(frame, text="Enter your search here:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

searchNow = tk.Button(root, text="Go!", padx=10, pady=5, fg="black", bg="#263D42", command=search_youtube)
searchNow.pack()

image = tk.PhotoImage(file="youtube_logo.png").subsample(10)
logo_label = tk.Label(frame, image=image)
logo_label.pack()

error_label = tk.Label(frame, text="")
error_label.pack()

root.mainloop()