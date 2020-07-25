import boto3   
from   pprint import pprint

ec2 = boto3.resource('ec2',region_name='us-east-1')
 
ins=ec2.Instance(id='i-01d77179956a9f40d')

for tags in ins.tags:
    print(tags.get('Key'))
    print(tags.get('Value'))

 

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
for instance in instances:
    
    print(instance.id, instance.instance_type)
    pprint(instance)
 
# boto3.resource object doen't have method describe_instances . So creating client object
ec2client = boto3.client('ec2',region_name='us-east-1')
 

response = ec2client.describe_instances(
    Filters=[
            {
                'Name': 'tag:test',
                'Values': ['sample']
        }
    ]
)

# prettiying the response with filters applied
pprint(response)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:
            if tag['Key'] == 'test':                 
                print(tag['Value'])
        print('Instance id : ' ,instance['InstanceId'])
        print('Image id : ',instance['ImageId'])
        
# instance properties.....  
ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(
        "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
        instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
        )
    )
