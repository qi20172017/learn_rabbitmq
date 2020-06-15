import asyncio
# import
async def ws_live_jd(room_id):
    uri = 'wss://xk.newrank.cn/xdnphb/nr/cloud/ks/websocket'
    async with websockets.connect(uri, ssl=True) as websocket:
        content = {"type": "webcast", "data": {"room_id": room_id}}

        await websocket.send(json.dumps(content))
        while True:
            res = await websocket.recv()
            message = json.loads(res)
            print(message)

import requests

if __name__ == '__main__':
    # room_id = "iishYjkug-s"
    room_id = '9eF6XnbLa3M'
    asyncio.get_event_loop().run_until_complete(ws_live_jd(room_id))