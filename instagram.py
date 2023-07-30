import os
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
#json file is giving the error so we deleted the json file here up

#429 error we removed by commenting  559 to 585 lines in api.py in instabot

from instabot import Bot

bot=Bot()
bot.login(username="vivekbnagare31",password="Madhu@31")
# bot.follow("larrywheels")

#to upload a image


# bot.upload_photo("C:/Users/vivek/OneDrive/Pictures/Screenshots/Screenshot 2023-04-19 234925.png",caption="i love programming")#here you can use path of photo or if the photo is directly present in the folder you can directly use it.
#also change the slash

#to unfollow a person

# bot.unfollow("codewithharry")

#if we want to send mssg to multiple persons

# bot.send_message("i love programming",["vicky30888","vighnesh_1503"])

# followers=bot.get_user_followers("vivekbnagare31")
# for follower in followers:
#     print(bot.get_user_info(follower))

follower=bot.get_user_info("vighnesh_1503")
print(follower)