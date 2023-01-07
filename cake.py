import discord
import datetime

#import token.json

client = discord.Client()

#create a dictionary to store the birthdays

@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')
    #set the bot to check for birthdays every minut
    client.loop.create_task(check_birthdays())

async def check_birthdays():
    await client.wait_until_ready()
    while not client.is_closed():
        #get the current time
        now = datetime.datetime.now()

        #If it is 8am check for birthdays
        if now.hour == 8:
            for user_id, birthday in birthday_dict.items():
                #split the birthday into month and day
                month, day = map(int, birthday.split('/'))
                #check if today is the users birthday
                if now.month == month and now.day == day:
                    user = client.get_user(user_id)
                    #send the birthday message
                    await user.send(f"Happy Birthday, {user.name}!")
    #Sleep for a minute before checking again
    await asyncio.sleep(60)


@client.event
async def on_message(message):
    if message.content.startswith("/addbirthday"):
        #split the message into parts
        parts = message.content.split()
        #check if the command was used correctly
        if len(parts) == 3:
            #get user's mention and birthday
            user = message.mentions[0]
            birthday = parts[2]
            #add the birthday to the dictionary
            birthday_dict[user.id]  = birthday
            await message.channel.send(f'Successfully added {user.name}\'s birthday: {birthday}')
        else:
            await message.channel.send('Invalid usage. Use the format `!addbirthday @user MM/DD`')

client.run('YOUR_BOT_TOKEN_HERE')
