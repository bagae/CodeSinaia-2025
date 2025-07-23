import sys
import segno
from tqdm import tqdm
import time

import secrets
import base64
import hmac
import hashlib
import struct


# ========= function for generating a secret ========
def generate_shared_secret():
    return secrets.token_bytes(10)


# ========= function for generating the QR code ========
def gen_qr(user_id):
    # Example URI: otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example
    code1 = "otpauth://totp/Google%20Authenticator:"
    code2 = "?secret="
    code3 = "&issuer=Google%20Authenticator"
    
    secret = base64.b32encode(generate_shared_secret()).decode('utf-8')     # generate secret key
    
    # TODO: combine code# and user id to create URI (hint: match example URI format given above)
    uri = None
    uri = f"{code1}{user_id}{code2}{secret}{code3}"
    print(" >> URI generated: ", uri)

    # TODO: store secret into a file named "secret.txt"

    file='secret.txt'
    with open(file, 'w') as f:
        f.write(secret)
   
    # TODO: generate QR code based on the URI using snego library
    qrcode = segno.make(uri, micro=False)
    qrcode.save('qr_code.png')

    return


# ========= function for generating the One-Time Password ========
import time, hmac, base64, struct, hashlib

def generate_otp(secret_base32, digits=6, time_step=30):
    # 1. Decode secret
    key = base64.b32decode(secret_base32, casefold=True)

    # 2. Get current time step
    counter = int(time.time() // time_step)

    # 3. Pack time step counter into 8-byte big-endian
    counter_bytes = struct.pack(">Q", counter)

    # 4. Generate HMAC-SHA1 digest
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()

    # 5. Dynamic truncation offset
    offset = hmac_hash[-1] & 0x0F

    # 6. Get 4 bytes from HMAC starting at offset
    selected_bytes = hmac_hash[offset:offset+4]

    # 7. Convert 4 bytes to 32-bit int
    code_int = struct.unpack(">I", selected_bytes)[0]

    # 8. Remove sign bit
    code_int = code_int & 0x7FFFFFFF

    # 9. Get last `digits` (default 6)
    otp = code_int % (10 ** digits)

    # Pad with leading zeros if needed
    return str(otp).zfill(digits)

# ========= function for displaying OPT every 30 sec ========
def get_otp(t=30):
    # TODO: open and read file containing secret; Hint: use readline
    file = 'secret.txt'
    with open(file, 'r') as f:
        secret = f.readline().strip()
        
    
    #file.close()

    while True:
        otp = generate_otp(secret)
        print(" > Generated OTP:", otp, "valid for", int(t-(time.time()%t))+1, "seconds")
        # loop for waiting 30 sec between OTP generation
        for _ in tqdm (range(int(t-(time.time()%t))+1), 
               desc="Loading…", 
               ascii=False, ncols=75):
            time.sleep(1)


# ========= mainfunction for command handling ========
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(" >> Invalid flag: can either be \"--generate-qr [user_id]\" or \"--get-otp\"")
    elif sys.argv[1] == "--generate-qr" and len(sys.argv) == 3:
        gen_qr(sys.argv[2])
    elif sys.argv[1] == "--get-otp" and len(sys.argv) == 2:
        get_otp()
    else:
        print(" >> Invalid flag: can either be \"--generate-qr [user_id]\" or \"--get-otp\"")
   