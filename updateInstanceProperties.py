import boto3
ec2 = boto3.client('ec2')

# choose an EC2 instance with id
instance_id = 'i-05ca5f05f965b3a4b'


# Stop the instance
ec2.stop_instances(InstanceIds=[instance_id])
waiter=ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])

# Change the instance type
ec2.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value='t2.small')

# Start the instance
ec2.start_instances(InstanceIds=[instance_id])