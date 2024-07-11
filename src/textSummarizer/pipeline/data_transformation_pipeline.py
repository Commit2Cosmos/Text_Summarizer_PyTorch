from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.entity import Pipeline



class DataTransformationPipeline(Pipeline):
    def __init__(self):
        self.name = "Data Transformation Pipeline"
    
    def main(self):
        config = ConfigManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.save_features()