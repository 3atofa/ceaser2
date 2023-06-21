alphapet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n" ,"o","p","k","r","s","t","u","v","w","x","y","z" ,"a","b","c","d","e","f","g","h","i","j","k","l","m","n" ,"o","p","k","r","s","t","u","v","w","x","y","z"]
sh = True

while sh:
 directions = input("type encode to encrypt type decode to decrypt:\n")
 text =input("input text\n").lower()
 shift = int(input("type sghift number to:\n"))
 if directions =="encode":
  def encrypt(plain_text ,shift_amount):
   cipher_text = ""
   for i in plain_text:
    position = alphapet.index(i)
    new_position =  position + shift_amount
    new_letter = alphapet[new_position]
    cipher_text += new_letter
   print(cipher_text)
  encrypt(text ,shift)
 if directions == "decode":
  def decrypt(plain_text ,shift_amount):
   decipher_text = ""
   for i in plain_text:
    position = alphapet.index(i)
    new_position =  position - shift_amount
    new_letter = alphapet[new_position]
    decipher_text += new_letter
   print(decipher_text)
  decrypt(text ,shift)
 type= input("would you like to continue:\n").lower()
 if  type=="no":
     sh=False