from src.SummarizeWithPegasus.logging import logger
from src.SummarizeWithPegasus.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.SummarizeWithPegasus.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.SummarizeWithPegasus.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.SummarizeWithPegasus.pipeline.model_trainer import ModelTrainerTrainingPipeline
from src.SummarizeWithPegasus.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

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

STAGE_NAME = 'Model Training Stage'

try:
    logger.info(f'stage {STAGE_NAME} started')
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f'stage {STAGE_NAME} finished')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
