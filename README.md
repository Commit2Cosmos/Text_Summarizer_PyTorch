# Text_Summarizer_PyTorch

This project aims to build a text summarizer with frontend using PyTorch and Hugging Face.



## TODO

- Write unit tests for **Data Transformation** and **Model Evaluation** pipeline
- Change training + evaluation components to work with multiple datasets (dynamic saving file paths etc)
- Add `num_beams` to config file
- Freeze the last layer to test training and evaluation pipelines
- Resolve `Some non-default generation parameters are set in the model config. These should go into a GenerationConfig file`

- Raise issue of the incorrect warning about that model needs to be trained because of newly initialised encoding layers


## Milestones

- [x] Choose and download the pre-trained model and dataset for transfer learning
- [x] Build pipelines (listed below)
- [ ] Check for transfer learning or **fine-tuning** (Untrained layers are already provided, so just train them -> update training pipeline)
- [ ] Model packaging (serialisation, containerisation) -> Docker
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
- [x] Model Evaluation
- [ ] Model Inference



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