import boto3

sagemaker = boto3.client('sagemaker')

response = sagemaker.create_processing_job(
    ProcessingJobName='my-processing-job',
    ProcessingInputs=[
        {
            'InputName': 'data',
            'S3Input': {
                'S3Uri': 's3://your-bucket/path-to-your-input-data',
                'LocalPath': '/opt/ml/processing/input',
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
                    'S3Uri': 's3://your-bucket/path-to-your-output',
                    'LocalPath': '/opt/ml/processing/output',
                    'S3UploadMode': 'EndOfJob'
                }
            }
        ]
    },
    ProcessingResources={
        'ClusterConfig': {
            'InstanceCount': 1,
            'InstanceType': 'ml.m5.xlarge',
            'VolumeSizeInGB': 10
           }
       },
    AppSpecification={
        'ImageUri': 'your-docker-image-uri',
        'ContainerEntrypoint': ['python3', 'your_script.py']
    },
    RoleArn='your-sagemaker-role-arn'
)