#!/usr/bin/python
import argparse
import hmac
import hashlib
import base64
import time

def generate_otp(secret_key, timestamp):
    # Divide the timestamp by 30 seconds to get the time step
    time_step = timestamp // 30

    # Convert the time step to a byte array
    time_bytes = time_step.to_bytes(8, byteorder='big')

    # Calculate the hash value using the HMAC-SHA1 algorithm
    hmac_result = hmac.new(secret_key, time_bytes, hashlib.sha1).digest()

    # Get the low four bits of the last byte of the hash value as the offset
    offset = hmac_result[-1] & 0x0F

    # Take four bytes starting from the offset as the dynamic code
    dynamic_code = ((hmac_result[offset] & 0x7F) << 24) \
        | (hmac_result[offset + 1] << 16)               \
        | (hmac_result[offset + 2] << 8)                \
        | hmac_result[offset + 3]

    # Convert the dynamic code to an integer
    otp = dynamic_code % 1000000
    return str(otp).zfill(6)

def read_secret_key(file_path):
    secret_key = b''
    with open(file_path, 'r') as file:
        for line in file:
            secret_key += base64.b32decode(line.strip().upper())
    return secret_key

def main(secret_key_file):
    # Read the secret key from the file
    secret_key = read_secret_key(secret_key_file)

    # Get the current timestamp
    current_timestamp = int(time.time())

    # Generate the OTP for the current time
    current_otp = generate_otp(secret_key, current_timestamp)

    # Calculate the remaining seconds until the next time step
    remaining_seconds = 30 - (current_timestamp % 30)

    # Generate the timestamp for the next time step
    next_timestamp = current_timestamp + 30

    # Generate the OTP for the next time step
    next_otp = generate_otp(secret_key, next_timestamp)

    print(f'Current OTP: {current_otp}')
    print(f'Next OTP: {next_otp}')
    print(f'Remaining Seconds: {remaining_seconds}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate OTP using TOTP algorithm.')
    parser.add_argument('secret_key_file', help='path to the secret key file')
    args = parser.parse_args()

    main(args.secret_key_file)
