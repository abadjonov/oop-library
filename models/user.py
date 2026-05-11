class User:
    def __init__(self, id: str, username: str, password_hash: str, full_name: str):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.full_name = full_name

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash,
            "full_name": self.full_name,
        }
