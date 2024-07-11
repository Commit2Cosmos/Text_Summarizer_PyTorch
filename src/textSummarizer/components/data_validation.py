import os
import glob
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_files_exist(self):
        try:
            if sorted(os.listdir(self.config.dataset_folder)) != sorted(self.config.datasets):
                raise Exception(f"Datasets in config and dataset folder don't match!")
            
            for ds in self.config.datasets:

                ds_path = os.path.join(self.config.dataset_folder, ds)

                folders_inside_dataset = os.listdir(ds_path)

                if not all(f in folders_inside_dataset for f in self.config.required_folders):
                    raise Exception(f"Dataset {ds} is missing one or more required folders: {self.config.required_folders}")

                for folder in self.config.required_folders:
                    for file in self.config.required_files:
                        if not glob.glob(os.path.join(ds_path, folder, file)):
                            raise Exception(f"Folder {folder} is missing one or more required files: {self.config.required_files}")


            logger.info(f"Dataset files have been validated!")

        except Exception as e:
            logger.error(f"Error in validate_files_exist: {e}")
