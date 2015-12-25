#test.py
import orm,asyncio
from models import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop=loop, host='127.0.0.1',port=3306,user='root', password='root', db = 'awesome')

    u = User(name='test', email = 'test@example.com', passwd='1234567890', image = 'about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
