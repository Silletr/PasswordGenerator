from passwordgen import generate_password

for i in range(6):  # because array's starting from zero. I need 5 passwords
    print(f"Password number {i} with 46 symbols is:")
    print(generate_password(length=46))
