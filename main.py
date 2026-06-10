import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pillow_heif
import os

# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()

class HEICConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HEIC to JPG Converter")
        self.root.geometry("400x250")
        self.root.iconbitmap("C:/Users/Alfonso Vecino/Documents/CODING/Icons/av.ico")
        
        self.file_paths = []

        # UI Elements
        self.label_title = tk.Label(root, text="Select *.HEIC files to convert to *.JPG", pady=20)
        self.label_title.pack()

        self.select_btn = tk.Button(root, text="Select Files", command=self.select_files, width=20)
        self.select_btn.pack(pady=5)

        self.convert_btn = tk.Button(root, text="Convert to JPG", command=self.convert_files, 
                                     state=tk.DISABLED, bg="red", fg="blue", disabledforeground="white", width=20)
        self.convert_btn.pack(pady=5)

        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=10)

        self.label = tk.Label(root, text="No files selected.", pady=5)
        self.label.pack()

        self.label_develop = tk.Label(root, text="Developed by Alfonso Vecino - 2026.", pady=10)
        self.label_develop.pack()

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames(
            title="Select HEIC files",
            filetypes=[("HEIC files", "*.heic"), ("All files", "*.*")]
        )
        
        if self.file_paths:
            self.label.config(text=f"{len(self.file_paths)} files selected")
            self.convert_btn.config(state=tk.NORMAL)
        else:
            self.label.config(text="No files selected.")
            self.convert_btn.config(state=tk.DISABLED)

    def convert_files(self):
        if not self.file_paths:
            return

        output_dir = filedialog.askdirectory(title="Select Output Folder")
        if not output_dir:
            return

        count = 0
        for path in self.file_paths:
            try:
                # Open the HEIC file
                image = Image.open(path)
                
                # Prepare the new filename
                base_name = os.path.basename(path)
                file_name = os.path.splitext(base_name)[0] + ".jpg"
                save_path = os.path.join(output_dir, file_name)
                
                # Convert and Save
                image.save(save_path, "JPEG", quality=100)
                count += 1
                self.status_label.config(text=f"Converting: {count}/{len(self.file_paths)}")
                self.root.update_idletasks()
                
            except Exception as e:
                print(f"Error converting {path}: {e}")

        messagebox.showinfo("Success", f"Converted {count} files successfully!")
        self.status_label.config(text="Done!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HEICConverterApp(root)
    root.mainloop()