import pyAesCrypt
import os


def decryption(file: str, password: str) -> None:
    """Add patch to encrypted file and create decrypted file on data folder, after that removed original file"""

    # buffer size
    buffer_size = 512 * 1024

    # call decrypted function
    pyAesCrypt.decryptFile(
        f"./enc_data/{str(file)}",
        f"./data/{str(os.path.splitext(file)[0])}",
        password,
        buffer_size
    )

    os.remove(f"./enc_data/{str(file)}")

    print(f'[+] File {file} success decrypted.\nDecrypted file on "data" folder.')

