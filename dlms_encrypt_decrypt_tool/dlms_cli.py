import argparse
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from binascii import unhexlify

SECURITY_HEADER = ["10", "30"]


def auth_apdu(system_title, frame_counter, encryption_key, authentication_key, stoc):

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
    from cryptography.hazmat.backends.interfaces import CipherBackend
    from cryptography.hazmat.primitives.ciphers import algorithms, base, modes

    aad = SECURITY_HEADER[0] + authentication_key + stoc

    cipher = base.Cipher(
        algorithms.AES(unhexlify(encryption_key)),
        modes.GCM(create_iv(frame_counter, system_title)),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()
    encryptor.authenticate_additional_data(unhexlify(aad))
    encryptor.finalize()

    data = encryptor.tag.hex()

    return data[:-8]


def cifra_decifra(system_title, frame_counter, encryption_key, aad, apdu):

    additional_auth_data = SECURITY_HEADER[1] + aad

    # Create AESGCM object
    aesgcm = AESGCM(unhexlify(encryption_key))

    apdu = aesgcm.encrypt(create_iv(frame_counter, system_title), unhexlify(apdu), unhexlify(additional_auth_data))

    apdu = apdu.hex()

    return apdu


def create_iv(frame_counter, system_title):

    # Concatenate System Title with Frame Counter
    return unhexlify(system_title + frame_counter)


def main():

    parser = argparse.ArgumentParser(description="Simple tool for encrypt and decrypt DLMS APDU", prog='DLMS CLI')

    parser.add_argument('-e', '--enc', nargs=5, help='Encrypt APDU')
    parser.add_argument('-d', '--dec', nargs=5, help='Decrypt APDU')
    parser.add_argument('-a', '--auth', nargs=5, help='Authenticate APDU')
    parser.add_argument('-k', '--key', action='store_true', help='Generate encryption key')

    args = parser.parse_args()

    if args.key:

        chiave = os.urandom(16).hex()
        print(f"Encryption Key: {chiave}")

    if args.enc:

        ret = cifra_decifra(args.enc[0], args.enc[1], args.enc[2], args.enc[3], args.enc[4])

        # Print encrypted or decrypted DLMS APDU
        print(f"Encrypted/Dcrypted APDU: {ret[:-32]}")
        print(f"Authentication TAG: {ret[-32:]}")

    if args.dec:

        ret = cifra_decifra(args.dec[0], args.dec[1], args.dec[2], args.dec[3], args.dec[4])

        # Print encrypted or decrypted DLMS APDU
        print(f"Encrypted/Dcrypted APDU: {ret[:-32]}")
        print(f"Authentication TAG: {ret[-32:]}")

    if args.auth:

        ret = auth_apdu(args.auth[0], args.auth[1], args.auth[2], args.auth[3], args.auth[4])

        print(f"TAG: {ret}")


if __name__ == "__main__":

    main()