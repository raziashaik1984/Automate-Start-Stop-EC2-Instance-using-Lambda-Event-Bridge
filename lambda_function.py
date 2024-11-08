```
import boto3
region = 'us-east-1' 
instances = ['i-033f8ac40ac7dd4e0'] 
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
```

   
  
