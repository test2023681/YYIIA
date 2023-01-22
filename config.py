import  os

TOKEN = os.environ.get("TOKEN", '5856353439:AAFdSE8ewLkLtmVpcuMDcIquEftCUNhP98w')
APP_ID = int(os.environ.get("API_ID", '22140808'))
API_HASH = os.environ.get("API_HASH", '72e39b383c4655d957f67d4ab94cb3aa')
CHAT_ID = os.environ.get("CHAT_ID")


youtube_next_fetch = 0  # time in minute


EDIT_TIME = 5
