#!/usr/bin/env python3
"""
Authentication system
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
