import hmac
import json
import base64
import struct
import time
import requests
from datetime import datetime

def generate_totp(email, time_step=30):
    # Create shared secret
    shared_secret = f"{email}HENNGECHALLENGE003"
    
    # Get current timestamp and calculate counter
    now = int(time.time())
    counter = struct.pack('>Q', now // time_step)
    
    # Generate HMAC-SHA512
    h = hmac.new(
        shared_secret.encode('utf-8'),
        counter,
        'sha512'
    )
    
    # Get 8 bytes offset
    offset = h.digest()[-1] & 0xf
    
    # Generate 4 bytes code
    code = struct.unpack('>I', h.digest()[offset:offset+4])[0]
    code = code & 0x7fffffff
    
    # Get 10 digits
    totp = str(code)[-10:].zfill(10)
    return totp

def send_solution(github_url, email):
    # Prepare JSON payload
    payload = {
        "github_url": github_url,
        "contact_email": email,
        "solution_language": "python"
    }
    
    # Generate TOTP
    totp = generate_totp(email)
    
    # Create basic auth credentials
    credentials = base64.b64encode(
        f"{email}:{totp}".encode('utf-8')
    ).decode('utf-8')
    
    # Prepare headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credentials}'
    }
    
    # Make POST request
    response = requests.post(
        'https://api.challenge.hennge.com/challenges/003',
        headers=headers,
        json=payload
    )
    
    return response

def main():
    # Replace these with your actual values
    github_url = "https://gist.github.com/ShiratsuYudachi/4f74f8712a4c6eb9a147509d3e2609f0"
    email = "cliudp@connect.ust.hk"
    
    try:
        response = send_solution(github_url, email)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
