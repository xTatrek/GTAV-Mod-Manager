# 🚗 GTA V Mod Manager

## ⚙️ How it works

This mod manager works by directly copying and synchronizing files between your **Mods folder** and your **GTA V installation directory**.

### 📥 Installation
- Files and folders from your Mods directory are copied into the GTA V directory
- Existing files are overwritten if they match the same path
- The folder structure is preserved exactly as in the Mods folder

### 🧹 Removal
- The tool scans your Mods folder structure
- It removes only files from GTA V that also exist in your Mods folder
- It does NOT touch any vanilla GTA V files that are not part of mods
- After removal, empty folders are cleaned up automatically

---

## 🧠 Important Logic

- Only matching file paths between Mods and GTA V are affected
- No random or full-folder deletion is performed
- Vanilla game files remain untouched unless they were replaced by mods

---

A simple and lightweight **mod manager for Grand Theft Auto V** built with Python and Tkinter.  
Easily install and remove mods with a clean and user-friendly interface.

---

## ✨ Features

- 📁 Select GTA V game folder
- 📦 Select mods folder
- ⚡ One-click mod installation
- 🧹 One-click mod removal
- 📊 Live status updates
- 🖥️ Simple and clean UI
- 🔒 Safe file handling (no external dependencies)

---

## 🚀 How to Use

### ⚠️ Notes
- Always run as administrator if GTA V is installed in protected folders
- Make sure you select correct directories
- It is recommended to backup your game before installing mods

---

### 🪟 Windows (Recommended)

1. Go to the **Releases** page of this repository  
2. Download the latest version:
   - `GTA V Mod_Manager.exe`

3. Run the application:
   - Double-click the `.exe` file

4. In the app:
   - Select your **GTA V folder**
   - Select your **Mods folder**
   - Click:
     - ⚡ **INSTALL MODS** to install mods
     - 🧹 **REMOVE MODS** to uninstall mods

---

### 📦 Alternative (Python version)

If you want to run from source:

```bash
git clone https://github.com/xTatrek/GTAV-Mod-Manager.git
cd GTAV-Mod-Manager
python main.py
