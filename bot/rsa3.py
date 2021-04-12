#!/usr/bin/env python3
# coding=utf-8

"""
Created by Johnny 2020/7/8 14:10
"""
import rsa
import base64


class RsaUtil:
    def __init__(self, privateKey, publicKey, data):
        if privateKey and publicKey:
            self.privateKey = rsa.PrivateKey.load_pkcs1(privateKey)
            self.publicKey = rsa.PublicKey.load_pkcs1(publicKey)
        else:
            (self.publicKey, self.privateKey) = rsa.newkeys(1024)
        self.data = data.encode("utf8")
        print("Decryption length: {} \ n decryption before content: {}".format(len(data), data))

    def encrypt(self):
        """
                 Public key encryption, public.pe requires PKCS1 format
                 : return: encryptdata encrypted
        """
        length = len(self.data)
        length_max = 117
        encryptDataText = []
        for i in range(0, length, length_max):
            encryptDataText.append(
                rsa.encrypt(self.data[i:i + length_max], self.publicKey))  # STR type, encode () is required to convert to bytes
        encryptData = b''.join(encryptDataText)
        encryptedData = base64.b64encode(encryptData)
        print("Encryption:", encryptedData.decode())
        return encryptData

    def decrypt(self, encryptData):
        """
                 Private key decryption, private.pem requires PKCS1 format
                 : PARAM Encryptdata: RSA public key encryption
                 : return: decryptdata decrypts the content
        """
        length = len(encryptData)
        length_max = 128
        decryptDataText = []
        for i in range(0, length, length_max):
            decryptDataText.append(
                rsa.decrypt(encryptData[i:i + length_max], self.privateKey).decode())  # bytes type, you need decode () to convert to Str
        decryptData = ''.join(decryptDataText)
        print("Decryption length: {} \ n Decrypt post: {}".format(len(decryptData), decryptData))

    def sign(self):
        # hash_method: the hash method used on the message. Use 'MD5', 'SHA-1','SHA-224', SHA-256', 'SHA-384' or 'SHA-512'.
        return rsa.sign(self.data, self.privateKey, 'MD5')

    def verify(self, signature):
        return bool(rsa.verify(self.data, signature, self.publicKey))


if __name__ == "__main__":
    privateKey = '''-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDZAzJb0n62WqMKQUFBdIBUc8Ld8NKuK1nrd9xXVrqt/UwXQlYn
MuGc8M1+c4rhRMZHcG1a4RBwUZBjQSWFSf9RdYAMHdyncmiHeTcAExZJC8jN8DrR
arbcJqPPPFPSsCMoRh9mxZESLJPikJjUCEdZvBYKXbMtiW5y3eefR6U2WQIDAQAB
AoGBAL1NtZM11sUZ4ZmjfNotV3jUFovmdNHsDR+DylkB1gzKpaKwgljlYLu3r3p8
Lgz+InzVDP+2ztE7xVlfzewstaNtRF/P32DI1J+zkK8tvW9jJ1Qj3kBIBeS6adn2
iWeMzcA4hNSekNPj3OXl8ZlsQHcwM+U0WoJV6t6nHF3dMMyBAkEA7KzVGFW5CgBn
OLITLbtMCpWgLeL7Cz5ZVZ/0bWOQ8L4Tl2h64XmPCLFWlmIWN1o8ndncfrb7r2BG
Y1QJcaNiyQJBAOq7XEuB9TMwXl6L8YdY18Ejve9TrTy8B9m9b++SeYYpKmrQrGxX
KOpSY6CV3W04fTdnv3GSeMD1wwqC3oUC7xECQQDAREd41WrU7S7tp/xckmNb1eGi
ZVp779Ky9JakptYAPOm9fmsU8KN59FbbJCPYI75Kncm6Rvx/pD6KQqLJZmnBAkEA
uLeqYM0rHRZCHRr5fa4fUyECVbS+jh3V+7ZEwP2+XiJE+/usxDEuxH8DYZqtvkaG
2zPshr5iAk8kJkBoRbnSUQJAbS97Id1Beq/rejivApjKTP2lCfkOj4TbluNspiec
rs7Eac1FTIFOwD+6tMG3K7nuRQ1UB9Cltjy15XW8MmYHRA==
-----END RSA PRIVATE KEY-----

'''
    publicKey = '''-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBANkDMlvSfrZaowpBQUF0gFRzwt3w0q4rWet33FdWuq39TBdCVicy4Zzw
zX5ziuFExkdwbVrhEHBRkGNBJYVJ/1F1gAwd3KdyaId5NwATFkkLyM3wOtFqttwm
o888U9KwIyhGH2bFkRIsk+KQmNQIR1m8Fgpdsy2JbnLd559HpTZZAgMBAAE=
-----END RSA PUBLIC KEY-----
'''
    # publicKey = privateKey = None
    data = 'nihao@456'
    RsaUtil = RsaUtil(privateKey, publicKey, data)
    encryptData = RsaUtil.encrypt()
    RsaUtil.decrypt(encryptData)
    signature = RsaUtil.sign()
    print(str(signature))
    result = RsaUtil.verify(signature)
    print("Check:", result)
