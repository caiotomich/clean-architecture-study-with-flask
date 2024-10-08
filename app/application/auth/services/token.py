import datetime, jwt, os
from app.domain.entities.users.entity import User

class Token:
    @staticmethod
    def generate(user: User):
        token = jwt.encode({
            'user': user.email,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=300)
        }, os.getenv('SECRET_KEY'), algorithm="HS256")
        return token

    @staticmethod
    def decode(token):
        try:
            token = token.replace('Bearer ', '')
            decoded_data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
            return decoded_data['user']
        except jwt.ExpiredSignatureError as e:
            raise Exception('Token has expired!')
        except jwt.InvalidTokenError as e:
            raise Exception('Invalid token!')
