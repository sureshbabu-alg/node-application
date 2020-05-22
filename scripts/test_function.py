import sys
import os
import yaml
import json
import sqlalchemy

path = os.getenv('PATH')
def lambda_handler(event, context):
    print(event)
