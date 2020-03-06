def ceasar_cipher_2(encrypt):
    firstString = "abcdefghijklmnopqrstuvwxyz"
    secondString = "cdefghijklmnopqrstuvwxyzab"
    
    translation = encrypt.maketrans(firstString, secondString)
    decrypt = encrypt.translate(translation)
    return decrypt