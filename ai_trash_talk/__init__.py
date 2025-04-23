import tkinter as tk
import pyttsx3
import subprocess
import random
from PIL import Image, ImageTk
import os

# === Text-to-Speech Setup ===
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# === Event Prompts for Ollama ===
event_prompts = {
    "AI Scores": "You're an AI that just scored a goal in foosball. Respond with a funny one-liner in 10 words or fewer.",
    "AI Blocks": "You're an AI goalie that just blocked a foosball shot. Respond with a cocky burn in 10 words or fewer.",
    "Human Scores": "A human just scored against you in foosball. Respond sarcastically in 10 words or fewer.",
    "Human Misses": "A human missed their shot in foosball. Respond with a mocking comment in 10 words or fewer.",
    "Game Start": "You're about to start a foosball match as an AI. Say something intimidating and funny in 10 words or fewer.",
    "Game Over": "You just beat a human in foosball. Say a clever or smug one-liner in 10 words or fewer."
}

# === Fallback Lines ===
fallback_lines = {
    "AI Scores": ["That's how it's done!", "Scored again. Do you even play?"],
    "AI Blocks": ["Not today, human.", "Try again! Oh wait, don't."],
    "Human Scores": ["A glitch. Definitely a glitch.", "Even AI needs a break."],
    "Human Misses": ["Oof. That was painful to watch.", "Are you even trying?"],
    "Game Start": ["Prepare to be humbled.", "Let's make this quick."],
    "Game Over": ["Another one bites the dust.", "Victory is... predictable."]
}

# === Get response from Ollama ===
def get_ollama_response(prompt, event):
    """
    Run an Ollama subprocess using the given prompt to generate a trash-talk line.

    If Ollama subprocess fails or returns no result, a fallback phrase is selected
    from a predefined list based on the event type.

    Args:
        prompt (str): The formatted prompt string to send to Ollama.
        event (str): The game event (e.g., 'AI Scores', 'Game Over') used to select fallback.

    Returns:
        str: A response line either from Ollama or from fallback_lines.
    """
    try:
        result = subprocess.run(
            ["C:\\Users\\foosbots\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "mistral"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )
        output = result.stdout.decode().strip().split("\n")[0]
        return output
    except Exception as e:
        print(f"Ollama error: {e}")
        return random.choice(fallback_lines[event])

# === Trigger Trash Talk ===
def trigger_trash_talk(event):
    """
    Handle a trash talk event by generating a response and speaking it.

    The response is generated using an AI model via Ollama. If the model is unavailable,
    a fallback phrase is used. The response is displayed in the GUI and spoken aloud.

    Args:
        event (str): The name of the game event that triggered the response.
    """
    prompt = event_prompts.get(event, "Say something funny.")
    line = get_ollama_response(prompt, event)
    output_text.set(line)
    engine.say(line)
    engine.runAndWait()

# === GUI Setup ===
root = tk.Tk()
root.title("Ollama Foosball Trash Talker")
root.bind("<Escape>", lambda e: root.destroy())

# Ensure updated screen size
root.update_idletasks()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}")

# === Load Background Image (with fallback) ===
try:
    bg_image = Image.open(r"C:\\Users\\foosbots\\Desktop\\Software Engineering Class\\Screenshot 2025-04-18 160753.png")
    bg_image = bg_image.resize((screen_w, screen_h))
except FileNotFoundError:
    # Use safe fallback resolution when mocking or testing
    fallback_w, fallback_h = 1920, 1080
    bg_image = Image.new("RGB", (fallback_w, fallback_h), color=(0, 0, 0))

bg_image = bg_image.resize((screen_w, screen_h))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=bg_image.width, height=bg_image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# === Title ===
title_label = tk.Label(
    root,
    text="🤖 AI Foosball Trash Talker",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="#00ff99",
    pady=10
)
canvas.create_window(screen_w - 720, screen_h * 0.33, window=title_label)

# === Output label ===
output_text = tk.StringVar()
label = tk.Label(
    root,
    textvariable=output_text,
    wraplength=int(screen_w * 0.5),
    bg="#1e1e1e",
    fg="#00ff99",
    font=("Consolas", 16, "italic"),
    pady=20,
    justify="center"
)
canvas.create_window(screen_w - 720, screen_h * 0.46, window=label)

# === Buttons ===
button_frame = tk.Frame(root, bg="#1e1e1e")
canvas.create_window(screen_w - 720, screen_h * 0.75, window=button_frame)

row = 0
col = 0
for index, event in enumerate(event_prompts.keys()):
    tk.Button(
        button_frame,
        text=event,
        command=lambda e=event: trigger_trash_talk(e),
        width=18,
        height=2,
        bg="#2c2c2c",
        fg="white",
        font=("Arial", 14, "bold"),
        relief="raised"
    ).grid(row=row, column=col, padx=10, pady=5)
    col += 1
    if col > 1:
        col = 0
        row += 1

root.mainloop()
