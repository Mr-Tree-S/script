import asyncio
import json

import websockets

url = "/ws/ops/tasks/log/"

async def main_logic(t):
	print("#### start ####")
	async with websockets.connect(t) as client:
		await client.send(json.dumps({"task": "/opt/jumpserver/logs/gunicorn"}))
		# await client.send(json.dumps({"task": "/opt/jumpserver/logs/jumpserver"}))
		while True:
			ret = json.loads(await client.recv())
			# print(ret["message"])
			if "user_id" in ret["message"]:
				print("#### TOP ####")
				print(ret["message"],end="")
				print("\n#### END ####")


if __name__ == "__main__":
	host = input()
	# print(host)
	# host = "121.199.17.253	47.111.161.207	116.196.79.227	"
	# target = "ws://" + host + url
	target = host.replace("https://", "wss://").replace("http://", "ws://") + url
	print("target: %s" %target)
	asyncio.get_event_loop().run_until_complete(main_logic(target))
