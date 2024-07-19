from faker import Faker


def generate_random_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    zip_code = fake.zipcode()

    return first_name, last_name, zip_code
