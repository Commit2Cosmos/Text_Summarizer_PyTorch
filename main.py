from textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline

from textSummarizer.utils.common import run_pipeline

#* Add more pipelines here
data_ingestion_pipeline = DataIngestionPipeline()


pipelines = [data_ingestion_pipeline]
    

if __name__ == "__main__":
    for pipeline in pipelines:
        run_pipeline(pipeline)