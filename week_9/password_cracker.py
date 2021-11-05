from zipfile import ZipFile
import zlib

with open('Ashley-Madison.txt', 'r') as t:
    passwords = []
    for line in t:
        passwords.append(line.replace('\n', ''))

with ZipFile('whitehouse_secrets.zip') as zf:
    for password in passwords:
        password = bytes(password, 'UTF-8')

        try:
            zf.extractall(pwd=password)
            print('password=', password)
            break

        except RuntimeError:
            pass
        except zlib.error:
            pass
