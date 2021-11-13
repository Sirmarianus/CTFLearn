import requests

data = {'username' : 'admin', 'password' : '71urlkufpsdnlkadsf'}
r = requests.post('http://165.227.106.113/post.php', data)
print(r.text[4:-5])
