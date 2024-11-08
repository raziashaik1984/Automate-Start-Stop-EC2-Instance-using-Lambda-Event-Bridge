# Automate-Start-Stop-EC2-Instance-using-Lambda-Event-Bridge
## Overview

This repository provides a solution to automate the start and stop of AWS EC2 instances at scheduled times. By using AWS Lambda and EventBridge, this automation can reduce costs by ensuring that instances are only running when needed.

## Architecture
### AWS Lambda: 
The Lambda function contains the code to start and stop EC2 instances based on EventBridge triggers.
### Amazon EventBridge:
 This is used to schedule events to trigger the Lambda function at specified times, controlling when EC2 instances should start or stop.
This setup enables automatic instance management without manual intervention.
## Prerequisites
Before deploying this solution, ensure that you have the following:

**AWS Account:** This solution requires access to AWS services.

**Permissions:**
Lambda must have permissions to start and stop EC2 instances.
EventBridge must be able to invoke Lambda.

**IAM Role for Lambda:**
An IAM role with the following policies attached:

**CloudWatch Logging:** Allows the Lambda function to write logs, so you can monitor function execution.

**EC2 Control:** Grants permissions for starting, stopping, and describing EC2 instances.

## Setup
### Step 1: Configure IAM Role for Lambda
Go to the IAM console.

Create a new role with the following custom IAM Policy:
```

{  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",	
        "ec2:Stop*"
      ],
      "Resource": "*"
    }
  ]
}
```

You can attach this IAM role to the Lambda function for your solution.

### Step 2: Create the Lambda Function
Open the AWS Lambda console.

Create a new function, using Python 3.9 as the runtime.

Assign the IAM role created in Step 1 to the Lambda function.

Copy the code provided in the repository (lambda_function.py) into the function's editor.
```
import boto3
region = 'us-east-1' 
instances = ['i-033f8ac40ac7dd4e0'] 
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
 ```

Adjust any variables in the code if necessary, such as the target instance ID or region.

### Step 3: Set Up EventBridge Rules for Scheduling

Go to the EventBridge console.

Create two rules:

Start EC2 Instance: Set the cron expression or rate to define the time to start the instance.

Stop EC2 Instance: Set another cron expression or rate to define the time to stop the instance.

For each rule, configure the target as the Lambda function created in Step 2.
Save the rules, and verify that they are enabled.

Configuration
The Lambda function can be configured by modifying the following variables:

INSTANCE_ID: ID of the EC2 instance to start/stop.
REGION: AWS region of the EC2 instance.
Additional configurations can be added as environment variables in the Lambda console.
Usage

### Once deployed, the setup will:

Automatically start the EC2 instance at the specified time(s) using EventBridge.
Automatically stop the EC2 instance at the specified time(s) using another EventBridge rule.

To test, you can manually invoke the Lambda function to ensure it starts and stops the instance as expected.



   
### Testing
To test the Lambda function independently:

Go to the Lambda console.
Use the "Test" feature and pass an event with "action": "start" or "action": "stop".
Verify that the EC2 instance starts or stops accordingly.
### Troubleshooting
**Permissions:** Ensure that the Lambda role has the necessary permissions to start and stop EC2 instances.

**Event Timing:** Double-check cron expressions or rate values in EventBridge rules to confirm they align with the desired schedule.

**Logging:** Check CloudWatch Logs for detailed output from Lambda function executions

### License
This project is licensed under the MIT License.



