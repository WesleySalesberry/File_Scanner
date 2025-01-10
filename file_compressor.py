import zipfile
import logging
from pathlib import Path
from typing import List, Optional


class FileCompressor:
    def __init__(self, output_dir: Optional[str] = None, zip_name: str = "zipped_files"):
        """
        Initialize the FileCompressor with output directory and zip file name.

        :param output_dir: Directory to save the zip file. Defaults to Desktop.
        :param zip_name: Name of the zip file. Defaults to 'zipped_files'.
        """
        self.output_dir = Path(output_dir or (Path.home() / "Desktop"))
        self.zip_name = zip_name
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def zip_files(self, files: List[Path]) -> Path:
        """
        Compress the provided files into a zip file using maximum compression.

        :param files: List of Path objects to compress.
        :return: Path to the created zip file.
        """
        zip_file_path = self.output_dir / f"{self.zip_name}.zip"

        if zip_file_path.exists():
            logging.warning(f"{zip_file_path} already exists and will be overwritten.")

        try:
            with zipfile.ZipFile(zip_file_path, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
                for file in files:
                    try:
                        # Ensure unique paths by prepending the parent directory name
                        unique_name = str(file.parent.name) + "_" + file.name
                        zipf.write(file, arcname=unique_name)
                    except Exception as e:
                        logging.error(f"Error adding file {file}: {e}")
            logging.info(f"Files successfully zipped to {zip_file_path}")
        except Exception as e:
            logging.error(f"Error zipping files: {e}")

        return zip_file_path