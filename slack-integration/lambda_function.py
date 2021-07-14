'''Requester for DinoCloudBot on Slack'''

import json
import urllib3
import os

def lambda_handler(event, context):
    # TODO implement
    http = urllib3.PoolManager()
    data = {"text": "Sample message from DinoCloudBot Lambda Function"}
    r = http.request("POST",
        os.environ['slack_url'],
        body = json.dumps(data),
        headers = {"Content-Type": "application/json"})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }