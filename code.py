

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
    data = {}
    data['LoanSum'] = str(int(float(item['LoanSum'])))
    data['FundSum'] = str(int(float(item['FundSum'])))
    data['FundSumInv'] = str(int(float(item['FundSumInv'])))
    graph1 = json.loads(item['Graph1'])
    data['Graph1'] = [{'x':list(graph1.keys()),'y':list(graph1.values()),'type':'bar'}]
    data['Graph2'] = json.loads(item['Graph2'])
    
    for item in data['Graph2']:
        data['Graph2'][item]['mode'] = 'lines'
        data['Graph2'][item]['name'] = item
    
    return data
