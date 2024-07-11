from textSummarizer.utils.common import read_json, create_directories
from textSummarizer.constants import *
from textSummarizer.entity import *


class ConfigManager:
    def __init__(self):
        self.config = read_json(path_to_json=CONFIG_FILE_PATH)
        self.params = read_json(path_to_json=PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        datasets = self.config.datasets

        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            datasets=datasets,
        )
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        datasets = self.config.datasets
        data_folder = self.config.data_ingestion.root_dir

        return DataValidationConfig(
            dataset_folder=Path(data_folder),
            datasets=datasets,
            required_folders=config.required_folders,
            required_files=config.required_files
        )