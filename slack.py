import json
import urllib3

def lambda_handler(event, context):
    # TODO implement
    http=urllib3.PoolManager()
    data={"text": "This is welcome page"}
    r =http.request("POST",
                    "https://hooks.slack.com/services/DGVSDVHJDSVDSJVHJ/HABFHVFHAVFAH/HASVHJAVHAJVHJAVAHJV",
                    body=json.dumps(data),
                    headers={"Content-Type": "application/json"})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
