import pytest


class TestFirstApi:
    names = ["Vitalii", "Arseniy", ""]

    @pytest.mark.parametrize("name", names)
    def test_api(self, app, name):
        data = {"name": name}

        r = app.methods.get(url="/api/hello", params=data)

        assert r.status_code == 200, "Wrong response code"
        r_dict = r.json()
        assert "answer" in r_dict, "There's no field 'answer' in the response"

        if name != "":
            expected_r_text = f"Hello, {name}"
        else:
            expected_r_text = "Hello, someone"
        actual_r_text = r_dict["answer"]

        assert actual_r_text == expected_r_text, "Actual text in the response isn't correct"
