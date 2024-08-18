

def create_user(user_data):
    user = User(user_id=generate_uuid(), name=user_data['name'], email=user_data['email'])
    user_repository.create_user(user)
