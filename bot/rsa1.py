# coding=utf-8
import base64
import rsa

__all__ = ['rsa_encrypt']


def _str2key(s):
    # decode the string
    b_str = base64.b64decode(s)

    if len(b_str) < 162:
        return False

    hex_str = ''

    # Convert to hexadecimal in bits
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h

    # Find the beginning and end of the modulus and exponent
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]

    return modulus, exponent


def rsa_encrypt(s, pubkey_str):
    '''
         Rsa encryption
    :param s:
         :param pubkey_str: public key
    :return:
    '''
    key = _str2key(pubkey_str)
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    pubkey = rsa.PublicKey(modulus, exponent)
    return base64.b64encode(rsa.encrypt(s.encode(), pubkey)).decode()

