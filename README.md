# Automated File Scanner, Compressor, Cleaner, and Uploader

This project automates the process of scanning directories for specific file types, compressing them into a zip file, cleaning up the original files, and uploading the compressed file to Dropbox.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project consists of Python scripts that work together to:

1. **Scan directories** for files matching specified extensions.
2. **Compress the files** into a zip archive.
3. **Clean up the original files** from the system.
4. **Upload the compressed file** to Dropbox.

---

## Features

- Scans multiple directories with configurable file extensions.
- Compresses files with high efficiency using the `zipfile` module.
- Deletes the original files after compression.
- Uploads the zip file to a Dropbox folder.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install dependencies:
    - Ensure Python 3.7 or higher is installed.
    - Install the Dropbox Python SDK
   ```bash
   pip install dropbox
   ```

3. Ensure the following files are in the project directory:
   ```bash
   - main.py
   - dropbox_uploader.py
   - file_scanner.py
   - file_compressor.py
   - file_cleaner.py
   ```

4. Obtain a valid Dropbox API access token. You can generate one from the Dropbox App Console.


## Usage

1. Open the main.py file and replace the placeholder access_token with your Dropbox API access token:
```bash
dropbox_uploader = DropboxUploader(access_token="your-access-token")
```

2. Run the main.py script:
```bash
python main.py
```

3. Monitor the console logs for updates and any potential issues.
