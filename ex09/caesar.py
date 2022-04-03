import sys

def encryption(text, key):
	str_encryption = ""
	for i in range(len(text)): 
		char = text[i]
		if (char.isalpha() == True):
			if(char.isupper()):
				if (ord(char) + key > 90):
					str_encryption += chr((ord(char) + key - 26)) 
				else:
					str_encryption += chr((ord(char) + key))
			else:
				if (ord(char) + key > 122):
					str_encryption += chr((ord(char) + key) - 26)
				else:
					str_encryption += chr((ord(char) + key))
		else:
			str_encryption += char
	return (str_encryption)


def decryption(text, key):
	str_decryption = ""
	for i in range(len(text)): 
		char = text[i]
		if (char.isalpha() == True):
			if(char.isupper()):
				if (ord(char) - key < 65):
					str_decryption += chr((ord(char) - key + 26)) 
				else:
					str_decryption += chr((ord(char) - key))
			else:
				if (ord(char) - key < 97):
					str_decryption += chr((ord(char) - key) + 26)
				else:
					str_decryption += chr((ord(char) - key))
		else:
			str_decryption += char
	return (str_decryption)

def caesar(operating_mode, text, key):
	if (operating_mode == 'encode'):
		str_return = encryption(text, key)
	else:
		str_return = decryption(text, key)
	return (str_return)

if __name__ == "__main__":
	if (len(sys.argv) != 4):
		exit(1)
	if (sys.argv[3].isnumeric() == True):
		key = int(sys.argv[3])
		if (key > 0 and key < 24):
			key = key
		else:
			exit(1)
	else:
		exit(1)
	if (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
		exit(1)
	cipher_text = caesar(sys.argv[1], sys.argv[2], key)
	print(cipher_text)

