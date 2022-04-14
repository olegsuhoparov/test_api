import allure
import pytest


@allure.epic("Authorisation cases")
class TestUserRegister:


    @allure.description("Test create user successfully")
    def test_create_user_successfully(self, app):
        data = app.core.prepare_registration_data()
        r = app.methods.post("/api/user", data=data)

        app.checkers.check_status_code(r, 200)
        app.checkers.check_json_has_key(r, "id")

    @allure.description("Test create user with existing email")
    def test_create_user_with_existing_email(self, app):
        email = 'vinkotov@example.com'

        data = app.core.prepare_registration_data(email)

        r = app.methods.post("/api/user", data=data)

        app.checkers.check_status_code(r, 400)
        assert r.content.decode("utf-8") == f"Users with email '{email}' already exists"

    def test_create_user_with_incorrect_email(self, app):
        email = 'aweasegrexample.com'

        data = app.core.prepare_registration_data(email)

        r = app.methods.post("/api/user", data=data)

        app.checkers.check_status_code(r, 400)

    @pytest.mark.xfail
    @pytest.mark.parametrize("field", ["email", "password", "username", "firstName", "lastName"])
    def test_crate_user_without_one_of_fields(self, app, field):
        if field == "email":
            data = {
            'password': "password",
            'username': "username",
            'firstName': "firstname",
            'lastName': "lastname",
            'email': None
        }
        else:
            data = app.core.prepare_registration_data(exec("field"))

        r = app.methods.post("/api/user", data=data)
        print(field, exec("field"))
        app.checkers.check_status_code(r, 400)