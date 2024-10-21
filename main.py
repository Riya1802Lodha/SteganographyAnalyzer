import os
from encoder import encode_image
from decoder import decode_image

def main():
    choice = input("Do you want to (e)ncode or (d)ecode a message? ").strip().lower()

    if choice == 'e':
        input_image = input("Enter the path of the image to encode: ")
        secret_message = input("Enter the message to encode: ")
        output_image = input("Enter the output path for the encoded image: ")
        encode_image(input_image, secret_message, output_image)
    elif choice == 'd':
        input_image = input("Enter the path of the image to decode: ")
        message = decode_image(input_image)
        print("Extracted Message:", message)
    else:
        print("Invalid choice. Please choose 'e' or 'd'.")

if __name__ == "__main__":
    main()
