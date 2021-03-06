import boto3
import csv
from pprint import pprint


session=boto3.Session(profile_name='default',region_name='us-east-1')
ec2 = boto3.resource('ec2')
PathToCSVFile="create_tag.csv"

#csv file format should be like every row has to be following format. Header row contents as below.
#instance_id,Key1,Value1,Key2,Value2

with open(PathToCSVFile, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        for var in ec2.instances.all():
            print(var.id == row['instance_id'].strip(),  var.id, row['instance_id'], row['Key1'], row['Value1'], row['Key2'], row['Value2'])
            if (var.id)==row['instance_id'].strip():
                var.create_tags(Tags=[{'Key': row['Key1'], 'Value': row['Value1']},{'Key': row['Key2'], 'Value': row['Value2']}])
