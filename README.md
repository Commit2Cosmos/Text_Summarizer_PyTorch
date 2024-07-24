# Text_Summarizer_PyTorch

This project aims to build a text summarizer with frontend using PyTorch and Hugging Face.


## Instructions to use

- Pull the [image](https://hub.docker.com/repository/docker/antonbeloval08/text-summarizer/) from DockerHub:
    ```console
    docker pull antonbeloval08/text-summarizer
    ```

OR

- Build the image yourself:
    ```console
    git clone https://github.com/Commit2Cosmos/Text_Summarizer_PyTorch.git
    docker build --no-cache -t text-summarizer .
    ```


- Create a container:
    ```console
    docker run --name text-sumarizer-test -p 8000:8000 text-summarizer
    ```

- Visit the webapp: [http://0.0.0.0:8000](http://0.0.0.0:8000)


- **To train:** Click on the "Training" section, press "Try it out" and press "Execute"

- **To summarize:** Click on the "Inference" section, press "Try it out", enter the text you want summarized and press "Execute"




-------------------------- **DEV NOTES** --------------------------

## TODO

- Add ability to control parameters in params.json in the web app
- Change training + evaluation components to work with multiple datasets (dynamic saving file paths etc)
- Resolve `Some non-default generation parameters are set in the model config. These should go into a GenerationConfig file`

- Raise issue of the incorrect warning about that model needs to be trained because of newly initialised encoding layers


## Milestones

- [x] Choose and download the pre-trained model and dataset for transfer learning
- [x] Build pipelines (listed below)
- [x] Check for transfer learning or **fine-tuning** (Untrained layers are already provided, so just train them -> update training pipeline)
- [x] Model packaging (serialisation, containerisation) -> Docker
- [x] Choose deployment strategy (cloud or local) and interaction type (API, **webapp**, cli, embedded systems)
- [ ] Train the model with VertexAI (separate data and model -> don't use the container) and upload trained weights

**(Optional):**

- [ ] Build + deploy custom webapp
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
- [x] Model Inference



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