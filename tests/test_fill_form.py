from model.registration_page import RegistrationPage

first_name = 'Santa'
last_name = 'Claus'
email = f'{first_name}@mail.com'
user_number = '1234567890'
birth_day = '11'
birth_month = 'April'
birth_year = '2007'
gender = "Male"
subjects = 'Maths'
hobby = 'Reading'
picture = 'pic.webp'
address = 'Zamshina street, 11/5'
state = 'NCR'
city = 'Noida'


def test_fill_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name(first_name)
    registration_page.fill_last_name(last_name)
    registration_page.fill_email(email)
    registration_page.select_gender(gender)
    registration_page.fill_user_number(user_number)
    registration_page.select_date_of_birth(birth_month, birth_year)
    registration_page.fill_subjects(subjects)
    registration_page.select_hobbies(hobby)
    registration_page.upload_picture(picture)
    registration_page.fill_address(address)
    registration_page.select_state(state)
    registration_page.select_city(city)

    registration_page.submit()

    registration_page.should_have_registered(first_name, last_name, email, gender, user_number, birth_day, birth_month,
                                             birth_year, subjects, picture, address, state, city)


