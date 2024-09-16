import boto3
import json
import time

sagemaker = boto3.client('sagemaker')

def lambda_handler(event, context):
    try:
        # Extract parameters from the event object if necessary
        input_s3_uri = "s3://ml-training-flow-sgm-pj-input/input-data/"
        output_s3_uri = "s3://ml-training-flow-sgm-pj-output/output-data/"
        role_arn = "arn:aws:iam::649999766497:role/service-role/AmazonSageMaker-ExecutionRole-20240910T110249"

        # Generate a unique job name using timestamp or UUID
        job_name = "ml-training-flow-sgm-pj-" + str(int(time.time()))
        
        # Create the SageMaker processing job
        response = sagemaker.create_processing_job(
            ProcessingJobName=job_name,
            ProcessingInputs=[
                {
                    'InputName': 'data',
                    'S3Input': {
                        'S3Uri': input_s3_uri,
                        'LocalPath': '/opt/ml/processing/input-data',
                        'S3DataType': 'S3Prefix',
                        'S3InputMode': 'File',
                    }
                }
            ],
            ProcessingOutputConfig={
                'Outputs': [
                    {
                        'OutputName': 'output',
                        'S3Output': {
                            'S3Uri': output_s3_uri,
                            'LocalPath': '/opt/ml/processing/output-data',
                            'S3UploadMode': 'EndOfJob'
                        }
                    }
                ]
            },
            ProcessingResources={
                'ClusterConfig': {
                    'InstanceCount': 1,
                    'InstanceType': 'ml.t3.medium',
                    'VolumeSizeInGB': 1
                }
            },
            AppSpecification={
                'ImageUri': '649999766497.dkr.ecr.us-east-1.amazonaws.com/epwery/ml-training-flow:1.0.0',
                'ContainerEntrypoint': ['bash', '-c'],
                'ContainerArguments': ['git pull && ./training_flow/sgm_proc_job_docker/pj_execute.sh']
            },
            RoleArn=role_arn
        )

        # Log the response
        print(f"Processing job created successfully: {response}")
        
        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps('Processing job created successfully'),
            'processingJobArn': response['ProcessingJobArn']
        }

    except Exception as e:
        print(f"Error creating processing job: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error creating processing job: {str(e)}")
        }
