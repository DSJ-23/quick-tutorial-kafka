import random
import string

user_ids = list(range(1,101))
recipients_ids = list(range(1,101))

def generate_message() -> dict:
    random_user_id = random.randrange(1,101)

    recipients_ids_copy = recipients_ids.copy()

    recipients_ids_copy.remove(random_user_id)
    random_recepient_id = random.choice(recipients_ids_copy)

    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id': random_recepient_id,
        'message': message
    }

if __name__ == "__main__":
    a = generate_message()
    print(a)