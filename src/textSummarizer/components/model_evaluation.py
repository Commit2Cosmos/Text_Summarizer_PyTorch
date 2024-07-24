import os
import evaluate
from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import json

from textSummarizer.logging import logger
from textSummarizer.entity import ModelEvaluationConfig




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config


    def evaluate(self):

        try:
            tokenizer = AutoTokenizer.from_pretrained(os.path.join(self.config.trained_folder, f'{self.config.trained_tokenizer_ckpt}-tokenizer'))

            rouge_metric = evaluate.load(self.config.metric_name)
            model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(os.path.join(self.config.trained_folder, f'{self.config.trained_model_ckpt}-model')).to(self.config.device)
        except EnvironmentError as e:
            logger.error(f"Failed to load tokenizer: {e}")
            raise


        def generate_batch_sized_chunks(list_of_elements, batch_size):
            """split the dataset into smaller batches that we can process simultaneously
            Yield successive batch-sized chunks from list_of_elements."""
            for i in range(0, len(list_of_elements), batch_size):
                yield list_of_elements[i : i + batch_size]


        for ds_name in self.config.datasets:
            ds_test = load_from_disk(os.path.join(self.config.dataset_folder, ds_name))['validation']

            for article_batch, target_batch in tqdm(zip(generate_batch_sized_chunks(ds_test['dialogue'], self.config.batch_size), 
                                                        generate_batch_sized_chunks(ds_test['summary'], self.config.batch_size)
                                                        )):
                
                inputs = tokenizer(article_batch, max_length=self.config.input_max_length, truncation=True, padding="max_length", return_tensors="pt")
                
                summaries = model_pegasus.generate(input_ids=inputs["input_ids"].to(self.config.device),
                                                   attention_mask=inputs["attention_mask"].to(self.config.device),
                                                   length_penalty=self.config.length_penalty,
                                                   num_beams=self.config.num_beams,
                                                   max_length=self.config.target_max_length)
                
                decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True) for s in summaries]      
                
                decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
                
                rouge_metric.add_batch(predictions=decoded_summaries, references=target_batch)
                
            score = rouge_metric.compute()
            
            with open(os.path.join(self.config.root_dir, self.config.metric_file), 'w') as f:
                json.dump(score, f)