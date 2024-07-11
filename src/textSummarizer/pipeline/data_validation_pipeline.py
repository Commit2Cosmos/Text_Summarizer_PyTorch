from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.entity import Pipeline



class DataValidationPipeline(Pipeline):
    def __init__(self):
        self.name = "Data Validation Pipeline"
    
    def main(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_validation_config)
        data_ingestion.validate_files_exist()