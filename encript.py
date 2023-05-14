import os
import pyAesCrypt

def crypter(_mode, _file):
    password = input('Введите пароль:')
    buffer = 512 *1024
    ext = _file.split('.')

    if (int(_mode) == 0):
        pyAesCrypt.encryptFile(_file, ext[0].lower() + '.cw', password, buffer)

    elif(int(_mode) == 1):
        _tipe = input('Введите тип:')
        pyAesCrypt.decryptFile(_file, ext[0].lower() + '.' + _tipe, password, buffer)

    os.remove(_file)

print('---shifr---')
print('0-crypt')
print('1-decrypt')

mode = input('выберите мод:')
filename = input('Введите название файла:')
crypter(mode, filename)