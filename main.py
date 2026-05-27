import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


BG = "#0a0f1d"
CARD = "#111a2e"
CARD2 = "#0b1220"
TEXT = "#e5e7eb"
MUTED = "#94a3b8"

GREEN = "#22c55e"
RED = "#ef4444"
BLUE = "#3b82f6"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GTA V Mod Manager")
        self.root.geometry("860x500")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.gta_path = tk.StringVar()
        self.mods_path = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root,
            text="GTA V MOD MANAGER",
            bg=BG,
            fg=TEXT,
            font=("Helvetica", 22, "bold")
        ).pack(pady=18)

        self.card = tk.Frame(self.root, bg=CARD)
        self.card.pack(fill="both", expand=True, padx=30, pady=20)

        self.section("GTA V Folder", self.gta_path, self.pick_gta)
        self.section("Mods Folder", self.mods_path, self.pick_mods)

        btns = tk.Frame(self.card, bg=CARD)
        btns.pack(fill="x", pady=25)

        tk.Button(
            btns, text="INSTALL MODS",
            bg=GREEN, fg="white",
            bd=0, font=("Helvetica", 12, "bold"),
            command=self.install
        ).pack(side="left", expand=True, fill="x", padx=8, ipady=10)

        tk.Button(
            btns, text="REMOVE MODS",
            bg=RED, fg="white",
            bd=0, font=("Helvetica", 12, "bold"),
            command=self.remove
        ).pack(side="left", expand=True, fill="x", padx=8, ipady=10)

        self.status = tk.Label(
            self.root,
            text="Ready",
            bg=BG,
            fg=MUTED,
            font=("Helvetica", 10)
        )
        self.status.pack(pady=(0, 10))

    def section(self, title, var, cmd):
        tk.Label(
            self.card,
            text=title,
            bg=CARD,
            fg=TEXT,
            font=("Helvetica", 11, "bold")
        ).pack(anchor="w", padx=15, pady=(12, 5))

        row = tk.Frame(self.card, bg=CARD)
        row.pack(fill="x", padx=15)

        tk.Entry(
            row,
            textvariable=var,
            bg=CARD2,
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Helvetica", 11)
        ).pack(side="left", fill="x", expand=True, ipady=10)

        tk.Button(
            row,
            text="Browse",
            bg=BLUE,
            fg="white",
            bd=0,
            command=cmd
        ).pack(side="left", padx=10)

    def pick_gta(self):
        path = filedialog.askdirectory()
        if path:
            self.gta_path.set(path)

    def pick_mods(self):
        path = filedialog.askdirectory()
        if path:
            self.mods_path.set(path)

    # ================= INSTALL =================

    def install(self):
        gta = self.gta_path.get()
        mods = self.mods_path.get()

        if not gta or not mods:
            messagebox.showerror("Error", "Select both folders")
            return

        files = 0
        folders_set = set()

        for current_dir, _, filenames in os.walk(mods):
            rel = os.path.relpath(current_dir, mods)

            # NIE LICZ ROOT
            if rel == ".":
                rel = ""

            target_dir = os.path.join(gta, rel)

            folders_set.add(target_dir)
            os.makedirs(target_dir, exist_ok=True)

            for file in filenames:
                src = os.path.join(current_dir, file)
                dst = os.path.join(target_dir, file)

                try:
                    shutil.copyfile(src, dst)
                    files += 1
                except Exception as e:
                    print(f"Copy error: {e}")

        # ✔️ FIX KLUCZOWY
        folders = len(folders_set) - 1  # odejmujemy root GTA

        self.status.config(text=f"Installed: {files} files, {folders} folders")

        messagebox.showinfo(
            "Done",
            f"Installed\nFiles: {files}\nFolders: {folders}"
        )

    # ================= REMOVE =================

    def remove(self):
        gta = self.gta_path.get()
        mods = self.mods_path.get()

        if not gta or not mods:
            messagebox.showerror("Error", "Select both folders")
            return

        removed_files = 0

        # usuwanie plików modów tylko jeśli istnieją w GTA
        for current_dir, _, filenames in os.walk(mods):
            rel = os.path.relpath(current_dir, mods)
            target_dir = os.path.join(gta, rel)

            for file in filenames:
                path = os.path.join(target_dir, file)

                if os.path.isfile(path):
                    try:
                        os.remove(path)
                        removed_files += 1
                    except OSError as e:
                        print(f"Remove file error: {path}: {e}")

        # usuwanie pustych folderów
        removed_folders = 0

        for current_dir, _, _ in os.walk(gta, topdown=False):
            if current_dir == gta:
                continue

            try:
                if os.path.isdir(current_dir) and not os.listdir(current_dir):
                    os.rmdir(current_dir)
                    removed_folders += 1
            except OSError as e:
                print(f"Remove folder error: {current_dir}: {e}")

        self.status.config(
            text=f"Removed: {removed_files} files, {removed_folders} folders"
        )

        messagebox.showinfo(
            "Done",
            f"Removed\nFiles: {removed_files}\nFolders: {removed_folders}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()