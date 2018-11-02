

######CODE FOR DYNAMODB Data Dump######

import json
import boto3
#import requests
import time
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import csv

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name = 'us-east-2')
    table = dynamodb.Table('LoanData')
    
    data_entry = {}
    data_entry['Year'] = '2011'
    data_entry['LoanSum'] = '57857825'
    data_entry['FundSum'] = '56158025'
    data_entry['FundSumInv'] = '47556195'
    
    x = json.loads(json.dumps(data_entry))
    print(type(x),x)
    table.put_item(TableName='LoanData',Item = x)



######CODE FOR DATA FETCH###########

import json
import boto3
#import requests
import time
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import csv

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource("dynamodb", region_name='us-east-2')

    table = dynamodb.Table('LoanData')
    
    
    
    response = table.get_item(Key={'Year': event['params']['querystring']['year']})
    
    item = response['Item']
    print("GetItem succeeded:",item)
    # print(json.dumps(item, indent=4, cls=DecimalEncoder))
    return item
    # return {
    #     'statusCode': 200,
    #     'body': event['params']['querystring']['year']
    # }
