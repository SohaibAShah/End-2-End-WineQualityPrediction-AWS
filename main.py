from WineQuality import logger
from WineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from WineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipline
from WineQuality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipline
from WineQuality.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipline
from WineQuality.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainerTrainingPipline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelEvaluationTrainingPipline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e