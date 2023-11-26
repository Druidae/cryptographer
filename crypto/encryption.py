import os

import pyAesCrypt


def encryption(file: str, password: str) -> None:
    """Add path to file from data folder and create encrypted file on enc_data folder after that removed original file"""

    # buffer size
    buffer_size = 512 * 1024

    # call encrypted method
    pyAesCrypt.encryptFile(
        f"./data/{str(file)}",
        f"./enc_data/{str(file)}.crp",
        password,
        buffer_size
    )

    os.remove(f"./data/{str(file)}")

    print(f'[+] File {file} success encrypted.\nEncrypted file on "enc_data" folder.')
