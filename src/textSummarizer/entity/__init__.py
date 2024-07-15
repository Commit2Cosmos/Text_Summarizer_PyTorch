from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path
from torch import device


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
    model_ckpt: str

    #* params.json
    batch_size: int
    input_max_length: int
    target_max_length: int


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    dataset_folder: Path
    datasets: Dict[str, str]
    model_ckpt: str
    trained_model_ckpt: str
    device: device

    #* params.json
    num_train_epochs: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    warmup_steps: int
    weight_decay: float
    logging_steps: int
    eval_strategy: str
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    dataset_folder: Path
    datasets: Dict[str, str]
    trained_folder: Path
    tokenizer_ckpt: str
    trained_model_ckpt: str
    metric_name: str
    metric_file: str
    device: device

    input_max_length: int
    target_max_length: int

    #* params.json
    batch_size: int
    length_penalty: float
    num_beams: int