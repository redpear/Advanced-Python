# Project 4 - Qodo Code Analysis

class User:

    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

    def get_id(self) -> int:
        return self.id

    def get_username(self) -> str:
        return self.username

    def get_email(self) -> str:
        return self.email


# Create a user
user = User(1, "redpear", "redpear@mac.com")

# Get the user's ID
user_id = user.get_id()

# Display the result
print(f"User ID: {user_id}")