

class TestUserGet():
    keys_for_check = ["username", "email", "firstName", "lastName"]

    def test_user_details_not_auth(self, app):
        r = app.methods.get("/api/user/2")
        app.checkers.check_json_has_key(r, self.keys_for_check[0])

        app.checkers.check_json_has_not_keys(r, self.keys_for_check[1:])

    def test_user_details_auth_as_some_user(self, app):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        r1 = app.methods.post("/api/user/login", data=data)

        auth_sid = app.core.get_cookie(r1, "auth_sid")
        token = app.core.get_header(r1, "x-csrf-token")
        user_id = app.core.get_json_value(r1, "user_id")

        r2 = app.methods.get(f"/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        app.checkers.check_json_has_keys(r2, self.keys_for_check)
