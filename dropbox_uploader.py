import dropbox
import logging
from pathlib import Path


class DropboxUploader:
    def __init__(self, access_token: str):
        """
        Initialize the DropboxUploader with an access token.

        :param access_token: Dropbox API access token.
        """
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, local_path: str, dropbox_folder: str = "/ZippedFiles") -> None:
        """
                Upload a file to a specific folder in Dropbox.

                :param local_path: Path to the local file to upload.
                :param dropbox_folder: Dropbox folder where the file will be uploaded.
                """
        try:
            # Ensure the Dropbox folder path ends with a slash
            if not dropbox_folder.endswith('/'):
                dropbox_folder += '/'

            # Get the file name and create the full Dropbox path
            file_name = Path(local_path).name
            dropbox_path = f"{dropbox_folder}{file_name}"

            with open(local_path, "rb") as f:
                self.dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))

            logging.info(f"File uploaded to Dropbox: {dropbox_path}")
        except dropbox.exceptions.ApiError as e:
            logging.error(f"Error uploading file to Dropbox: {e}")
            raise