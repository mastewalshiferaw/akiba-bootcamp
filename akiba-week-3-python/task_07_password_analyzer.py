def check_min_length(password, min_length=8):
    return len(password) >= min_length

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"
    return any(char in special_characters for char in password)


def analyze_password(password, min_length=8):
    checks = {
        f"At least {min_length} characters": check_min_length(password, min_length),
        "At least one uppercase letter": check_uppercase(password),
        "At least one lowercase letter": check_lowercase(password),
        "At least one digit": check_digit(password),
        "At least one special character": check_special(password),
    }

    missing = [rule for rule, passed in checks.items() if not passed]
    passed = [rule for rule, passed in checks.items() if passed]

    return {
        "password": password,
        "is_valid": len(missing) == 0,
        "passed": passed,
        "missing": missing,
    }



test_passwords = [
    "short",                
    "alllowercase123",     
    "NOLOWERCASE123!",     
    "NoSpecialChar123",    
    "Str0ng#P@ssword2026", 
]

for pwd in test_passwords:
    result = analyze_password(pwd, min_length=8)
    print(f"Password: {result['password']}")
    print(f"Valid:    {result['is_valid']}")
    if result["missing"]:
        print(f"Missing:  {result['missing']}")
    else:
        print("Status:   All requirements met!")
    print("-" * 40)