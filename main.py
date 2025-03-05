from src.SummarizeWithPegasus.logging import logger
from src.SummarizeWithPegasus.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.SummarizeWithPegasus.pipeline.data_transformation import DataTransformationTrainingPipeline

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


STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f'stage {STAGE_NAME} started')
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f'stage {STAGE_NAME} finished')
except Exception as e:
    logger.exception(e)
    raise e