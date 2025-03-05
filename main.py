from src.SummarizeWithPegasus.logging import logger
from src.SummarizeWithPegasus.pipeline.data_ingestion import DataIngestionTrainingPipeline

logger.info("logging is implemented")

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'stage {STAGE_NAME} started')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f'stage {STAGE_NAME} finished')
except Exception as e:
    logger.exception(e)
    raise e

