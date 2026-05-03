# Describe all EC2 instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Instance:InstanceId,Type:InstanceType,State:State.Name}' --output table
