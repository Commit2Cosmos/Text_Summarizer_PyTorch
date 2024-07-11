import os
import zipfile
import urllib.request as request
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size_of_folder, create_directories


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_data(self):
        for (ds, url) in self.config.datasets.items():
            if not os.path.exists(os.path.join(self.config.root_dir, ds)):
                create_directories([os.path.join(self.config.root_dir, ds)])
                try:
                    
                    filename, headers = request.urlretrieve(
                        url = url,
                        filename=os.path.join(self.config.root_dir, ds, 'data.zip'),
                    )
                    logger.info(f"{filename} downloaded with headers: {headers}")

                except Exception as e:
                    logger.error(f"Error in download_data: {e}")
            else:
                logger.info(f'Data folder already exists, folder size: {get_size_of_folder(os.path.join(self.config.root_dir, ds))}')


    def extract_zip_files(self):
        for ds in self.config.datasets:
            zip_path = os.path.join(self.config.root_dir, ds, "data.zip")

            if os.path.exists(zip_path):
                logger.info(f"Extraction of {zip_path} has begun")
                with zipfile.ZipFile(os.path.join(self.config.root_dir, ds, "data.zip"), 'r') as zip_ref:
                    zip_ref.extractall(self.config.root_dir)

                logger.info(f"Unzipped file {zip_path}, deleting the zip file")

                #* delete the zip file after unzipping
                os.remove(os.path.join(self.config.root_dir, ds, "data.zip"))
