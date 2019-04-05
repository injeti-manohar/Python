import requests
import json
from requests.auth import HTTPBasicAuth
import csv


def get_v2details():
    a = 'orgID1'
    b = 'appID1'
    c = 'ConKey1'
    d = 'ConSecret1'
    org_lst = []
    some_dict = {}
    con_blst = []  # variable to append the dictionary app level
    n = int(input("Enter number of orgs from Landscape 1: "))
    for i in range(0, n):
        ele = str(input())
        org_lst.append(ele)
    cmp_orglst = list(org_lst)
#    print(cmp_orglst)
    for j in cmp_orglst:
        url = "https://canarydevmgmtsrv.dmzmo.sap.corp/v1/o/" + str(j) + "/apps/"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, auth=HTTPBasicAuth('suraj.pai.airody@sap.com', 'Manager1234'), headers=headers, verify=False)
        app_data = json.loads(response.text)
#        print(app_data)
        for k in app_data:
            url1 = "https://canarydevmgmtsrv.dmzmo.sap.corp/v1/o/" + str(j) + "/apps/" + str(k)
            headers = {'Content-Type': 'application/json'}
            response1 = requests.get(url1, auth=HTTPBasicAuth('suraj.pai.airody@sap.com', 'Manager1234'), headers=headers, verify=False)
            consumer_data = json.loads(response1.text)
#            print(consumer_data)
            some_dict[a] = str(j)
            some_dict[b] = consumer_data['appId']
            some_dict[c] = consumer_data['credentials'][0]['consumerKey']
            some_dict[d] = consumer_data['credentials'][0]['consumerSecret']
            print(some_dict)  # Print dictionary of each app ID
            con_blst.append(some_dict.copy())
            print(con_blst)

            csv_columns = ['orgID1', 'appID1', 'ConKey1', 'ConSecret1']
            csv_file = "Names1.csv"
            try:
                with open(csv_file, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in con_blst:
                        writer.writerow(data)
            except IOError:
                print("I/O error")


def get_cc3details():
    a = 'orgID2'
    b = 'appID2'
    c = 'ConKey2'
    d = 'ConSecret2'
    org_lst = []
    some_dict = {}
    con_blst = []  # variable to append the dictionary app level
    n = int(input("Enter number of orgs from Landscape 2: "))
    for i in range(0, n):
        ele = str(input())
        org_lst.append(ele)
    cmp_orglst = list(org_lst)
    #    print(cmp_orglst)
    for j in cmp_orglst:
        url = "https://cluster3eude1devmanagementserver.apim.hana.ondemand.com/v1/o/" + str(j) + "/apps/"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, auth=HTTPBasicAuth('admin@sap.com', 'Manager123'), headers=headers, verify=False)
        app_data = json.loads(response.text)
        #        print(app_data)
        for k in app_data:
            url1 = "https://cluster3eude1devmanagementserver.apim.hana.ondemand.com/v1/o/" + str(j) + "/apps/" + str(k)
            headers = {'Content-Type': 'application/json'}
            response1 = requests.get(url1, auth=HTTPBasicAuth('admin@sap.com', 'Manager123'), headers=headers, verify=False)
            consumer_data = json.loads(response1.text)
            #            print(consumer_data)
            some_dict[a] = str(j)
            some_dict[b] = consumer_data['appId']
            some_dict[c] = consumer_data['credentials'][0]['consumerKey']
            some_dict[d] = consumer_data['credentials'][0]['consumerSecret']
            print(some_dict)  # Print dictionary of each app ID
            con_blst.append(some_dict.copy())
            print(con_blst)

            csv_columns = ['orgID2', 'appID2', 'ConKey2', 'ConSecret2']
            csv_file = "Names2.csv"
            try:
                with open(csv_file, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in con_blst:
                        writer.writerow(data)
            except IOError:
                print("I/O error")


def main():
    get_v2details()
    get_cc3details()


if __name__ == '__main__':
    main()
