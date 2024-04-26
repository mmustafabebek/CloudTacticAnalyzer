import re
import boto3

def get_caller_identity():
    try:
        # Attempt to list queues, which should result in an AccessDenied error
        sqs_client = boto3.client('sqs')
        sqs_client.list_queues()
    except Exception as e:
        # Check if the error message contains the caller identity information
        error_message = str(e)
        # Use regular expressions to extract the caller's identity from the error message
        match = re.search(r'User: (arn:aws:iam::\d+:.*?)\n', error_message)
        if match:
            caller_identity = match.group(1)
            return caller_identity
    return None

if __name__ == "__main__":
    caller_identity = get_caller_identity()
    if caller_identity:
        print("Caller's Identity:", caller_identity)
    else:
        print("Failed to retrieve caller's identity.")
