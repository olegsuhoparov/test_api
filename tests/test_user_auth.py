import pytest


class TestUserAuth:
    exclude_params = ("no_cookie", "no_token")

    def test_user_auth(self, app):
        app.core.auth()
        r2 = app.methods.get("/api/user/auth", headers={"x-csrf-token": app.core.token},
                            cookies={"auth_sid": app.core.auth_sid})

        assert "user_id" in r2.json()
        app.checkers.check_json_value_by_name(r2, "user_id", app.core.user_id,
                                          "User id from auth method and from check method isn't equals")

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, app, condition):
        app.core.auth()

        if condition == "no_cookie":
            r2 = app.methods.get("/api/user/auth", headers={"x-csrf-token": app.core.token})
        else:
            r2 = app.methods.get("/api/user/auth", cookies={"auth_sid": app.core.auth_sid})

        app.checkers.check_json_value_by_name(r2, "user_id", 0,
                                          "User id from auth method and from check method isn't equals")
