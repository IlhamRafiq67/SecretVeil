import os
from PIL import Image

def hide_message(image_path, message, output_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Get the dimensions of the image
    width, height = image.size

    # Convert the message to binary and add a termination character
    message += '\0'  # Null character as termination
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Check if the message can be hidden in the image
    if len(binary_message) > width * height * 3:
        print("Error: Message is too large to be hidden in the image.")
        return

    # Hide the message in the image
    hidden_image = image.copy()
    pixels = hidden_image.load()  # Use load() for faster pixel access

    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(binary_message):
                r, g, b = pixels[x, y]
                # Modify the least significant bit of the blue channel
                new_b = (b & 0xFE) | int(binary_message[index])
                pixels[x, y] = (r, g, new_b)
                index += 1
            else:
                break

    # Save the hidden image
    hidden_image.save(output_path)
    print(f"Message hidden in image and saved as: {output_path}")


def extract_message(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Get the dimensions of the image
    width, height = image.size

    # Extract the hidden message
    binary_message = ''
    pixels = image.load()  # Use load() for faster pixel access
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_message += str(b & 1)

    # Convert the binary message to text
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        if byte == '00000000':  # Null termination character found
            break
        message += chr(int(byte, 2))

    return message


def main():
    print("Welcome to the Steganography Tool!")
    while True:
        print("\nMenu:")
        print("1. Hide message in image")
        print("2. Extract message from image")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            image_path = input("Enter the path to the image file: ")
            message = input("Enter the message to hide: ")
            output_path = input("Enter the path to save the hidden image: ")
            hide_message(image_path, message, output_path)

        elif choice == '2':
            image_path = input("Enter the path to the image file: ")
            try:
                extracted_message = extract_message(image_path)
                if extracted_message:
                    print("Extracted Message:", extracted_message)
                else:
                    print("No message found.")
            except Exception as e:
                print(f"Error extracting message: {e}")

        elif choice == '3':
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

