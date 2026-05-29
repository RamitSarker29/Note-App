import tkinter as tk 
from tkinter import filedialog, messagebox 
root= tk.Tk()
root.title("Ramit's Text App")
root.geometry("800x600")
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("Folio", 25)
)
text.pack(expand=True,fill=tk.BOTH)
def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


def save_file():
    file_path= filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved successfully")

menu= tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)

 
menu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="Naya", command=new_file)
file_menu.add_command(label="Kholo", command=open_file)
file_menu.add_command(label="Save Karo", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Niklo", command=root.quit)


root.mainloop()







