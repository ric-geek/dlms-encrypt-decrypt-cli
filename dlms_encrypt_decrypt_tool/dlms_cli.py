import argparse
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import unhexlify


def cifra_decifra(system_title, frame_counter, encryption_key, aad, apdu):

    additional_auth_data = "30" + aad

    # Create AESGCM object
    aesgcm = AESGCM(unhexlify(encryption_key))

    apdu = aesgcm.encrypt(create_iv(frame_counter, system_title), unhexlify(apdu), unhexlify(additional_auth_data))

    apdu = apdu.hex()

    return apdu


def create_iv(frame_counter, system_title):

    # Concatenate System Title with Frame Counter
    return unhexlify(system_title + frame_counter)


def main():

    parser = argparse.ArgumentParser(description="Simple tool for encrypt and decrypt DLMS APDU")
    parser.add_argument("system_title", type=str, help="System Title")
    parser.add_argument("frame_counter", type=str, help="Frame Counter")
    parser.add_argument("encryption_key", type=str, help="Encryption Key")
    parser.add_argument("authentication_key", type=str, help="Authentication Key")
    parser.add_argument("apdu", type=str, help="DLMS APDU")
    args = parser.parse_args()

    ret = cifra_decifra(args.system_title, args.frame_counter, args.encryption_key, args.authentication_key, args.apdu)

    # Print encrypted or decrypted DLMS APDU
    print("Encrypted/Dcrypted APDU: " + ret[:-32])
    print("Authentication TAG: " + ret[-32:])

if __name__ == "__main__":

    main()