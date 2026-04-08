from generator import generate_base

for i in range(6):  # because array's starting from zero. I need 5 passwords
    print(f"Password number {i}, 16 symbols is:")
    print(generate_base(16))
