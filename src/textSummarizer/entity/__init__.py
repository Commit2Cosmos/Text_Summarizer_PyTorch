from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path


class Pipeline:
    name: str
    #* Make sure the method is overriden
    def main(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    datasets: Dict[str, str]


@dataclass(frozen=True)
class DataValidationConfig:
    dataset_folder: Path
    datasets: Dict[str, str]
    required_folders: List[str]
    required_files: List[str]


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    dataset_folder: Path
    datasets: Dict[str, str]
    tokenizer: str
    batch_size: int
    input_max_length: int
    target_max_length: int