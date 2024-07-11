from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from textSummarizer.pipeline.data_validation_pipeline import DataValidationPipeline

from textSummarizer.utils.common import run_pipeline

#* Add more pipelines here
data_ingestion_pipeline = DataIngestionPipeline()
data_validation_pipeline = DataValidationPipeline()


pipelines = [data_ingestion_pipeline, data_validation_pipeline]
    

if __name__ == "__main__":
    for pipeline in pipelines:
        run_pipeline(pipeline)