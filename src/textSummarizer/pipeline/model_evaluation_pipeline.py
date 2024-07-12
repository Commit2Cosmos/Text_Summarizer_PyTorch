from textSummarizer.config.configuration import ConfigManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.entity import Pipeline



class ModelEvaluationPipeline(Pipeline):
    def __init__(self):
        self.name = "Model Evaluation Pipeline"
    
    def main(self):
        config = ConfigManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()