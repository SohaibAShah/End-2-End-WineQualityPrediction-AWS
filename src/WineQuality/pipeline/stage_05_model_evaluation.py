from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.model_evaluation import ModelEvaluation
from WineQuality import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()

if __name__ ==  '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationTrainingPipline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
