password = input("Password: ")

end_msg = ""
allowed_special = "*-#"
forbidden_chars = "!@№$%^&()_+=[]{}|;:'\",.<>?/`~\\"

if len(password) < 8:
    end_msg += "Длина пароля меньше 8;\n"
if password.lower() == password:
    end_msg += "В пароле отсутствуют заглавные буквы;\n"
if password.upper() == password:
    end_msg += "В пароле отсутствуют строчные буквы;\n"
if not any(symbol.isdigit() for symbol in password):
    end_msg += "В пароле отсутствуют цифры;\n"
if not any(symbol in allowed_special for symbol in password):
    end_msg += "В пароле отсутствуют специальные символы;\n"
if any(symbol in forbidden_chars for symbol in password):
    end_msg += "В пароле используются непредусмотренные символы\n"
if end_msg == "":
    end_msg = "Надежный пароль"

print(end_msg)