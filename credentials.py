import requests
import os
import argparse
import json
import sys


# import platform


def get_auth_info():
    if os.getenv('OS_AUTH_URL') is not None:
        OS_AUTH_URL = os.getenv('OS_AUTH_URL')
    else:
        print('Set OS_AUTH_URL Environmental Vairable')
        return -1, 'OS_AUTH_URL'
    if os.getenv('OS_IDENTITY_API_VERSION') is not None:
        OS_IDENTITY_API_VERSION = os.getenv('OS_IDENTITY_API_VERSION')
    else:
        print('Set OS_IDENTITY_API_VERSION Environmental Vairable')
        return -1, 'OS_IDENTITY_API_VERSION'
    if os.getenv('OS_PROJECT_NAME') is not None:
        OS_PROJECT_NAME = os.getenv('OS_PROJECT_NAME')
    else:
        print('Set OS_PROJECT_NAME Environmental Vairable')
        return -1, 'OS_PROJECT_NAME'
    if os.getenv('OS_PROJECT_DOMAIN_NAME') is not None:
        OS_PROJECT_DOMAIN_NAME = os.getenv('OS_PROJECT_DOMAIN_NAME')
    else:
        print('Set OS_PROJECT_DOMAIN_NAME Environmental Vairable')
        return -1, 'OS_PROJECT_DOMAIN_NAME'
    if os.getenv('OS_USERNAME') is not None:
        OS_USERNAME = os.getenv('OS_USERNAME')
    else:
        print('Set OS_USERNAME Environmental Vairable')
        return -1, 'OS_USERNAME'
    if os.getenv('OS_USER_DOMAIN_NAME') is not None:
        OS_USER_DOMAIN_NAME = os.getenv('OS_USER_DOMAIN_NAME')
    else:
        print('Set OS_USER_DOMAIN_NAME Environmental Vairable')
        return -1, 'OS_USER_DOMAIN_NAME'
    if os.getenv('OS_PASSWORD') is not None:
        OS_PASSWORD = os.getenv('OS_PASSWORD')
    else:
        print('Set OS_PASSWORD Environmental Vairable')
        return -1, 'OS_PASSWORD'
    if os.getenv('OS_REGION_NAME') is not None:
        OS_REGION_NAME = os.getenv('OS_REGION_NAME')
    else:
        print('Set OS_REGION_NAME Environmental Vairable')
        return -1, 'OS_REGION_NAME'
    headers = {'Content-Type': 'application/json'}
    body = {"auth": {
        "identity": {
            "methods": ["password"],
            "password": {
                "user": {
                    "name": OS_USERNAME,
                    "domain": {"name": OS_USER_DOMAIN_NAME},
                    "password": OS_PASSWORD
                }
            }
        },
        "scope": {
            "project": {
                "domain": {"name": OS_PROJECT_DOMAIN_NAME},
                "name": OS_PROJECT_NAME
            }
        }
    }
    }
    try:
        r = requests.post(OS_AUTH_URL + '/auth/tokens', headers=headers, data=json.dumps(body))
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    data = json.loads(r.text)
    for i in data['token']['catalog']:
        if i['type'] == 'network':
            endpoints = i['endpoints']
            for i in endpoints:
                if i['interface'] == 'public':
                    nw_manager_url = i['url']
    # print(r.headers['X-Subject-Token'])
    return r.headers['X-Subject-Token'], nw_manager_url


def get_lbs():
    auth_token, nw_manager_url = get_auth_info()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    try:
        r = requests.get(nw_manager_url + '/v2.0/lbaas/loadbalancers?project_id=f449ee4128c9411a8f22a736a73bf570',
                         headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    if r.status_code == 200:
        data = json.loads(r.text)
        lbs = data['loadbalancers']
        print(len(lbs))


def main():
    get_lbs()


if __name__ == '__main__':
    main()