import grequests
import schedule
import time
def job():
    urls=[]
    for i in range (200):
    
        urls.append('https://graph.facebook.com/v5.0/107868444080665/photos')
#urls = ['https://graph.facebook.com/v5.0/107868444080665/photos','https://graph.facebook.com/v5.0/107868444080665/photos']

    params = { 'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS32w9JVSRWMxhtfpcOrKtegjyxfiKYNCxJuddhwsJbDyKIuTyF',
         'message': ' love from Harsh Singh / techSonic',
         'published': 'true',
         'access_token': 'EAAZAr9jtizGcBANIbPE1wC61coxvmzOCHp1TZA8XZCO65KKXPnpexfZCVeA8PCViBo8e1TZBvaYP5TeLszkcp2ZCRqhVCzsQlle7ZCmRfZAEaYrCtACB5bMZCGHEgQcZCEYl1RlcC1M56UCDZCZBNjWEonzDcdb1jbBYU0BLGfcdyHcjjcWRnxVlke0Q'}
    rs = (grequests.post(u, data=params) for u in urls)
    grequests.map(rs)
schedule.every(4).hours.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)