from textSummarizer.utils.common import read_json, create_directories
from textSummarizer.constants import *
from textSummarizer.entity import DataIngestionConfig


class ConfigManager:
    def __init__(self) -> None:
        self.config = read_json(path_to_json=CONFIG_FILE_PATH)
        self.params = read_json(path_to_json=PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )