import redis
from switch import Switch
rc = redis.Redis(host='182.254.134.84', port=36379)

ps = rc.pubsub()
ps.subscribe(['000-000-001', 'bar'])
a = Switch('switchv2.0','host')
for item in ps.listen():
    if item['type'] == 'message':
        data = str(item['data'])
        if data ==r"b'switch on'":
            print('success')
            a.execute('on')
        elif data == r"b'switch off'":
            a.execute("off")
        else:
           print(item['data'])

