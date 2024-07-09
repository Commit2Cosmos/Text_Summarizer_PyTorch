# Text_Summarizer_PyTorch

This project aims to build a text summarizer with frontend using PyTorch and Hugging Face.


## Workflow

See [architecture](./architecture/architecture.excalidraw) file for detailed breakdown of the project's architecture and what each file does.

- [x] `logging.py`
- [x] `pyproject.toml`

- [ ] `config.json`
- [ ] `params.json`
- [ ] `src/entity`
- [ ] `src/config`
- [ ] `src/components`
- [ ] `src/pipeline`
- [ ] `main.py`
- [ ] `app.py`


## Milestones

- [x] Choose and download the pre-trained model and dataset for transfer learning
- [ ] Fine-tune the model
- [ ] Model packaging (serialisation, containerisation)
- [ ] Choose deployment strategy (cloud or local) and interaction type (API, **webapp**, cli, embedded systems)
- [ ] Build + deploy the webapp
- [ ] Deploy the model (one-off)
- [ ] Add output text size control feature
- [ ] Add context area for user defined personalisations
- [ ] Add support for pdf (and other) files (multimodality)