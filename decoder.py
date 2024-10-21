import cv2

def decode_image(image_path):
    image = cv2.imread(image_path)
    binary_message = ''
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            for k in range(3):
                binary_message += str(pixel[k] & 1)

    # Split the binary message into 8-bit chunks and convert to characters
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111111':  # Stop when we reach the delimiter
            break
        message += chr(int(byte, 2))

    return message


if __name__ == "__main__":
    extracted_message = decode_image('images/encoded_image.png')
    print("Extracted Message:", extracted_message)
