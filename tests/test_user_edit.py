

class TestUserEdit:
    def test_edit_just_created_user(self, app):
        register_data = app.core.prepare_registration_data()
        r1 = app.methods.post("/api/user", data=register_data)

        app.checkers.check_status_code(r1, 200)
        app.checkers.check_json_has_key(r1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = app.core.get_json_value(r1, "id")

        login_data = {
            'email': email,
            'password': password
        }

        r2 = app.methods.post("/api/user/login", data=login_data)

        auth_sid = app.core.get_cookie(r2, "auth_sid")
        token = app.core.get_header(r2, "x-csrf-token")

        new_name = "changed_name"
        r3 = app.methods.put(f"/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},
                         data={"firstName": new_name})

        app.checkers.check_status_code(r3, 200)

        r4 = app.methods.get(f"/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        app.checkers.check_json_value_by_name(r4, "firstName", new_name, "Wrong name of user after edit")
