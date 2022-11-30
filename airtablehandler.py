import requests
def testit(id,gid):
    headers = {
        'Authorization': 'Bearer key6OhVcVppxONYOe',
        # Already added when you pass json= but not when you pass data=

    }
    Response = requests.get("https://api.airtable.com/v0/appHXjkKNtDVs9aVm/tblnRCTgqOA0n6qEB?fields%5B%5D=id&fields%5B%5D=gid",headers=headers).json()
    for i in Response['records'] :
        # print(i)
        if id == i['fields']['id'] and i['fields']['gid'] == gid:
            print(i['fields']['id'])
            return(0)

    return(1)


def updatedata(name,bday,id,gid):

    flag = testit(id,gid)
    if(flag==0):
        return 501
    headers = {
        'Authorization': 'Bearer key6OhVcVppxONYOe',
        # Already added when you pass json= but not when you pass data=
        'Content-Type': 'application/json',
    }

    json_data = {
        'records': [
            {
                'fields': {
                    'Name': f'{name}',
                    'Birthday': f'{bday}',
                    'id': id,
                    'gid': gid,
                },
            },
        ],
    }

    response = requests.post('https://api.airtable.com/v0/appHXjkKNtDVs9aVm/Data', headers=headers, json=json_data)
    print(response.status_code)
    return(response.status_code)

# updatedata("name","bday","id")