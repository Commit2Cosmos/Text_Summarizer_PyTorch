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
            logger.info(f"Created directory at {dir}")


@ensure_annotations
def get_size_of_folder(start_path: str):
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size



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