import argparse
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import unhexlify


def cifra_decifra(system_title, frame_counter, encryption_key, apdu, aad):

    # Create AESGCM object
    aesgcm = AESGCM(encryption_key)

    apdu = aesgcm.encrypt(create_iv(frame_counter, system_title), apdu, aad)

    apdu = apdu.hex()

    return apdu

def create_iv(frame_counter, system_title):

    # Concatenate System Title with Frame Counter
    return system_title + frame_counter



parser = argparse.ArgumentParser(description="Simple tool for encrypt and decrypt DLMS APDU")
parser.add_argument("system_title", type=str, help="System Title")
parser.add_argument("frame_counter", type=str, help="Frame Counter")
parser.add_argument("encryption_key", type=str, help="Encryption Key")
parser.add_argument("apdu", type=str, help="DLMS APDU")
args = parser.parse_args()

ret = cifra_decifra(args.system_title, args.frame_counter, args.encryption_key, args.apdu)