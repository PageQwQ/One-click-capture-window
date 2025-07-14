import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk

class ModernWindowResizer:
    def __init__(self, root):
        self.root = root
        self.root.title("OCCW")

        sv_ttk.set_theme("light")

        def validate_input(new_value):
            if new_value == "":
                return True
            try:
                int(new_value)
                return True
            except ValueError:
                return False

        self.validate_cmd = self.root.register(validate_input)

        self.main_frame = ttk.Frame(root, padding="30")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        title_label = ttk.Label(self.main_frame, text="One-Click capture window", font=("Microsoft YaHei UI", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 25), sticky="nsew")

        input_frame = ttk.Frame(self.main_frame, padding="15")
        input_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        input_frame.grid_columnconfigure(1, weight=1)

        width_label = ttk.Label(input_frame, text="Width:", font=("Microsoft YaHei UI", 10))
        width_label.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="w")
        
        self.width_var = tk.IntVar(value=320)
        self.width_entry = ttk.Entry(input_frame, textvariable=self.width_var, width=10, validate="key", validatecommand=(self.validate_cmd, '%P'))
        self.width_entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

        self.width_scale = ttk.Scale(input_frame, from_=100, to=1920, variable=self.width_var, orient="horizontal", command=lambda v: self.width_var.set(int(float(v))))
        self.width_scale.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 15), sticky="ew")

        height_label = ttk.Label(input_frame, text="Height:", font=("Microsoft YaHei UI", 10))
        height_label.grid(row=2, column=0, padx=(0, 10), pady=10, sticky="w")
        
        self.height_var = tk.IntVar(value=360)
        self.height_entry = ttk.Entry(input_frame, textvariable=self.height_var, width=10, validate="key", validatecommand=(self.validate_cmd, '%P'))
        self.height_entry.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

        self.height_scale = ttk.Scale(input_frame, from_=100, to=1080, variable=self.height_var, orient="horizontal", command=lambda v: self.height_var.set(int(float(v))))
        self.height_scale.grid(row=3, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="ew")

        self.status_label = ttk.Label(self.main_frame, text="Status:", font=("Microsoft YaHei UI", 10))
        self.status_label.grid(row=2, column=0, pady=20, sticky="nsew")

        self.width_var.trace_add("write", self.resize_window)
        self.height_var.trace_add("write", self.resize_window)

        self.resize_window()
        
        self.resize_window()
        
        self.status_label = ttk.Label(
            self.main_frame, 
            text="Current size: 320x360", 
            font=("Microsoft YaHei UI", 9)
        )
        self.status_label.grid(row=3, column=0, columnspan=2, pady=(0, 20), sticky="nsew")

    def resize_window(self, *args):
        try:
            width = self.width_var.get()
            height = self.height_var.get()
            if width > 0 and height > 0:
                self.root.geometry(f"{width}x{height}")
                self.status_label.config(text=f"Current size: {width}x{height}")
            else:
                self.status_label.config(text="Width and height must be positive")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernWindowResizer(root)
    root.mainloop()
