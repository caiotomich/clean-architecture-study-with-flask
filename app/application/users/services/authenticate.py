from app.domain.entities.users.entity import User

# In-memory user "database"
USERS_DB = {
    "user": User(id="uuid", name="user test", email="user@email.com", password="bcrypt_password")
}

class UserAuthenticateService:
    @staticmethod
    def execute(email, password):
        user = USERS_DB.get(email)
        if user and user.check_password(password):
            return user
        return None
