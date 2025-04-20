import tkinter as tk
from tkinter import scrolledtext
import os
from dotenv import load_dotenv
import openai

# Load .env and API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI client
client = openai.OpenAI(api_key=api_key)

def send_prompt():
    prompt = prompt_entry.get("1.0", tk.END).strip()
    if not prompt:
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        output_text = response.choices[0].message.content
    except Exception as e:
        output_text = f"Error: {e}"

    # Display output
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output_text)
    output_box.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("ChatGPT Prompt Sender")

tk.Label(root, text="Enter your prompt:").pack(pady=(10, 0))
prompt_entry = tk.Text(root, height=6, width=70)
prompt_entry.pack(padx=10, pady=(0, 10))

submit_button = tk.Button(root, text="Submit", command=send_prompt)
submit_button.pack(pady=5)

tk.Label(root, text="Response:").pack(pady=(10, 0))
output_box = scrolledtext.ScrolledText(root, height=12, width=70, state=tk.DISABLED, wrap=tk.WORD)
output_box.pack(padx=10, pady=(0, 10))

root.mainloop()
