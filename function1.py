#function1.py
def setvalue(newvalue):
    x = newvalue
    print("함수내부:", x)

result = setvalue(5)
print(result)

def swap(x,y):
    return y,x

result = swap(5,6)
print(result)
print( result[0], result[1])

def union(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print( union("HAM", "SPAM"))


def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

print( userURIBuilder("naver.com", "80", id="kim", password="1234", name="mike", age="30"))