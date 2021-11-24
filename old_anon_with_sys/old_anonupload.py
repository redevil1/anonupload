import sys
import os
import click
import requests
import json

def main():
    url = 'https://api.anonfiles.com/upload'

    if len(sys.argv) == 1:
        print("[ERROR] You need to specify one or more files!")

    for filename in sys.argv[1:]:
        if os.path.isdir(filename):
            print('[ERROR] You cannot upload a directory!')
            break
        else:
            if click.confirm("Do you want change file name", default=False):
                input_name = input("Enter new file name with extension: ")
                try:
                    os.rename(filename, input_name)
                except FileNotFoundError:
                    print(f'[ERROR] The file "{filename}" doesn\'t exist!')
                    break

                try:
                    files = {'file': (open(input_name, 'rb'))}
                except FileNotFoundError:
                    print(f'[ERROR] The file "{input_name}" doesn\'t exist!')
                    break
            else:
                try:
                    files = {'file': (open(filename, 'rb'))}
                except FileNotFoundError:
                    print(f'[ERROR] The file "{filename}" doesn\'t exist!')
                    break

        if (os.path.isfile(filename)==False):
            print("[UPLOADING]", input_name)
        else:
            print("[UPLOADING]", filename)

        r = requests.post(url, files=files)
        
        resp = json.loads(r.text)
        if resp['status']:
            urlshort = resp['data']['file']['url']['short']
            urllong = resp['data']['file']['url']['full']
            print(f'[SUCCESS] Your file has been succesfully uploaded:\nFull URL: {urllong}\nShort URL: {urlshort}')
        else:
            message = resp['error']['message']
            errtype = resp['error']['type']
            print(f'[ERROR] {message}\n{errtype}')

if __name__ == '__main__':
    main()