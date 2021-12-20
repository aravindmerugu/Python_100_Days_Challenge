from caesar_cipher_art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text,shift,direction):
  if direction=='encode':
    lst_text = list(text)
    encode = ''
    for letter in lst_text:
      if letter in alphabet:
        index = alphabet.index(letter) + shift
        if index > 25:
          index = ((index+1) % 26)-1
        encode+=alphabet[index]
      else:
        encode+=letter  
    print(f"the encoded text is '{encode}'")  

  if direction=='decode':
    lst_text = list(text)
    decode = ''
    for letter in lst_text:
      if letter in alphabet:
        index = alphabet.index(letter) - shift
        if index < 0:
          index = ((index+1) % 26)-1
        decode+=alphabet[index]
      else:
        encode+=letter  
    print(f"the decoded text is '{decode}'")


to_run = True
while(to_run):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar_cipher(text,shift,direction)
  choose = input("Type 'YES' to continue or 'NO' to stop: ").lower()
  if choose == 'no':
    to_run = False