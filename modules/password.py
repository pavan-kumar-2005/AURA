import secrets
import string
def generate_password():
    characters=string.ascii_letters + string.digits + string.punctuation
    password="".join(secrets.choice(characters) for _ in range(12))
    return password