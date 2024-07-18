from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline
from textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from textSummarizer.pipeline.model_training_pipeline import ModelTrainingPipeline
from textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

from textSummarizer.utils.common import run_pipeline

#* <<< Add more pipelines here >>>
data_ingestion_pipeline = DataIngestionPipeline()
data_validation_pipeline = DataValidationPipeline()
data_transformation_pipeline = DataTransformationPipeline()
model_training_pipeline = ModelTrainingPipeline()
model_evaluation_pipeline = ModelEvaluationPipeline()


pipelines = [data_ingestion_pipeline, data_validation_pipeline, data_transformation_pipeline, model_training_pipeline, model_evaluation_pipeline]


if __name__ == "__main__":
    for pipeline in pipelines:
        run_pipeline(pipeline)