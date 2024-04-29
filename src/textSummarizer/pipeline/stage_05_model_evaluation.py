from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evalution import ModelEvaluation
 
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main4(self):
        config = ConfigurationManager()
        model_evalution_config = config.get_model_evalution_config()
        model_evalution_config = ModelEvaluation(config=model_evalution_config)
        model_evalution_config.evaluate_model()                             