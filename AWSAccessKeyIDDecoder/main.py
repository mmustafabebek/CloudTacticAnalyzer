import base64
import binascii

def get_aws_account_id(access_key_id):
    trimmed_access_key_id = access_key_id[4:]  # remove KeyID prefix
    decoded_key = base64.b32decode(trimmed_access_key_id)  # base32 decode
    first_six_bytes = decoded_key[:6]
    mask = int.from_bytes(binascii.unhexlify(b'7fffffffff80'), byteorder='big', signed=False)
    account_id = (int.from_bytes(first_six_bytes, byteorder='big', signed=False) & mask) >> 7
    return "{:012d}".format(account_id)

# Prompt the user to enter the access key ID
access_key_id = input("Enter the AWS Access Key ID: ")

# Get and print the AWS account ID
account_id = get_aws_account_id(access_key_id)
print("\nAccount ID:", account_id)


# Example usage
# access_key_id = "ASIAQNZGKIQY56JQ7WML"
