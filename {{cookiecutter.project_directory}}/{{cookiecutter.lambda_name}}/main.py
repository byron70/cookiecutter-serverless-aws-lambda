import json

import boto3
from aws_lambda_powertools import Logger, Metrics, Tracer

# https://awslabs.github.io/aws-lambda-powertools-python/#features
tracer = Tracer()
logger = Logger()
metrics = Metrics()

# Global variables are reused across execution contexts (if available)
session = boto3.Session()


# @metrics.log_metrics(capture_cold_start_metric=True)
# @logger.inject_lambda_context
# @tracer.capture_lambda_handler
def lambda_handler(event, context):
    logger.debug(json.dump(event))

    message = {"hello": "world"}
    return {'statusCode': 200,
            'body': json.dumps(message)}
