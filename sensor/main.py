from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeLine
if __name__ == "__main__":
    training_pipeline = TrainPipeLine()
    training_pipeline.run_pipeline()
   
