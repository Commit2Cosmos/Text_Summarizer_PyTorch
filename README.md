# Text_Summarizer_PyTorch

This project aims to build a text summarizer with frontend using PyTorch and Hugging Face.



## TODO

- Write unit tests for **Data Transformation** pipeline



## Milestones

- [x] Choose and download the pre-trained model and dataset for transfer learning
- [ ] Build pipelines (listed below)
- [ ] Fine-tune the model
- [ ] Model packaging (serialisation, containerisation)
- [ ] Choose deployment strategy (cloud or local) and interaction type (API, **webapp**, cli, embedded systems)
- [ ] Build + deploy the webapp
- [ ] Deploy the model (one-off)
- [ ] Support for multiple datasets
- [ ] Add output text size control feature
- [ ] Add context area for user defined personalisations
- [ ] Add support for pdf (and other) files (multimodality)



## Pipelines

- [x] Data Ingestion
- [x] Data Validation
- [x] Data Transformation + Feature Engineering
- [x] Model Training
- [ ] Model Evaluation



## Workflow (Files to update)

See [architecture](./architecture/architecture.excalidraw) file for detailed breakdown of the project's architecture and what each file does.

- `logging.py`
- `pyproject.toml`
- `params.json`

- `config.json`
- `src/entity`
- `src/config`
- `src/components`
- `src/pipeline`
- `main.py`
- `app.py`