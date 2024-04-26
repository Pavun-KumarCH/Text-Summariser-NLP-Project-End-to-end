from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTraingingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTraingingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} Completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e