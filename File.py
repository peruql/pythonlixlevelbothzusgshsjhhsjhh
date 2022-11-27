import os

os.system("python3 webserver.py & >/dev/null")

import requests

import time

playload = {

    'content': 'level'

    # < < SPAM MSG

}

headerst = {

    'authorization': 'MTAwMzY0NDc4NjUxMjc3NzIxNg.GvbsnP.sqJZkXYecNGJEiE7i2a5wYd_SF1-QoYvg2tzQY'  # < < Token 1

}

headerst1 = {

    'authorization': 'ODU5MjA5MjE5OTE5NzA4MTcx.GPnuuj.OLRJ9MN2R8pIHw8UpjK0evCxK_5VAcPr61-fTc'  # < < Token 2

}

headerst2 = {

    'authorization': ''  # < < Token 3

}

channel = '1042551184344502332'  # < < Room Id

url = f'https://discord.com/api/v8/channels/{channel}/messages'

while True:

    requests.post(

        url,

        data=playload,

        headers=headerst,

    )

    requests.post(

        url,

        data=playload,

        headers=headerst1,

    )

    requests.post(

        url,

        data=playload,

        headers=headerst2,

    )

    time.sleep(1)  # < < How many msg sand in 1 second

