import requests


def test_get_API():
    URL = "http://reqres.in/api/users"

    Query_Params = {
        "page": 2
    }

    response = requests.get(URL, Query_Params)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200
