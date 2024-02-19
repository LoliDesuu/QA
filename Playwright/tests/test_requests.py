import requests
from tests.src.enums.global_enums import Error
from tests.src.config import *


def test_get_single_user() :
    request = requests.get(SINGLE_USER_URL, timeout = 1)
    if request.status_code == 200 :
        response = request.json()  
        assert (response['data']['id']) == 2, Error.response_value
        assert (response['data']['first_name']) == 'Janet', Error.response_value
        assert (response['data']['last_name']) == 'Weaver', Error.response_value
        assert request.status_code == 200, Error.status_code
    else :
        print(f'An error occured with statuse code: {request.status_code}')

def test_get_list_users() :
    request = requests.get(LIST_USER_URL, timeout = 0.5)
    response = request.json()
    assert (response['data'][1]['email']) == 'lindsay.ferguson@reqres.in', Error.response_value
    assert request.status_code == 200, Error.status_code

def test_get_not_found_user() :
    request = requests.get(NOT_FOUND_USER_URL, timeout = 0.5)
    assert request.status_code == 404, Error.status_code

def test_create_user() :
    request = requests.post(CREATE_USER_URL, data = CREATE_USER_DATA, timeout = 0.5)
    response = request.json()
    assert (response['name']) == 'Kate', Error.response_value
    assert (response['job']) == 'Banker', Error.response_value
    assert request.status_code == 201, Error.status_code

# def get_list_resource() :
#     request = requests.get('https://reqres.in/api/unknown', timeout = 0.5)
#     response = request.json()
#     assert (response['data'][2]['name']) == 'true red', Error.response_value
#     assert request.status_code == 200, Error.status_code
#     return(request)

# def get_single_resource() :
#     request = requests.get('https://reqres.in/api/unknown/23', timeout = 0.5)
#     response = request.json()
#     if not response.get(None):
#         Error.empty_value
#     assert request.status_code == 404, Error.status_code
#     return(request)

# def register() :
#     body = {
#     "email": "eve.holt@reqres.in",
#     "password": "pistol"
#     }
#     request = requests.post('https://reqres.in/api/register', data = body, timeout = 0.5)
#     response = request.json()
#     assert (response['id']) == 4, Error.response_value
#     assert (response['token']) == 'QpwL5tke4Pnpja7X4', Error.response_value
#     assert request.status_code == 200, Error.status_code
#     if response.get(None):
#         Error.empty_value
#     return(request)

# def get_single_user_not_found() :
#     request = requests.get('https://reqres.in/api/users/23', timeout = 0.5)
#     response = request.json()
#     if not response.get(None):
#         Error.empty_value
#     assert request.status_code == 404, Error.status_code
#     return(request)

# test_get_single_user()
# test_get_list_users()
# test_get_not_found_user()
# test_create_user()
# get_list_resource()
# get_single_resource()
# register()
# get_single_user_not_found()
