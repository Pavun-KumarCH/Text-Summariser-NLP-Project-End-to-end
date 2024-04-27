from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTraingingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTraingingPipeline
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

