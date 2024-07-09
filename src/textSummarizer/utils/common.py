import os
import json
import time
from textSummarizer.logging import logger
from textSummarizer.entity import Pipeline
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import List


@ensure_annotations
def read_json(path_to_json: Path) -> ConfigBox:
    try:
        with open(path_to_json) as json_file:
            content = json.load(json_file)
            logger.info(f"json file {json_file} has been loaded")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("json file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(list_of_paths: List, verbose = True):
    for dir in list_of_paths:
        os.makedirs(dir, exist_ok=True)
        if verbose:
            logger.info(f"directory at {dir} has been created")


@ensure_annotations
def get_size_of_file(file_path: Path):
    size_in_kb = os.path.getsize(file_path)
    return f"size of {file_path} is {size_in_kb}"



@ensure_annotations
def run_pipeline(pipeline: Pipeline):
    try:
        start = time.time()
        logger.info(f">>>>>> Pipeline {pipeline.name} started <<<<<<") 

        pipeline.main()
        end = time.time()
        logger.info(f">>>>>> Pipeline {pipeline.name} completed in {end - start} seconds <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e