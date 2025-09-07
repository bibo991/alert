import requests
import subprocess
import os

# URL to download the latest AutoHotkey installer (64-bit version)
installer_url = "https://www.autohotkey.com/download/ahk-v2.exe"  # Replace with the correct URL if needed

# Path to save the installer (in the user's temporary directory)
installer_path = os.path.join(os.path.expanduser("~"), "Downloads", "ahk-installer.exe")

# Download the AHK installer
response = requests.get(installer_url)
if response.status_code == 200:
    with open(installer_path, 'wb') as f:
        f.write(response.content)

    # Run the installer silently (no user interaction)
    subprocess.run([installer_path, "/S"], check=True)

    # Optionally, delete the installer after installation
    os.remove(installer_path)
