from string import digits


def validate_username(username: str) -> tuple[bool, str]:
    if " " in username:
        return False, "Username bo'sh jouydan iborat bo'lmaslik kerak."
    elif not username.isalpha():
        return False, "Username harflar iborat bo'lishi kerak."
    elif not username.islower():
        return False, "Username kichik harflardan iborat bo'lishi kerak."
    else:
        return True, ""


def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 4:
        return False, "Password kamida 4 ta belgidan iborak bolsin"

    digit_count = 0
    for d in digits:
        digit_count += password.count(d)

    if digit_count == 0:
        return False, "Password kamida 1 ta raqamdan iborak bo'lsin"

    return True, ""


def nomalize_full_name(full_name: str) -> str:
    return full_name.title()
