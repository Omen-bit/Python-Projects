alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text,shift):
#     ciphered_text=""
#
#     for letters in text:
#         if letters in alphabets:
#             shifted_idx=(alphabets.index(letters)+shift) % 26
#             ciphered_text+=alphabets[shifted_idx]
#
#         else:
#             ciphered_text+=letters
#
#     return ciphered_text
#
# def decrypt(text2,shift):
#     ciphered_text=""
#
#     for letters in text2:
#         if letters in alphabets:
#             shifted_idx=(alphabets.index(letters)-shift) % 26
#             ciphered_text+=alphabets[shifted_idx]
#
#         else:
#             ciphered_text+=letters
#
#     return ciphered_text

def casear(text,shift,choice):
    ciphered_text = ""

    if choice=="decode":
        shift*=-1

    for letters in text:
        if letters in alphabets:
             shifted_idx=(alphabets.index(letters)+shift)
             ciphered_text+=alphabets[shifted_idx]

        else:
             ciphered_text+=letters

    return ciphered_text


print("Welcome to Caesar Cipher, type encode to encrypt a message or decode to decrypt a message")
choice=input("->>").lower()
text = input("Enter a message to encode :").lower()
shift = int(input("Enter shift number :"))

result=casear(text,shift,choice)
print(result)
# if choice=="encode":
#     text = input("Enter a message to encode :").lower()
#     shift = int(input("Enter shift number :"))
#     result =encrypt(text, shift)
#     print(result)
# elif choice=="decode":
#     text2 = input("Enter a message to decode :").lower()
#     shift = int(input("Enter shift number :"))
#     result2=decrypt(text2,shift)
#     print(result2)
# else:
#     print("Invalid choice")