from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
 
class ModelTrainerTraingingPipeline:
    def __init__(self) -> None:
      pass
        
    def main3(self):
        config = ConfigurationManager()
        model_traine_config  = config.get_model_trainer_config()
        model_traine_config = ModelTrainer(config = model_traine_config)
        model_traine_config.train()