from clear_module import list
print(list)


direction=input("Tyoe 'encode' to encrypt, type 'decode' to decrypt: \n")
text =input("Type your message:\n").lower()
shift=int(input("TYpe the shift number:\n"))

# def encrypt(shift,test):
#     cipher_text=""
#     for letter in text:
#         position=list.index(letter)
#         new_postion=position + shift
#         new_letter=list[new_postion]
# # encrypt(shipt=shift,test=text)
#         cipher_text+=new_letter
#     print(f"The encoded text is {cipher_text}")
# # encrypt(shipt=shift,test=text)

# def decrypt(shift,test):
#     cipher_text=''
#     for letter in text:
#         position =list.index(letter)
#         new_postion=position - shift 
#         new_letter=list[new_postion]
#         cipher_text+=new_letter
#     print(f"The decoded text is {cipher_text}")
# if direction=="encode":
#     encrypt(shipt=shift,test=text)
# else:
#     decrypt(shift=shift,test=text)
# # else:
#     # print("Check ypur input")
def caesar(shift,test):
    new_letter=""
 
    for letter in text:
        if direction=="decode":
            shift*=-1
        position=list.index(letter)
        new_postion=position + shift
        new_letter+=list[new_postion]
# encrypt(shipt=shift,test=text)
        # cipher_text+=new_letter
    print(f"The {direction}d text is {new_letter}")
caesar(shift=shift,test=text)
