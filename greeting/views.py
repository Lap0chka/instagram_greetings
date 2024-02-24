from django.shortcuts import render
from instabot import Bot


def index(request):
    bot = Bot()
    username = 'tattoo_partak_com'
    password = 'zGstiw3259'
    message = 'Ny tu i pidor'
    # Логин в систему
    bot.login(username=username, password=password)
    user_followers = bot.get_user_followers(username)
    while True:
        update_user_followers = bot.get_user_followers(username)
        if len(user_followers) < len(update_user_followers):
            new_folowers = set(update_user_followers) - set(user_followers)
            user_followers = update_user_followers
            for follower in new_folowers:
                bot.send_message(message, follower)

    return render(requests, 'greeting/base.html')
