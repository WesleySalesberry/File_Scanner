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

1. Open the `main.py` file and replace the placeholder access_token with your Dropbox API access token:
```bash
dropbox_uploader = DropboxUploader(access_token="your-access-token")
```

2. Run the main.py script:
```bash
python main.py
```

3. Monitor the console logs for updates and any potential issues.


## Modules

### `main.py`
- Orchestrates the overall workflow:
  <ul>
    <li>Scans directories for files matching specific extensions.</li>
    <li>Compresses the files into a zip archive.</li>
    <li>Cleans up the original files.</li>
    <li>Uploads the zip file to Dropbox.</li>
  </ul>

### `file_scanner.py`
- Scans directories for files matching specified extensions.
  <ul>
    <li>Uses multi-threading for faster directory traversal.</li>
    <li>Filters files based on a list of extensions.</li>
  </ul>

### `file_compressor.py`
- Compresses files into a zip archive.
  <ul>
    <li>Applies maximum compression using the `zipfile` module.</li>
    <li>Ensures unique file names in the archive to avoid overwriting.</li>
  </ul>

### `file_cleaner.py`
- Deletes files from the filesystem after compression.
  <ul>
    <li>Handles errors, such as permission issues, gracefully.</li>
    <li>Logs the status of each deletion.</li>
  </ul>

### `dropbox_uploader.py`
- Uploads the compressed zip file to Dropbox.
  <ul>
    <li>Uses the Dropbox Python SDK.</li>
    <li>Requires a valid Dropbox API access token.</li>
    <li>Uploads files to a specified Dropbox folder.</li>
  </ul>


## Logging

- Logs are configured in the main.py file and provide detailed information about the process:

<ul>
    <li>INFO: General progress updates.</li>
    <li>WARNING: Non-critical issues (e.g., file overwrite warnings).</li>
    <li>ERROR: Critical issues (e.g., permission errors, failed uploads).</li>
</ul>

- You can customize logging settings in the `logging.basicConfig` configuration in `main.py`


## License
- This project is licensed under the MIT License.
