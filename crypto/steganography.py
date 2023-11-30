from stegano import exifHeader

def encrypt_sten(file_1, file_2, info):
    secret = exifHeader(f"img/{file_1}", f"img/{file_2}", info)

def decrypt_sten(file):
    result = exifHeader.reveal(f"img/{file}").decode()
    
    return result