import pytest

list_methods = ["GET", "POST", "PUT", "DELETE", "HEAD"]


@pytest.mark.parametrize("method_request", list_methods)
@pytest.mark.parametrize("method_payload", list_methods)
def test_method(app, method_request, method_payload):

    if method_request == "GET":
        r = app.methods.get(url="/ajax/api/compare_query_type", params={"method": method_payload})

    else:
        r = app.methods._send(url="/ajax/api/compare_query_type", method=method_request,
                              data={"method": method_payload}, params=None, headers=None, cookies=None)

    assert "success" in r.text and method_payload == method_request, \
        f"method {method_request}, payload {method_payload}, result {r.text}"
