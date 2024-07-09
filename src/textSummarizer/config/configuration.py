from textSummarizer.utils.common import read_json, create_directories
from textSummarizer.constants import *
from textSummarizer.entity import DataIngestionConfig


class ConfigManager:
    def __init__(self) -> None:
        self.config = read_json(file_path=CONFIG_FILE_PATH)
        self.params = read_json(file_path=PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )