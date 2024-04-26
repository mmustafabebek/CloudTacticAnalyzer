import re

# Function to check if an AWS S3 bucket name is valid
def aws_is_valid_bucket_name(bucket_name):
    # Regular expression pattern to validate an AWS S3 bucket name
    pattern = r"^(?=.{3,63}$)(?!xn--|sthree-|sthree-configurator)(?!.*\.\.|.*-s3alias$|.*--ol-s3$)[a-z0-9][a-z0-9.-]*[a-z0-9]$"
    return bool(re.match(pattern, bucket_name))
