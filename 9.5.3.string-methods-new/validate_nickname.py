import re

def validate_nickname(nickname: str) -> str:
    if not nickname.startswith('@') or not (5 <= len(nickname) <= 15):
        return "Incorrect"
    
    if re.match(r'^[a-z0-9]+$', nickname[1:]):
        return "Correct"
    
    return "Incorrect"

nickname = input().strip()
print(validate_nickname(nickname))
