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
        if i['type'] == 'resources':
            endpoints = i['endpoints']
            for j in endpoints:
                if j['interface'] == 'public':
                    limes_url = j['url']
    return r.headers['X-Subject-Token'], limes_url


def get_resources():
    auth_token, limes_url = get_auth_info()
    headers = {'Content-Type': 'application/json', 'X-Auth-Token': auth_token}
    try:
        r = requests.get(limes_url + '/v1/domains/ab5617f02fef4ba7937bda0c58da1471/projects/f449ee4128c9411a8f22a736a73bf570',headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    if r.status_code == 200:
        data = json.loads(r.text)
        for p in data['project']['services']:
            if p['type'] == 'network' and p['area'] == 'network':
                resources = p['resources']
                for q in resources:
                    if q['name'] == 'floating_ips':
                        print("\nQuota available for Floatingips : \nTotal quota is = {} \nUsable Quota is = {} \nTotal used is = {}".format(q['quota'],q['usable_quota'],q['usage']))
                    if q['name'] == 'healthmonitors':
                        print("\nQuota available for Health_Monitors :\nTotal quota is ={} \nUsable Quota is = {} \nTotal used is = {}".format(q['quota'],q['usable_quota'],q['usage']))
                    if q['name'] == 'listeners':
                        print("\nQuota available for Listeners :\nTotal quota is ={} \nUsable Quota is = {} \nTotal used is = {}".format(q['quota'],q['usable_quota'],q['usage']))
                    if q['name'] == 'loadbalancers':
                        print("\nQuota available for Loadbalancers :\nTotal quota is ={} \nUsable Quota is = {} \nTotal used is = {}".format(q['quota'],q['usable_quota'],q['usage']))
                    if q['name'] == 'pools':
                        print("\nQuota available for Pools :\nTotal quota is ={} \nUsable Quota is = {} \nTotal used is = {}".format(q['quota'],q['usable_quota'],q['usage']))
						



def main():
    get_resources()
    


if __name__ == '__main__':
    main()
