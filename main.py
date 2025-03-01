import base64, random, sys, json, string, pyperclip, geocoder, requests
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLineEdit, QLabel, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui_main import Ui_has_mari


class PasswordManager(QMainWindow):
    def __init__(self):
        super(PasswordManager, self).__init__()
        self.ui = Ui_has_mari()
        self.ui.setupUi(self)
        self.current_language = 'en'
        self.setWindowTitle("Password Manager")
        self.setWindowIcon(QIcon("icon.png"))

        self.ui.encrypt.clicked.connect(self.encrypt)
        self.ui.decrypt.clicked.connect(self.decrypt)
        self.ui.file_input.clicked.connect(self.import_file)
        self.ui.password_generator.clicked.connect(self.generate_password)

        self.update_ui_texts()

    def update_ui_texts(self):
        if self.current_language == 'ru':
            self.setWindowTitle("Менеджер паролей")
            self.ui.encrypt.setText("Зашифровать")
            self.ui.decrypt.setText("Расшифровать")
            self.ui.file_input.setText("Импорт файла")
            self.ui.password_generator.setText("Генератор паролей")
            self.ui.input.setPlaceholderText("Введите пароль...")
            self.ui.output.setText("Ожидание...")
        else:
            self.setWindowTitle("Password Manager")
            self.ui.encrypt.setText("Encrypt")
            self.ui.decrypt.setText("Decrypt")
            self.ui.file_input.setText("Import File")
            self.ui.password_generator.setText("Generate Password")
            self.ui.input.setPlaceholderText("Enter password...")


    def get_public_ip(self):
        try:
            return requests.get('https://api64.ipify.org?format=json').json()['ip']
        except Exception as e:
            return None

    def get_location(self) -> None:
        ip_address = self.get_public_ip()
        g = geocoder.ip(ip_address)
        if g.ok and g.country == "RU" and self.current_language != 'ru':
            reply = QMessageBox.question(
                self,
                "Язык" if self.current_language == 'ru' else "Language",
                "Хотите переключиться на русский язык?" if self.current_language == 'ru' else "Do you want to switch to Russian?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.current_language = 'ru'
                self.update_ui_texts()

    def import_file(self) -> None:
            file_path, _ = QFileDialog.getOpenFileName(self)
            if file_path:
                if not file_path.endswith('.txt'):
                    QMessageBox.warning(
                        self,
                        "Ошибка" if self.current_language == 'ru' else "Error",
                        "Пожалуйста, выберите .txt файл" if self.current_language == 'ru' else "Please select a .txt file"
                    )
                else:
                    QMessageBox.information(
                        self,
                        "Файл выбран" if self.current_language == 'ru' else "File Selected",
                        f"Выбран файл: {file_path}" if self.current_language == 'ru' else f"Selected file: {file_path}"
                    )
                    try:
                        with open(file_path) as file:
                            data = [line.rstrip() for line in file]
                            self.encrypt_for_files(data)
                    except Exception as e:
                        QMessageBox.critical(
                            self,
                            "Ошибка" if self.current_language == 'ru' else "Error",
                            f"Ошибка чтения файла: {e}" if self.current_language == 'ru' else f"File read error: {e}"
                        )

    def encrypt_for_files(self, non_encrypted_inputted_password) -> None:
        encrypted_data = []

        keys = self.load_keys_from_json()

        if keys is None:
            keys = self.key_generator()
            encrypted = keys[1].encrypt(non_encrypted_inputted_password.encode('utf-8'),
                                        padding.OAEP(
                                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(), label=None))
            encrypted_data.append(base64.b64encode(encrypted).decode('utf-8'))

            self.save_in_json(" ".join(encrypted_data), keys[0], keys[1])

        else:
            encrypted = keys[1].encrypt(non_encrypted_inputted_password.encode('utf-8'),
                                        padding.OAEP(
                                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(), label=None))
            encrypted_data.append(base64.b64encode(encrypted).decode('utf-8'))

            self.save_passwords_in_json(" ".join(encrypted_data))

        self.set_data_in_qlabel(" ".join(encrypted_data))

    def get_data_from_qlineedit(self):
        data_in = self.ui.input.text()
        return data_in

    def set_data_in_qlabel(self, data) -> None:
        self.ui.output.setWordWrap(True)
        self.ui.output.setText(data)

    def save_passwords_in_json(self, encrypted_password) -> None:
        with open('config.json', 'r') as file:
            data = json.load(file)
            data["encrypted_passwords"].append(encrypted_password + "\n")
            with open('config.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

    def save_in_json(self, encrypted_data, private_key, public_key) -> None:
        encrypted_passwords = []
        encrypted_passwords.append(encrypted_data)
        config_json = {
            "encrypted_passwords": encrypted_passwords,
            "private": private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8'),
            "public": public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')
        }

        with open('config.json', 'w') as json_file:
            json.dump(config_json, json_file, indent=4)

    def load_passwords_from_json(self):
        with open('config.json', 'r') as file:
            data = json.load(file)
            return data["encrypted_passwords"]

    def load_keys_from_json(self):
        try:
            with open('config.json', 'r') as file:
                keys_output = []
                keys_data = json.load(file)
                public_key = keys_data.get('public')
                private_key = keys_data.get('private')
                if public_key is None or private_key is None:
                    return None
                pub_key = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
                priv_key = serialization.load_pem_private_key(private_key.encode(), password=None,
                                                              backend=default_backend())

                keys_output.append(priv_key)
                keys_output.append(pub_key)

                return keys_output
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None
        return None

    def key_generator(self):
        key_generator_output = []
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        public_key = private_key.public_key()

        # Сохранение ключей в файлы
        with open('private_key.pem', 'wb') as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open('public_key.pem', 'wb') as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        key_generator_output.append(private_key)
        key_generator_output.append(public_key)

        return key_generator_output

    def encrypt(self) -> None:
        non_encrypted_inputted_password = self.get_data_from_qlineedit()
        encrypted_data = []

        keys = self.load_keys_from_json()

        if keys is None:
            keys = self.key_generator()
            encrypted = keys[1].encrypt(non_encrypted_inputted_password.encode('utf-8'),
                                        padding.OAEP(
                                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(), label=None))
            encrypted_data.append(base64.b64encode(encrypted).decode('utf-8'))

            self.save_in_json(" ".join(encrypted_data), keys[0], keys[1])

        else:
            encrypted = keys[1].encrypt(non_encrypted_inputted_password.encode('utf-8'),
                                        padding.OAEP(
                                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                            algorithm=hashes.SHA256(), label=None))
            encrypted_data.append(base64.b64encode(encrypted).decode('utf-8'))

            self.save_passwords_in_json(" ".join(encrypted_data))

        self.set_data_in_qlabel(" ".join(encrypted_data))

    def decrypt(self) -> None:
        keys = self.load_keys_from_json()
        if keys is None or len(keys) == 0:
            QMessageBox.information(
                self,
                "Ошибка" if self.current_language == 'ru' else "Error",
                "Ошибка загрузки ключей" if self.current_language == 'ru' else "Key loading error"
            )
        else:
            encrypted_data = self.load_passwords_from_json()
            decrypted_data = []
            for data in encrypted_data:
                data = data.strip()
                encrypted_bytes = base64.b64decode(data)
                decrypted_data.append(keys[0].decrypt(encrypted_bytes,
                                                      padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                   algorithm=hashes.SHA256(),
                                                                   label=None)).decode('utf-8'))
            pyperclip.copy(" ".join(decrypted_data))
            self.set_data_in_qlabel(" ".join(decrypted_data))
            QMessageBox.information(
                self,
                "Расшифровка завершена" if self.current_language == 'ru' else "Decryption Complete",
                "Пароли скопированы в буфер обмена" if self.current_language == 'ru' else "Passwords copied to clipboard"
            )

    def generate_password(self) -> None:
        length = 32

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        all_characters = lowercase + uppercase + digits + special_characters

        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special_characters)
        ]

        password += random.choices(all_characters, k=length - 4)

        random.shuffle(password)

        self.set_data_in_qlabel(''.join(password))
        pyperclip.copy(''.join(password))
        QMessageBox.information(
            self,
            "Пароль создан" if self.current_language == 'ru' else "Password Created",
            "Пароль скопирован в буфер обмена" if self.current_language == 'ru' else "Password copied to clipboard"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    window.get_location()
    sys.exit(app.exec())
