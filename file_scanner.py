import os
import logging
from pathlib import Path
from typing import List, Optional


class FileScanner:
    def __init__(self, extensions: Optional[List[str]] = None):
        """
        Initialize the FileScanner with file extensions to filter by.

        :param extensions: List of file extensions to scan for (e.g., ['.txt', '.csv']).
                          Defaults to ['.csv', '.txt'].
        """
        self.extensions = [ext.lower() for ext in (extensions or ['.csv', '.txt'])]

    def scan_directory(self, target_dir: str) -> List[Path]:
        """
        Scan a single directory for files matching the given extensions.

        :param target_dir: Path to the directory to scan.
        :return: List of matching file paths.
        """
        files = []
        try:
            for root, dirs, filenames in os.walk(target_dir):
                # Skip system directories (e.g., node_modules, .git)
                dirs[:] = [d for d in dirs if not d.startswith(('.', 'node_modules', '.git'))]
                for filename in filenames:
                    if any(filename.lower().endswith(ext) for ext in self.extensions):
                        files.append(Path(root) / filename)
        except PermissionError as e:
            logging.error(f"Permission error while accessing {target_dir}: {e}")
        except Exception as err:
            logging.error(f"Error scanning {target_dir}: {err}")
        return files

    def scan_directories(self, target_dirs: List[str]) -> List[Path]:
        """
        Scan multiple directories for files matching the given extensions.

        :param target_dirs: List of directory paths to scan.
        :return: List of matching file paths.
        """
        from concurrent.futures import ThreadPoolExecutor

        files = []
        with ThreadPoolExecutor() as executor:
            results = executor.map(self.scan_directory, target_dirs)
            for result in results:
                files.extend(result)

        return files
