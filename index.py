import boto3
def lambda_handler(event, context):
    print('THIS IS A LAMBDA created FROM Cloudformation')
    return 'Sucess'