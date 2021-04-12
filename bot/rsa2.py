import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA

def encrpt(password, public_key):
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    return cipher_text.decode()

if __name__ == '__main__':
    public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9iE3T355IktI5kG+XMrh8k71L
0aqDTG5YRh3hT+0ouS3hxufPvLEN8eUmPFdYXJ6RU7tezX84xGf58t0pLo+TV6Rq
QlyJikH9ZhEV1/W5FTXcH+N7Ei98WHk2H8auRTDp1JLO9EY9zDuVbsLuVjXkrDHY
aGvxp0RYvmwm3bbYyQIDAQAB
-----END PUBLIC KEY-----
"""
    pass_word = '123456'
    print(encrpt(pass_word, public_key))
