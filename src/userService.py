from user import User
class UserService:
    def __init__(self):
        self.users = {}

    def register_user(self, username: str, password: str, role: str = "user") -> User:
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_id = len(self.users) + 1
        user = User(user_id, username, password_hash, role)
        self.users[username] = user
        return user

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = self.users.get(username)
        if user and user.check_password(password):
            return user
        return None
