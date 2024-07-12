#!/usr/bin/env python3
"""
class SessionAuth that inherits form Auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    class SessionAuth that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        id = str(uuid4())
        self.user_id_by_session_id[id] = user_id

        return id
