import cv2

def encode_image(image_path, secret_message, output_path):
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image file {image_path} not found.")
    
    encoded_image = image.copy()

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    binary_message += '1111111111111110'  # Delimiter to indicate end of message
    message_length = len(binary_message)

    data_index = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = list(encoded_image[i, j])
            for k in range(3):  # Loop over RGB channels
                if data_index < message_length:
                    # Modify the pixel value to embed the binary message
                    pixel[k] = (pixel[k] & 0xFE) | int(binary_message[data_index])
                    data_index += 1
            encoded_image[i, j] = tuple(pixel)
            if data_index >= message_length:
                break

    cv2.imwrite(output_path, encoded_image)
    print(f"Message encoded successfully into {output_path}!")
