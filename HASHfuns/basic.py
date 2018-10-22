from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "superpass"

hashed = bcrypt.generate_password_hash(password=password)
check = bcrypt.check_password_hash(hashed, 'wrongpass')
print(hashed)
print(check)

from werkzeug.security import generate_password_hash, check_password_hash

hashe = generate_password_hash('superpass')
print(hashe)
chck = check_password_hash(hashe, 'worrr')
print(chck)