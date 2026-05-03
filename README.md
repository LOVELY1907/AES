# 🔐 AES Encryption & Decryption in Python

A simple Python project demonstrating **AES (Advanced Encryption Standard)** encryption and decryption using the `PyCryptodome` library.

---

## 🚀 Features

* AES encryption using **ECB mode**
* Automatic padding for block size (16 bytes)
* Base64 encoding for readable encrypted output
* Decryption back to original plaintext
* Random secure key generation

---

## 🧠 How It Works

1. User inputs a message
2. Message is padded to match AES block size (16 bytes)
3. AES encryption is applied
4. Encrypted data is encoded using Base64
5. Decryption reverses the process to retrieve the original message

---

## 📦 Installation

Make sure Python is installed, then install the required library:

```bash
pip install pycryptodome
```

---

## ▶️ Usage

Run the script:

```bash
python aes_proj.py
```

Example:

```bash
Enter message: HELLO LOVELY

Encrypted: k20NxhLEgOOMdSDicXml+w==
Decrypted: HELLO LOVELY
```

---

## 🛠️ Technologies Used

* Python 3
* PyCryptodome (`Crypto` module)
* Base64 Encoding

---

## ⚠️ Important Note (Security)

This project uses **AES in ECB mode**, which is **not secure for real-world applications** because:

* It does not use an IV (Initialization Vector)
* Patterns in plaintext can be exposed

👉 For real applications, use:

* AES-CBC or AES-GCM mode
* Proper key management

---

## 📁 Project Structure

```
aes_proj.py   # Main script for encryption & decryption
README.md     # Project documentation
```

---

## 💡 Future Improvements

* Switch to AES-CBC / AES-GCM
* Add IV handling
* File encryption support
* GUI interface
* Key storage mechanism

---

## 👨‍💻 Author

Lovely G

---

## ⭐ If you found this useful

Give this repo a star ⭐ and consider improving it further!
