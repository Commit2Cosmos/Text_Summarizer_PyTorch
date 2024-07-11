import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq, TrainingArguments, Trainer
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainingConfig
from textSummarizer.logging import logger



class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    
    def train(self):
    
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to('cpu')
        seq2seq_DC = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

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
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            use_cpu=True
        )

        for ds_name in self.config.datasets:

            logger.info(f"Loading dataset: {ds_name}...")
            ds = load_from_disk(os.path.join(self.config.dataset_folder, ds_name))

            logger.info(f"Dataset loaded, staring training!")
            
            # try:

            trainer = Trainer(
                model = model_pegasus,
                args = trainer_args,
                tokenizer = tokenizer,
                data_collator=seq2seq_DC,
                train_dataset=ds['test'],
                eval_dataset=ds['validation']
            )

            trainer.train()

            model_pegasus.save_pretrained(os.path.join(self.config.root_dir, f"pegasus-{ds_name}-model"))
            tokenizer.save_pretrained(os.path.join(self.config.root_dir, f"{ds_name}-tokenizer"))

            # except Exception as e:
            #     logger.error(f"Error in training: {e}")

            logger.info(f"Training completed for dataset: {ds_name}! Model and tokenizer saved!")