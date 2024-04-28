from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTraingingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTraingingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTraingingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTraingingPipeline

from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTraingingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
    data_validation = DataValidationTraingingPipeline()
    data_validation.main1()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
    data_transformation = DataTransformationTraingingPipeline()
    data_transformation.main2()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training stage"
try:
    logger.info(f"#######################################")
    logger.info(f"Run it on google colab if any error encounters")
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
    model_trainer = ModelTrainerTraingingPipeline()
    model_trainer.main3()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e