
# SecretVeil

## Introduction
**SecretVeil** is a Python-based steganography tool that allows you to hide and extract secret messages in images. This simple yet powerful tool is perfect for anyone interested in learning or experimenting with steganography techniques.

## Features:
- Hide messages within images.
- Extract hidden messages from images.
- Supports common image formats like PNG and JPEG.

## Installation

To install and use **SecretVeil**, follow the steps below:

1. Clone this repository:
   ```bash
   git clone https://github.com/IlhamRafiq67/SecretVeil.git
   ```

2. Navigate into the project directory:
   ```bash
   cd SecretVeil
   ```

3. Install the required Python libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the tool, use the following command:

```bash
python3 SecretVeil.py
```

### Hiding a Message in an Image:
1. Choose option `1` in the menu to hide a message.
2. Enter the image path (for example, `image.png`).
3. Enter the message you wish to hide.
4. Specify the output path to save the modified image.

The tool will embed the message within the image and save the new image.

### Extracting a Message from an Image:
1. Choose option `2` to extract a hidden message from an image.
2. Enter the path of the image containing the hidden message.
3. The tool will display the hidden message on the screen.

## Requirements

This tool requires the following Python library:
- `Pillow`

To install it, run:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as long as the license terms are followed.

```

---

### Project Structure

1. **UpdSecretVeil.py**: The Python script containing the code for hiding and extracting messages.
2. **requirements.txt**: The file listing the required dependencies (Pillow).
3. **README.md**: The documentation file containing project details, installation steps, and usage instructions.
4. **LICENSE**: A file specifying the project’s MIT open-source license.

---

### `requirements.txt`

```txt
Pillow
```
