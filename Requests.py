import requests
import random
import json
import string

# base url
Base_URL = "https://gorest.co.in"

# Auth token
auth_token = "Bearer b13655c6e00d1164569137714f6d7600978c6191ce83c8c1c45b83db3e8ef315"

# Random email
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

# Get request
def get_request():
    url = Base_URL + "/public/v2/users"
    print("Get url:" + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("GET Response data:", json_str)
    print("Getting info of users done!!!!!!!!!!")
    print("=====================================================")

# Post request
def post_request():
    url = Base_URL + "/public/v2/users"
    print("Post url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Kavin api",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Response data:", json_str)
    user_id = json_data["id"]
    print("user id:=", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Kavin api"
    print("Creating new user done!!!!!!!!!!")
    print("=====================================================")
    return user_id


# Put request
def put_request(user_id):
    url = Base_URL + f"/public/v2/users/{user_id}"
    print("Put url:" + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Kaveen",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("PUT Response data:", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Kaveen"
    print("Updating user done!!!!!!!!!!")
    print("=====================================================")

# Delete request
def delete_request(user_id):
    url = Base_URL + f"/public/v2/users/{user_id}"
    print("Delete url:" + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("Delete user done!!!!!!!!!!")
    print("=====================================================")

# calling
get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)
