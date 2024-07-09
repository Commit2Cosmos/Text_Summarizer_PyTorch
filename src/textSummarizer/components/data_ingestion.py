import os
import io
import zipfile
import requests
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size_of_file


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_extract_data(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                response = requests.get(self.config.source_URL)
                if response.status_code == 200:
                    with io.BytesIO(response.content) as buffer:
                        logger.info(f'Data downloaded with info: {response.headers}')
                        with zipfile.ZipFile(buffer) as zip_ref:
                            zip_ref.extractall(self.config.unzip_dir)
                            logger.info(f'Data unzipped, file size: {get_size_of_file(self.config.local_data_file)}')
                else:
                    logger.error("Could not download data")
                    raise Exception()
            except Exception as e:
                logger.error(f"Error in download_data: {e}")
        else:
            logger.info(f'Data file already exists, file size: {get_size_of_file(self.config.local_data_file)}')