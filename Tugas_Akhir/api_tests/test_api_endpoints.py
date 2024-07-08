import requests

def test_get_employees():
    url = "https://api.orangehrm.com/employees"
    headers = {"Authorization": "Bearer <API_KEY>"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.json())

if __name__ == "__main__":
    test_get_employees()
