# File Organizer Script Documentation

The "File Organizer" script is a Python program designed to organise files in a specified folder based on their file extensions into separate folders.

## Usage

1. Get a copy of the FileOrganiser.py
2. Open a terminal or command prompt.
3. Navigate to the directory where the Python script is located.
4. Run the script using the command: `python FileOrganizer.py`

## Code Explanation

The script consists of the following sections:

### Importing Required Modules

```python
import os
import shutil
```
In this section, we import two Python modules:

* `os`: This module provides a way to interact with the operating system, enabling file and directory-related operations.
* `shutil`: This module offers high-level file operations like moving files, copying files, etc.
## File Extensions

```python
audio = ('.mp3', '.flac', '.wav')
video = ('.mp4', '.mov')
img = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
docs = ('.doc', '.docx', '.pdf', '.rtf', '.txt')
```

