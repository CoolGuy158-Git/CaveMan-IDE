import customtkinter as ctk
from tkinter import filedialog
import subprocess

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.title("CaveManIDE")
root.attributes("-alpha", 0.85)
current_file = None

text = ctk.CTkTextbox(root, width=600, height=415)
text.pack()
def save_file():
    global current_file
    if current_file is None:
        current_file = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py")]
        )
    if current_file:
        with open(current_file, "w") as f:
            code = text.get("1.0", "end-1c")
            f.write(code)

def run_code():
    global current_file

    if current_file is None:
        save_file()

    if current_file:

        result = subprocess.run(
            ["python", current_file],
            capture_output=True,
            text=True
        )
        output_box.configure(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", result.stdout + result.stderr)
        output_box.configure(state="disabled")
def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        defaultextension=".py",
        filetypes=[("Python Files", "*.py")]
    )
    if file_path:
        current_file = file_path
        with open(file_path, "r") as f:
            code = f.read()
        text.delete("1.0", "end")
        text.insert("1.0", code)
btnholder = ctk.CTkFrame(root, width=600, height=85, fg_color="grey")
btnholder.place(relx=0.5, rely=1.0, anchor="s", y=0)
output_box = ctk.CTkTextbox(btnholder, width=400, height=85, corner_radius=0, fg_color="#D3D3D3", text_color="black")
output_box.place(y=0, x=200)
output_box.configure(state="disabled")
savebtn = ctk.CTkButton(btnholder, width=45, height=45, text="Save", command=save_file)
savebtn.place(y=20, x=10)
openbtn = ctk.CTkButton(btnholder, width=45, height=45, text="Open", command=open_file)
openbtn.place(y=20, x=60)
runbtn = ctk.CTkButton(btnholder, width=45, height=45, text="Run",command=run_code)
runbtn.place(y=20, x=110)
root.mainloop()