from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.entity import Pipeline



class DataIngestionPipeline(Pipeline):
    def __init__(self):
        self.name = "Data Ingestion Pipeline"
    
    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_files()