"""
Password Security Tool - INFO 153B/253B Lab 1

Analyze password strength and generate secure passwords.

AUTHOR: Evan Vlahos

"""

import string
import random
import pandas as pd
import numpy as np
import re

# Common weak passwords
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley"
]


# ============================================
# TODO 1: Password Strength Checker
# ============================================

def check_password_strength(password):
    """
    Analyze password and return strength score.
    
    Scoring:
    - 8+ characters: 20 points
    - 12+ characters: 30 points (instead of 20)
    - Has number: 20 points
    - Has uppercase: 20 points
    - Has lowercase: 20 points
    - Has special char (!@#$%): 20 points
    - Not in common list: 10 points
    
    Returns:
        dict with keys: "password", "score", "strength", "feedback"
        
    Strength levels:
    - 0-39: "Weak"
    - 40-69: "Medium"
    - 70-100: "Strong"
    
    Example:
        >>> result = check_password_strength("Hello123!")
        >>> result["score"]
        90
        >>> result["strength"]
        "Strong"
    
    Hint: Use .isdigit(), .isupper(), .islower() and string.punctuation
    """
    score = 0
    if not password:
        score = 0
    else:
        if ((password in COMMON_PASSWORDS) == False):
            score = score + 10
        
        if ((len(password) >= 12)):
            score = score + 30
        elif ((len(password) >= 8)):
            score = score + 20
        
        special_characters = "!@#$%"
        has_num = False
        has_special_char = False
        has_upper = False
        has_lower = False

        for i in np.arange(len(password)):
            if (password[i].isdigit()):
                has_num = True
            elif (password[i].isupper()):
                has_upper = True
            elif (password[i].islower()): 
                has_lower = True
            elif (password[i] in special_characters):
                has_special_char = True
            
        has_arr = [has_num, has_special_char, has_upper, has_lower]
        score = score + (np.sum(has_arr) * 20)
    
    if ((score >= 0) and (score < 40)):
        return {"strength": "Weak", "score": score, "password": password, "feedback": "Your password is too weak."}
    elif ((score >= 40) and (score < 70)):
        return {"strength": "Medium", "score": score, "password": password, "feedback": "Your password is acceptable."}
    else:
        return {"strength": "Strong", "score": score, "password": password, "feedback": "Your password is strong."}
    pass


# ============================================
# TODO 2: Password Generator
# ============================================

def generate_password(length=12, use_special=True):
    """
    Generate a random secure password.
    
    Requirements:
    - Include uppercase, lowercase, and numbers
    - Include special characters if use_special=True
    - Minimum length: 8
    
    Args:
        length: Password length (default 12)
        use_special: Include special characters (default True)
    
    Returns:
        str: Generated password
    
    Example:
        >>> pwd = generate_password(10, True)
        >>> len(pwd)
        10
    
    Hint: Use string.ascii_uppercase, string.ascii_lowercase, 
          string.digits, and random.choice()
    """

    if (length < 8):         
        return "Password is too short. Must be at least 8 characters."    
    
    special_characters = "!@#$%"
    characters = string.ascii_letters + string.digits
    if (use_special):
        characters = characters + special_characters
    
    # make a password with 4 fewer characters to accomodate the 4 conditions
    result = ''.join(random.choice(characters) for _ in range(length - 4))

    # check to make sure we have at least a number, special character, uppercase, lowercase characters 
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for i in np.arange(len(result)):
        if (result[i].isdigit()):
            has_digit = True
        elif (result[i].isupper()):
            has_upper = True
        elif(result[i].islower()):
            has_lower = True
        elif (result[i] in special_characters):
            has_special = True

    # Check if the password has a digit in its string
    if (has_digit):
        # If it has a digit, just append another random character
        result = result + ''.join(random.choice(characters))
    else:
        # If there is no digit, append a random digit
        result = result + ''.join(random.choice(string.digits))

    # Check if the password has a special character in its string
    if (has_special or (use_special == False)):
        # If it has a special character or if the use_special flag is False, just append another random character
        result = result + ''.join(random.choice(characters))
    else:
        # If no special character is present, append a random special character from the special_characters list 
        result = result + ''.join(random.choice(special_characters))

    # Check if the password has an uppercase in its string
    if (has_upper):
        # If it has a uppercase, just append another random character
        result = result + ''.join(random.choice(characters))
    else:
        # If there is no uppercase, append a random uppercase letter
        result = result + ''.join(random.choice(string.ascii_uppercase))

    # Check if the password has an lowercase in its string
    if (has_lower):
        # If it has a lowercase, just append another random character
        result = result + ''.join(random.choice(characters))
    else:
        # If there is no lowercase, append a random lowercase letter
        result = result + ''.join(random.choice(string.ascii_lowercase))

    return result
    pass


# ============================================
# Simple Testing
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PASSWORD SECURITY TOOL - Quick Test")
    print("=" * 60 + "\n")
    
    # Check if functions are implemented
    try:
        # Test TODO 1
        result = check_password_strength("TestPassword123!")
        
        if result is None:
            print("❌ TODO 1 not implemented yet (returned None)")
            print("\nImplement check_password_strength() and try again.\n")
            exit()
        
        if not isinstance(result, dict):
            print("❌ TODO 1 should return a dictionary")
            exit()
        
        required_keys = ["password", "score", "strength", "feedback"]
        missing_keys = [key for key in required_keys if key not in result]
        
        if missing_keys:
            print(f"❌ TODO 1 missing keys in return dict: {missing_keys}")
            exit()
        
        print("✓ TODO 1 implemented - returns correct structure")
        print(f"  Example: '{result['password']}' → {result['strength']} ({result['score']}/100)")
        
        # Test TODO 2
        pwd = generate_password(12, True)
        
        if pwd is None:
            print("\n❌ TODO 2 not implemented yet (returned None)")
            print("\nImplement generate_password() and try again.\n")
            exit()
        
        if not isinstance(pwd, str):
            print("\n❌ TODO 2 should return a string")
            exit()
        
        print(f"\n✓ TODO 2 implemented - generates passwords")
        print(f"  Example: '{pwd}' (length: {len(pwd)})")
        
        # Success!
        print("\n" + "=" * 60)
        print("✅ Both functions implemented!")
        print("=" * 60)
        print("\nRun the full test suite to verify correctness:")
        print("  python test_password_tool.py")
        print()
        
    except AttributeError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure both functions are defined.\n")
    except Exception as e:
        print(f"❌ Error running functions: {e}")
        print("\nCheck your implementation and try again.\n")