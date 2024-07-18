import os
from transformers import AutoTokenizer
from datasets import load_from_disk

from textSummarizer.entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)

    
    def __convert_egs_to_features(self, batch):

        input_encodings = self.tokenizer(batch['dialogue'], max_length=self.config.input_max_length, truncation=True, padding=True)
        target_encodings = self.tokenizer(text_target=batch['summary'], max_length=self.config.input_max_length, truncation=True, padding=True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def save_features(self):
        
        for ds_name in self.config.datasets:
            ds = load_from_disk(os.path.join(self.config.dataset_folder, ds_name))

            #! TESTING
            for name in ['test', 'validation']:
                ds[name] = ds[name].select(range(20))

            ds = ds.map(self.__convert_egs_to_features, batched = True, batch_size=self.config.batch_size)
            ds.save_to_disk(os.path.join(self.config.root_dir, ds_name))