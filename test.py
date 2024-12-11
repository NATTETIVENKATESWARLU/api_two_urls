import requests
import json

BASE_URL="http://127.0.0.1:8000/"
ENDPOINT="Json1/"





# def callingg():
#     req=requests.get(BASE_URL + ENDPOINT)
#     if req.status_code==requests.codes.ok:
#         print(req.json())
#     else:
#         print(req.status_code)
#         print(req.json())

    


# id=input("enter your number !")
# callingg()

# def create_user():
#     dct={
#         "eno":6,
#         "ename":"venakteswarlu",
#         "esal":2000,
#         "eaddress":"eaddress"
#     }

#     req=requests.post(BASE_URL + ENDPOINT,data=json.dumps(dct))
#     print(req.status_code)
#     print(req.json())

#create_user()


# def update_resours(id):
#     dict={
#         "esal":60000,
#         "eaddress":"nellore",
#     }
#     reqs=requests.put(BASE_URL + ENDPOINT + str(id),data=json.dumps(dict))
#     print(reqs.status_code)
#     print(reqs.json())

# update_resours(4)

def delete_resours(id):
    
    reqs=requests.delete(BASE_URL + ENDPOINT + str(id))
    print(reqs.status_code)
    print(reqs.json())

delete_resours(19)