import boto3
#import aws.accesskey as ak

# S3Buckets = boto3.resource('s3')
# bi= S3Buckets.buckes.all())

S3Buckets = boto3.resource('s3')

# response = S3Buckets.list_buckets()
 


for bucket in S3Buckets.buckets.all():
    print(bucket.name)
    for obj in bucket.objects.all():
       print("Name:  %s,size:  %.3f kb ,Storage cla ss:  %s, Creation date: %s" % (obj.key,(obj.size/1024), obj.storage_class,  bucket.creation_date))
 

ec2_sess = boto3.client('ec2', region_name='us-east-1')

# print(dir(ec2_sess))
# f1 = {"OwnerIds": ["685831863693"]}
# allsnapshots = ec2_sess.describe_snapshots(Filters=[f1])
#print(allsnapshots['Snapshots'])
# print(allsnapshots)