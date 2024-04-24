import boto3

# Specify your AWS region
aws_region = 'us-east-2'

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=aws_region)

def create_ec2_instance(tag_value: str) -> None:

    # Specify the parameters for the instance

    instance_params = {
        'ImageId': 'ami-09b90e09742640522',      # AMI ID of the instance 
        'InstanceType': 't2.micro',     # Instance type 
        'MinCount': 1,
        'MaxCount': 1,
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': tag_value # Specify the desired name for the instance
                    }
                ]
            }
        ]
    }

    # Launch the EC2 instance
    response = ec2.run_instances(**instance_params)

    # Retrieve the instance ID
    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 instance {instance_id} is launching...")


def terminate_ec2_instance(tag_value: str): 

    response = ec2.describe_instances(Filters=[
        {
            'Name': 'tag:Name',
            'Values': [tag_value]
        }
    ])

    # Extract instance IDs from the response
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

  
    # Terminate instances with the specified tag
    if instance_ids:
        ec2.terminate_instances(InstanceIds=instance_ids)
        print(f"Terminating instances with tag Name and value '{tag_value}'...")
    else:
        print(f"No instances found with tag Name and value '{tag_value}' to terminate.")
    # for instance_id in instance_ids:
    #     print(instance_id)


