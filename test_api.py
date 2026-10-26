import requests


# def test_httpbin_get():
#     response = requests.get("http://httpbin.org")
#     assert response.status_code == 200
#     print("接口测试通过")
def test_login_and_get_user():
    login_data = {"email":"eve.holt@reqres.in",
                  "password":"cityslicka"}
    print("\n1. 开始发送POST登录请求...")
    response = requests.post("https://reqres.in/api/login",json = login_data)
    assert response.status_code == 200
    token = response.json()["token"]
    print(f"登录成功，拿到的Token是{token}")
    headers = {"Authorization":f"Bearer{token}"}
    user_response = requests.get("https://reqres.in/api/users/2",headers=headers)
    assert user_response.status_code == 200
    print(f"查到了用户信息:{user_response.json()['data']['first_name']}")


