import requests
import os
import json
import sys


def get_auth_info():
    if os.getenv('OS_AUTH_URL') is not None:
        OS_AUTH_URL = os.getenv('OS_AUTH_URL')
    else:
        print('Set OS_AUTH_URL Environmental Variable')
        return -1, 'OS_AUTH_URL'
    if os.getenv('OS_PROJECT_NAME') is not None:
        OS_PROJECT_NAME = os.getenv('OS_PROJECT_NAME')
    else:
        print('Set OS_PROJECT_NAME Environmental Variable')
        return -1, 'OS_PROJECT_NAME'
    if os.getenv('OS_PROJECT_DOMAIN_NAME') is not None:
        OS_PROJECT_DOMAIN_NAME = os.getenv('OS_PROJECT_DOMAIN_NAME')
    else:
        print('Set OS_PROJECT_DOMAIN_NAME Environmental Variable')
        return -1, 'OS_PROJECT_DOMAIN_NAME'
    if os.getenv('OS_USERNAME') is not None:
        OS_USERNAME = os.getenv('OS_USERNAME')
    else:
        print('Set OS_USERNAME Environmental Variable')
        return -1, 'OS_USERNAME'
    if os.getenv('OS_USER_DOMAIN_NAME') is not None:
        OS_USER_DOMAIN_NAME = os.getenv('OS_USER_DOMAIN_NAME')
    else:
        print('Set OS_USER_DOMAIN_NAME Environmental Variable')
        return -1, 'OS_USER_DOMAIN_NAME'
    if os.getenv('OS_PASSWORD') is not None:
        OS_PASSWORD = os.getenv('OS_PASSWORD')
    else:
        print('Set OS_PASSWORD Environmental Variable')
        return -1, 'OS_PASSWORD'

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
            for j in endpoints:
                if j['interface'] == 'public':
                    nw_manager_url = j['url']
    return r.headers['X-Subject-Token'], nw_manager_url


def get_floatip():
    auth_token, nw_manager_url = get_auth_info()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    try:
        r = requests.get(nw_manager_url + '/v2.0/lbaas/floatingips?project_id=f449ee4128c9411a8f22a736a73bf570',headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    if r.status_code == 200:
        data = json.loads(r.text)
        for p in data['floatingips']:
            if p in ['floatingips']['fixed_ip_address'] == 'null':
                max_count = len(p)
                print("Total no.of free floating ips available= ", max_count)
			


def total_floatip():
    auth_token, nw_manager_url = get_auth_info()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    try:
        p = requests.get(nw_manager_url + '/v2.0/quotas/f449ee4128c9411a8f22a736a73bf570', headers=headers)
    except requests.exceptions.RequestException as f:
        print(f)
        sys.exit(1)
    if p.status_code == 200:
        data1 = json.loads(p.text)
        print("Total quota available for LBs =", data1['quota']['floatingip'])


def main():
    get_floatip()
    total_floatip()


if __name__ == '__main__':
    main()
