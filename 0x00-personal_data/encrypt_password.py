#!/usr/bin/env python3
"""
Password Encryption and Validation Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        Generates a salted and hashed password.

        Args:
                password (str): A string containing the plain text
                password to be hashed.

        Returns:
                bytes: A byte string representing the salted, hashed password.
        """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed
