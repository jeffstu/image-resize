# image-resize
# Instructions for Using the Image resize Script

## Prerequisites:
1. **Python:** The script requires Python to be installed.
2. **Pillow:** A Python Imaging Library that adds image processing capabilities.

## Installing Python and Pillow
### Windows:
1. **Installing Python:**
   - Download from [Python.org](https://www.python.org/).
   - Ensure to check “Add Python 3.x to PATH” during installation.
   - Verify installation: `python --version` in Command Prompt.

2. **Installing Pillow:**
   - In Command Prompt: `pip install Pillow`.

### macOS:
1. **Installing Python:**
   - Pre-installed but can check/update version: `python3 --version` in Terminal.
   - Alternatively, use [Homebrew](https://brew.sh/): `brew install python`.

2. **Installing Pillow:**
   - In Terminal: `pip3 install Pillow`.

## Running the Script
1. **Prepare Your Images:**
   - Store all images in one folder (e.g., `MyImages`).
   
2. **Save the Script:**
   - Save the script as `.py` (e.g., `re-size-images.py`).

3. **Using the Command Line/Terminal:**
   - Navigate to the script folder.
   - Command to run script (replace `MyImages` with your image folder name):
     - Windows: `python re-size-images.py c:\Users\yourusername\MyImages`
     - macOS: `python3 image_processing.py /Users/yourusername/MyImages`

## Notes
- Keep backups of original images.
- Processed images will appear in new folders: `web_sized` and `PurplePort_sized`.

## Troubleshooting
- Issues with `pip` or `pip3`? Ensure it's installed/updated.
- Permission errors? Try: `pip install --user Pillow` (or `pip3` on macOS).
- Ensure sufficient disk space for new images.
- Check terminal output for errors or alerts.

