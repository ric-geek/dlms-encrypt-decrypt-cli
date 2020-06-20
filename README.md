# Dlms encrypt-decrypt CLI
This simple tool allow you to easly encrypt or decrypt DLMS APDU

## Installation
Use pip:
```
pip install setup.py
```
## Usage
### Encrypt
**Example**\
System Title = 5249435249435249\
Frame Counter = 80000001\
Encryption Key = 454E4352595054494F4E4B45594B4559\
Authentication Key = 41555448454E5449434154494F4E4B45\
APDU = c001810001000060010aff0200
```
dlms_cli 5249435249435249 80000001 454E4352595054494F4E4B45594B4559 41555448454E5449434154494F4E4B45 c001810001000060010aff0200
```
Result
```
Encrypted/Decrypted APDU: 0de63f2331a09aa85e8830f5f3
Authentication TAG: 610d47e1e24b14e8a022aefc6a43f3a3
```
### Decrypt
**Example**\
System Title = 5249435249435249\
Frame Counter = 80000001\
Encryption Key = 454E4352595054494F4E4B45594B4559\
Authentication Key = 41555448454E5449434154494F4E4B45\
APDU = 0de63f2331a09aa85e8830f5f3
```
dlms_cli 5249435249435249 80000001 454E4352595054494F4E4B45594B4559 41555448454E5449434154494F4E4B45 0de63f2331a09aa85e8830f5f3
```
Result
```
Encrypted/Decrypted APDU: c001810001000060010aff0200
Authentication TAG: 977d4d21b7255a1b681fe6b1c902a7dc
```
## Dependency
[cryptography](https://github.com/pyca/cryptography)

## License
MIT