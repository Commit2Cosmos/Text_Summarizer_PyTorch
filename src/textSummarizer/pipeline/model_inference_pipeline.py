import os
from transformers import pipeline

from transformers import AutoTokenizer
from textSummarizer.config.configuration import ConfigManager
from textSummarizer.entity import Pipeline



class ModelInferencePipeline(Pipeline):
    def __init__(self):
        self.name = "Model Inference Pipeline"
        self.config = ConfigManager().get_model_evaluation_config()

    

    def infer(self, input_text: str):
        
        tokenizer = AutoTokenizer.from_pretrained(os.path.join(self.config.trained_folder, f"{self.config.trained_model_ckpt}-tokenizer"))
        pip_kwargs = {
            "length_penalty": self.config.length_penalty,
            "num_beams": self.config.num_beams,
            "max_length": self.config.target_max_length
        }

        pipe = pipeline(
            "summarization",
            model=os.path.join(self.config.trained_folder, f"{self.config.trained_model_ckpt}-model"),
            tokenizer=tokenizer
        )

        print("Dialogue:")
        print(input_text)

        output = pipe(input_text, **pip_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)