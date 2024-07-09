from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.data_ingestion import DataIngestion



class DataIngestionPipeline:
    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_extract_data()