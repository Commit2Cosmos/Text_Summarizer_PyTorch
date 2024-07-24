import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq, TrainingArguments, Trainer, PreTrainedModel
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainingConfig
from textSummarizer.logging import logger
import torch



class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    
    def train(self):
    
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus: PreTrainedModel = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(self.config.device)

        #* freeze all layers
        for param in model_pegasus.parameters():
            param.requires_grad = False

        #* unfreeze newly initialized layers
        for name, param in model_pegasus.named_parameters():
            if name.startswith("model.decoder.layers.15") or name.startswith("model.encoder.layers.15"):
                param.requires_grad = True


        seq2seq_DC = DataCollatorForSeq2Seq(tokenizer, model = model_pegasus)


        trainer_args = TrainingArguments(
            output_dir = self.config.root_dir,
            num_train_epochs = self.config.num_train_epochs,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size = self.config.per_device_eval_batch_size,
            warmup_steps = self.config.warmup_steps,
            weight_decay = self.config.weight_decay,
            logging_steps = self.config.logging_steps,
            eval_strategy=self.config.eval_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            #TODO: ADD TO PARAMS
            save_total_limit=1,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )

        for ds_name in self.config.datasets:

            logger.info(f"Loading dataset: {ds_name}...")
            ds = load_from_disk(os.path.join(self.config.dataset_folder, ds_name))
            # ds.set_format('torch', device="mps")

            logger.info(f"Dataset loaded, staring training!")
            
            try:

                trainer = Trainer(
                    model = model_pegasus,
                    args = trainer_args,
                    tokenizer = tokenizer,
                    data_collator=seq2seq_DC,
                    train_dataset=ds['test'],
                    eval_dataset=ds['validation']
                )

                trainer.train()

                model_pegasus.save_pretrained(os.path.join(self.config.root_dir, f"{self.config.trained_model_ckpt}-model"))
                tokenizer.save_pretrained(os.path.join(self.config.root_dir, f"{self.config.trained_model_ckpt}-tokenizer"))

            except Exception as e:
                logger.error(f"Error in training: {e}")
                raise e

            logger.info(f"Training completed for dataset: {ds_name}! Model and tokenizer saved!")