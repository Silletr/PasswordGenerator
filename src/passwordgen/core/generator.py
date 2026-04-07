import secrets
import string


def generate_base(length=32):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(chars) for _ in range(length))
    print(password)
    return password


if __name__ == "__main__":
    generate_base()
