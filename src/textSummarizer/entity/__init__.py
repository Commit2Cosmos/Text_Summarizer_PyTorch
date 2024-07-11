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
    datasets: List[str]
    required_folders: List[str]
    required_files: List[str]