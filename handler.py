from time import time
from telegram_phone_number_checker import main
from asyncio import run
API_ID="8888659"
API_HASH="75fb85de4a0b0a4e00aeb72d8458de11"
PHONE_NUMBER="+989100261726"
f = open( file="./csv.txt",mode="r")
async def handler():
        client = await  main.login(api_id=API_ID,api_hash=API_HASH,phone_number=PHONE_NUMBER)
        start =  time()
        res = await main.validate_users(client,f.read())
        print(time()-start)
        ans =""
        print(type(res))
        print(res.values())
run(handler())
