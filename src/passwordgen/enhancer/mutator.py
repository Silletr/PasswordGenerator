import secrets
import string


def ensure_min_digits(password: str, min_digits: int = 1) -> str:
    while sum(c.isdigit() for c in password) < min_digits:
        pos = secrets.randbelow(len(password))
        password = password[:pos] + secrets.choice(string.digits) + password[pos + 1 :]
    return password


def ensure_min_uppercase(password: str, min_upper: int = 1) -> str:
    chars = string.ascii_uppercase
    while sum(c.isupper() for c in password) < min_upper:
        pos = secrets.randbelow(len(password))
        password = password[:pos] + secrets.choice(chars) + password[pos + 1 :]
    return password


def ensure_min_lowercase(password: str, min_lower: int = 1) -> str:
    chars = string.ascii_lowercase
    while sum(c.islower() for c in password) < min_lower:
        pos = secrets.randbelow(len(password))
        password = password[:pos] + secrets.choice(chars) + password[pos + 1 :]
    return password


def ensure_min_symbols(password: str, min_symbols: int = 1) -> str:
    chars = string.punctuation
    while sum(c in chars for c in password) < min_symbols:
        pos = secrets.randbelow(len(password))
        password = password[:pos] + secrets.choice(chars) + password[pos + 1 :]
    return password


def apply_policy(
    password: str,
    min_digits: int = 1,
    min_upper: int = 1,
    min_lower: int = 1,
    min_symbols: int = 1,
) -> str:
    password = ensure_min_digits(password, min_digits)
    password = ensure_min_uppercase(password, min_upper)
    password = ensure_min_lowercase(password, min_lower)
    password = ensure_min_symbols(password, min_symbols)
    return password
