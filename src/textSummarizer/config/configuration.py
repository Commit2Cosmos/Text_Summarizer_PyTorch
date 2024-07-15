import torch
from textSummarizer.utils.common import read_json, create_directories
from textSummarizer.constants import *
from textSummarizer.entity import *


class ConfigManager:
    def __init__(self):
        self.config = read_json(path_to_json=CONFIG_FILE_PATH)
        self.params = read_json(path_to_json=PARAMS_FILE_PATH)

        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        datasets = self.config.datasets

        create_directories([config.root_dir])
        
        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            datasets=datasets,
        )
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        datasets = self.config.datasets
        data_folder = self.config.data_ingestion.root_dir

        return DataValidationConfig(
            dataset_folder=Path(data_folder),
            datasets=datasets,
            required_folders=config.required_folders,
            required_files=config.required_files
        )
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        data_folder = self.config.data_ingestion.root_dir
        datasets = self.config.datasets
        params = self.params.transformation_args

        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            dataset_folder=Path(data_folder),
            datasets=datasets,
            model_ckpt=config.model_ckpt,

            batch_size=params.batch_size,
            input_max_length=params.input_max_length,
            target_max_length=params.target_max_length
        )
    

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        data_folder = self.config.data_transformation.root_dir
        datasets = self.config.datasets
        model_ckpt = self.config.data_transformation.model_ckpt
        params = self.params.training_args

        create_directories([config.root_dir])

        return ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            dataset_folder=Path(data_folder),
            datasets=datasets,
            model_ckpt=model_ckpt,
            trained_model_ckpt=config.trained_model_ckpt,
            device=self.device,

            num_train_epochs=params.num_train_epochs,
            per_device_train_batch_size=params.per_device_train_batch_size,
            per_device_eval_batch_size=params.per_device_eval_batch_size,
            warmup_steps=params.warmup_steps,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            eval_strategy=params.eval_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        data_folder = self.config.data_transformation.root_dir
        datasets = self.config.datasets
        trained_folder = self.config.model_training.root_dir
        trained_model_ckpt = self.config.model_training.trained_model_ckpt
        tokenizer_ckpt = self.config.data_transformation.model_ckpt
        params = self.params.eval_args
        input_max_length = self.params.transformation_args.input_max_length
        target_max_length = self.params.transformation_args.target_max_length

        create_directories([config.root_dir])

        return ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            dataset_folder=Path(data_folder),
            datasets=datasets,
            trained_folder=Path(trained_folder),
            trained_model_ckpt=trained_model_ckpt,
            tokenizer_ckpt=tokenizer_ckpt,
            metric_name=config.metric_name,
            metric_file=config.metric_file,
            device=self.device,
            
            input_max_length=input_max_length,
            target_max_length=target_max_length,

            batch_size=params.per_device_eval_batch_size,
            length_penalty=params.length_penalty,
            num_beams=params.num_beams
        )