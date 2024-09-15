from app.domain.entities.user import User

# In-memory user "database"
USERS_DB = {
    "user": User(username="user", password="password")
}

class UserAuthenticateService:
    @staticmethod
    def execute(username, password):
        user = USERS_DB.get(username)
        if user and user.check_password(password):
            return user
        return None
