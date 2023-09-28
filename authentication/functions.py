from .models import UserVerification


def generate_and_store_code(username, generate_unique_code=None):
    unique_code = generate_unique_code(username)
    UserVerification.objects.create(username=username, unique_code=unique_code)


def get_code_by_username(username):
    try:
        user_verification = UserVerification.objects.get(username=username)
        return user_verification.unique_code
    except UserVerification.DoesNotExist:
        return None

def update_code(username, generate_unique_code=None):
    unique_code = generate_unique_code(username)
    UserVerification.objects.filter(username=username).update(unique_code=unique_code)

def delete_verification(username):
    UserVerification.objects.filter(username=username).delete()