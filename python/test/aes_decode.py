#coding:utf-8
import base64
from Crypto.Cipher import AES
import binascii
import json #注：python3 安装 Crypto 是 pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome<br><br>
#解密
def aes_decode(data, key):
    try:
        aes = AES.new(str.encode(key), AES.MODE_ECB) # 初始化加密器
        decrypted_text = aes.decrypt(data) # 解密
        decrypted_text = decrypted_text[:-(decrypted_text[-1])]
    except Exception as e:
        print(e)
    return decrypted_text



if __name__ == '__main__':
    key = 'e45e329feb5d925b' # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    data="bcc3WtES9X8i/azpzxLNzHsb0s9eQIfj2qDW/r5OeNJjI0AyF8zGcTflsJ6gHqP9zRX29Jgou+JjFOuGhPvy3btK1A/RJ4etXhshdIDJECBMbhT/DbonVEkG+/BfcqKB9NQcCHInyNBiAmyQnTazWoYjTSAqvwrDSJrkJwN5F/YZjG+uVUkqLLpMdUqzBwhBY+jkuBRF83sUkzdPcXPnxWSxxY6G9AGEbbW2Dcu2KG3zqeaNMZoci7sZ4NolS9nKnS7TBnGpDY2HgmwrwDVEaZVTEEsisrUySQCDCkO+2CNUw4Jf2rD7mNYmtt1Yn85LkH7aNJz+LFThtUXM79etcr6HQay7XH6ZGMw6Q74kJd8L1OImMpNDIORULoQIFADbk7+LoNynoOkGNc92R+kUEyzDlYHAOkmJkXWwyrb2jkX6J0Vp34kXfncm1e788hiwXJUepVCaCeYSlqa+ogXDkXsisD86ROUZkTEJfeUMC7YdD50AzAgr1WRhsaV8a3xesvAC5iQwzHGAvVWiN7u+e8GiFbt6OIYIBvQNKzJdfF8z695EPQgmyixyakrFi9wh10bbud2NVUPFvfw29/z4/utltfgLmrTUQWZZnmEIuKCpj43DSgZI3079Yz5ZzctfFhOQyX68Z9qRL5weyIQxUFOYV9f55/+AJtQzUGorckSz/8zjYuF3/SvTFFM6oFVC/g+MSsNigivZuKFUn01DgeGWsjZNnih3gBaXgbZnR8+BF1qnU6hqxrLfYYA+rjogQykfs3jeTF9qNNpah6wUOEKRngAunMWCE9pnBj0E4buC/nIfKZpl8cJKgUencoppW8U+8KfpXq8vZnZGliMzKNbBMzlduT/+VN0SAJGuFKyEINxI4HbR7SE2trcu+zz7W+WjLkRxRpEc5x6nbzXa3dkmNKmFjQDc0pgFvVixGxNPU08s8CUqiAK7+CMoBmrExk5r3GqFoE38zVdJ/9GOTkM3Av1wgwO1FnkgCIEX3aGm7Dq6kvh1HAKulBhXT7sWE75zYYqDL2KdtYLokBiBiLdySetlCCaxs2r4okocqN4a8EyIGVMVB6D2yg2ljIJ0jP1NOXX1MuYF7Tgy/4V2hIFn5V2vmZSuNLHdWVBHr8YCLkbHbGiMnjiSOFSxJollsFEA2B5lHmOykAdDV787z8axDBXvbzlFPFvU8Kk2fkVfRmuTJ5TGv91aFNWs9kDdKZ4ynEp9GEzUk9pOffDGKbfPp2jPYmEFWOC3qrQ/v02BWwAPStRjAEft5JZH0vYxn3b+GgQ+UGbrKJJutS1vvkAuvKFKEcDuliowh/C9FsY01ml1Uby0pT1CGV/fo2ZSdfYtpTTNOIB6BeZqQUv4LPSfh4bE0f2XVx3awihuSuy1KA7Jnlx1q2v/1Ses0Y3ib+MzPj7E2KPrCP17uktzKKit84L7edChTYbtoXcW83XJfdSPiuxZ92E3HBS6qvY1y4IgwAn7zYmyGEfPOH/UJkx4cnuLEU6nSp2D0xr"