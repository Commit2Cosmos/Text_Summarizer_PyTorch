from google.cloud import aiplatform



job = aiplatform.CustomContainerTrainingJob(
    display_name="text_summarizer_test",
    container_uri="gcr.io/upheld-rain-429509-n1/text-summarizer",
    staging_bucket="gs://text_sumarizer_test_bucket",
    location="europe-west2",
)

model = job.run()