import argparse
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

    parser = argparse.ArgumentParser(description="Simple tool for encrypt and decrypt DLMS APDU")
    parser.add_argument("system_title", type=str, help="System Title")
    parser.add_argument("frame_counter", type=str, help="Frame Counter")
    parser.add_argument("encryption_key", type=str, help="Encryption Key")
    parser.add_argument("authentication_key", type=str, help="Authentication Key")
    parser.add_argument("apdu", type=str, help="DLMS APDU")
    parser.add_argument("-a", "--auth", help="Authenticate data", action="store_true")
    args = parser.parse_args()

    if(args.auth):

        ret = auth_apdu(args.system_title, args.frame_counter, args.encryption_key, args.authentication_key, args.apdu)

        print(f"TAG: {ret}")

    else:

        ret = cifra_decifra(args.system_title, args.frame_counter, args.encryption_key, args.authentication_key, args.apdu)

        # Print encrypted or decrypted DLMS APDU
        print(f"Encrypted/Dcrypted APDU: {ret[:-32]}")
        print(f"Authentication TAG: {ret[-32:]}")

if __name__ == "__main__":

    main()