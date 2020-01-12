import requests
import json
def fun(key,url):
    st='Key '+key
    
    h = {'Authorization':st,'Content-Type':'application/json'}
    #headers=json.dumps(h)
    d =  {'inputs':[{'data':{'image':{'url':url}}}]}
    data=json.dumps(d)
    response = requests.post('https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs', headers=h,data=data)
    r=json.loads(response.text)
    arr=r['outputs'][0]['data']['concepts']
    li=[]
    for i in arr:
        li.append(i['name'])
    print(li)
fun('a7f5daee06044c8eb6d8100a01f10d39','https://samples.clarifai.com/food.jpg')