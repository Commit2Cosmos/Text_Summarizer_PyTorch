from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.model_training import ModelTraining
from textSummarizer.entity import Pipeline



class ModelTrainingPipeline(Pipeline):
    def __init__(self):
        self.name = "Model Training Pipeline"
    
    def main(self):
        config = ConfigManager()
        model_training_config = config.get_model_training_config()
        model_training = ModelTraining(config=model_training_config)
        model_training.train()