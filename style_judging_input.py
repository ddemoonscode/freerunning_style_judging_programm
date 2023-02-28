import tkinter as tk

class ScoreEntry(tk.Frame):
    def __init__(self, master=None, label_text="Score"):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text=label_text)
        self.entry = tk.Entry(self, font=("Helvetica", 16))
        self.pack_widgets()

    def pack_widgets(self):
        self.label.pack(side=tk.LEFT)
        self.entry.pack(side=tk.LEFT)

    def get_score(self):
        score = self.entry.get()
        self.entry.delete(0, tk.END)
        return score

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Score Entry")
        self.name = tk.StringVar()
        self.name_label = tk.Label(self, text="Name:", font=("Helvetica", 16))
        self.name_entry = tk.Entry(self, textvariable=self.name, font=("Helvetica", 16))
        self.submit_button = tk.Button(self, text="Submit", font=("Helvetica", 16), command=self.submit)
        self.entries = []
        self.pack_widgets()

    def pack_widgets(self):
        self.name_label.pack(pady=10)
        self.name_entry.pack(pady=10)
        self.submit_button.pack(pady=20)
        for i, label_text in enumerate(["Difficulty:", "Creativity:", "Safety:", "Flow:", "Overall:"]):
            entry = ScoreEntry(self, label_text=label_text)
            self.entries.append(entry)
            entry.pack(pady=10)

    def submit(self):
        name = self.name.get()
        difficulty = creativity = safety = flow = overall = 0.0
        for i, entry in enumerate(self.entries):
            score = entry.get_score()
            try:
                score = float(score)
            except ValueError:
                score = 0.0
            if i == 0:
                difficulty = score
            elif i == 1:
                creativity = score
            elif i == 2:
                safety = score
            elif i == 3:
                flow = score
            elif i == 4:
                overall = score
        total_score = difficulty + creativity + safety + flow + overall
        with open("scores.txt", "a") as f:
            f.write(f"{name},{int(total_score)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500+0+0")
    app = Application(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
