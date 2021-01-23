import json
import boto3
import requests

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    # TODO implement
    URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    r = requests.get( url = URL)
    
    data = r.json()
    print(data)
    price=data['bpi']['USD']['rate_float']
    time_data=data['time']['updated']
    
    output="Price of bitcoin is "+str(price)+"USD at datetime: "+time_data

    operation = event['httpMethod']
    if operation=='GET':
        return respond(None, output)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))