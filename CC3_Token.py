import os
import requests
import json

#Set up to read using openstackrc

os_auth_url=https://identity-3.eu-de-1.cloud.sap:443/v3
os_identity_api_version=3:
os_project_name="api-management-perf-EU":
os_project_domain_name="monsoon3"
os_username=I332512
os_user_domain_name="monsoon3"
echo "Please enter your OpenStack Password: "
read -sr OS_PASSWORD_INPUT
os_password=$OS_PASSWORD_INPUT
os_region_name=eu-de-1

req_payload = { "auth": { "identity": { "methods": ["password"],"password": {"user": {"domain": {"name": os_user_domain_name},"name": os_username, "password": os_password} } }, "scope": { "project": { "domain": { "name": os_project_domain_name }, "name":  os_project_name } } }}

token_req_payload = json.dumps(req_payload)

os_auth = os_auth_url+'/auth/tokens?nocatalog'

token_res = requests.post(os_auth, data = token_req_payload)

os_token = token_res.headers.get('X-Subject-Token')

print(os_token)
