from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key value to each pixel (mod 256 for RGB overflow)
    encrypted_array = (image_array + key) % 256

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted successfully and saved to {output_image_path}")


def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(input_image_path)
    encrypted_array = np.array(encrypted_image)

    # Decrypt the image by subtracting the key value from each pixel (mod 256 for RGB overflow)
    decrypted_array = (encrypted_array - key) % 256

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted successfully and saved to {output_image_path}")


if __name__ == "__main__":
    print("Welcome to the Image Encryption Tool!")
    print("Choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        input_path = input("Enter the path to the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter an encryption key (integer): "))
        encrypt_image(input_path, output_path, key)
    
    elif choice == "2":
        input_path = input("Enter the path to the image to decrypt: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (same as encryption key): "))
        decrypt_image(input_path, output_path, key)
    
    else:
        print("Invalid choice! Please enter 1 or 2.")
