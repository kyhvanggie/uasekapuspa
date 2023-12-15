from flask import Flask, render_template, request
from affine_cipher import encrypt_affine, decrypt_affine
from caesar_cipher import encrypt_caesar, decrypt_caesar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cipher_affine_caesar.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    key_affine = int(request.form['key_affine'])
    key_caesar = int(request.form['key_caesar'])

    # Apply Affine Cipher followed by Caesar Cipher
    ciphertext = encrypt_affine(plaintext, key_affine)
    ciphertext = encrypt_caesar(ciphertext, key_caesar)

    return render_template('cipher_affine_caesar.html', ciphertext=ciphertext)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    key_affine = int(request.form['key_affine'])
    key_caesar = int(request.form['key_caesar'])

    # Apply Caesar Cipher followed by Affine Cipher (in reverse order)
    decrypted_text = decrypt_caesar(ciphertext, key_caesar)
    decrypted_text = decrypt_affine(decrypted_text, key_affine)

    return render_template('cipher_affine_caesar.html', decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
