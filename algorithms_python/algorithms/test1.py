import requests



r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
data = r.json()['data']
data = data.split(', ')

count = 0
for x in data:
    if(x[:3] == 'age'):
        if(int(x[4:])>50):
            count += 1

print(count)


