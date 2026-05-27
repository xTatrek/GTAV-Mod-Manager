# 🚗 GTA V Mod Manager

A simple and lightweight **mod installer/remover for Grand Theft Auto V** built with Python and Tkinter.  
It helps you quickly copy mods into your game folder and remove them safely based on folder structure matching.

---

## ⚙️ How it works

This tool manages GTA V mods using **file path matching between your Mods folder and GTA V directory**.

### 📥 Installation
- Copies all files from the Mods folder into your GTA V directory
- Preserves the folder structure exactly as in the Mods folder
- Overwrites files in GTA V if they already exist at the same path

### 🧹 Removal
- Scans the Mods folder structure
- Removes files from GTA V only if they exist at the same relative path
- Does NOT touch files that are not part of the Mods folder structure
- Removes empty folders after uninstalling mods

---

## 🧠 Important Notes

- ❗ This is NOT a full synchronization system (not yet)
- ❗ It does NOT track original GTA V files
- ❗ It only matches files based on folder paths

Always make a backup of your GTA V directory before using mods.

---

## ✨ Features

- 📁 Select GTA V game folder
- 📦 Select mods folder
- ⚡ One-click mod installation
- 🧹 One-click mod removal
- 📊 Live status updates
- 🖥️ Clean and simple UI
- 🔒 No external dependencies

---

## 🚀 How to Use

### 🪟 Windows (Recommended)

1. Go to the **Releases** page of this repository  
2. Download the latest version:
   - `GTA_V_Mod_Manager.exe`

3. Run the application:
   - Double-click the `.exe` file

4. In the app:
   - Select your **GTA V folder**
   - Select your **Mods folder**
   - Click:
     - ⚡ **INSTALL MODS** to install mods
     - 🧹 **REMOVE MODS** to uninstall mods

---

### 📦 Run from source (Python)

```bash
git clone https://github.com/xTatrek/GTAV-Mod-Manager.git
cd GTAV-Mod-Manager
python main.py
