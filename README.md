# Automated File Scanner, Compressor, Cleaner, and Uploader

This project automates the process of scanning directories for specific file types, compressing them into a zip file, cleaning up the original files, and uploading the compressed file to Dropbox.

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
4. **Upload the compressed file** to a specified Dropbox folder.

---

## Features

- Scans multiple directories with configurable extensions.
- Compresses files with high compression using the `zipfile` module.
- Deletes the original files post-compression.
- Uploads the zip file to Dropbox.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
