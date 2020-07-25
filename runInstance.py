import boto3  
ec2= boto3.resource('ec2',region_name='us-east-1')
instances = ec2.create_instances(
     ImageId='ami-00b6a8a2bd28daf19',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro'
    
    
 )