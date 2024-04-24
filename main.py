from ec2_utils import create_ec2_instance, terminate_ec2_instance

def main(event, context):
    tag_name = "instance_test"

    create_ec2_instance(tag_name)

