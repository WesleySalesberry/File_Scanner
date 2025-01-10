import logging
from pathlib import Path
from typing import List

class FileCleaner:
    def __init__(self):
        """Initialize the FileCleaner."""
        pass

    def delete_files(self, files: List[Path]) -> None:
        """
        Delete the provided files from the filesystem.

        :param files: List of Path objects to delete.
        """
        logging.info("***** Deleting Files *****")
        for file in files:
            try:
                if file.exists():
                    file.unlink()  # Removes the file
                    logging.info(f"Deleted file: {file}")
                else:
                    logging.warning(f"File no longer exists, skipping deletion: {file}")
            except PermissionError:
                logging.error(f"Permission denied: {file}. Could not delete.")
            except Exception as e:
                logging.error(f"Error deleting {file}: {e}")