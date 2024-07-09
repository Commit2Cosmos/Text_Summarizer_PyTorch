import os
import zipfile
import urllib.request as request
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size_of_file


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file
                )
                logger.info(f"{filename} downloaded with encoding: {headers['Content-Encoding']}")

            except Exception as e:
                logger.error(f"Error in download_data: {e}")
        else:
            logger.info(f'Data file already exists, file size: {get_size_of_file(self.config.local_data_file)}')


    def extract_zip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)

        #* delete the zip file after unzipping
        os.remove(self.config.local_data_file)
