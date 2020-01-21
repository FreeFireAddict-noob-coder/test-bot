import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
import time
import asyncio
import logging
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL




client = commands.Bot(command_prefix='!',help_command=None)


@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed=discord.Embed(title='Missing arguments!',description='Run !help <command> to check the command syntax.',colour=discord.Colour.red())
		embed.set_footer(text='Made by Apple™#5889')
		embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/665873158288703501/666325649576689673/images-1.png')
		await ctx.send(embed=embed)

colours = ['discord.Colour.red()','discord.Colour.green()','discord.Colour.blue()','discord.Colour.orange()']




@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you run !help"))
	print("Bot is ready.")





@client.command()
async def ping(ctx):
	embed=discord.Embed(title='My latency', description=f'My latency is ``{round(client.latency * 1000)} ms``', colour=discord.Colour.blue())
	embed.set_footer(text='Made by Apple™#5889')
	await ctx.send(embed=embed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = ['It is certain',
	            'I dont care',
	            'Ask again',
	            'I am busy, ask later',
	            'No',
				'My sources say no',
				'My sources say yes',
				'I have no idea about this']

	embed=discord.Embed(title='8ball',colour=discord.Colour.blue())
	embed.set_footer(text='Made by Apple™#5889')
	embed.add_field(name='Question',value=f'{question}')
	embed.add_field(name='Answer',value=f'{random.choice(responses)}')
	await ctx.send(embed=embed)

@_8ball.error
async def _8ballerror(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed=discord.Embed(title=f'Invalid syntax!',description=f'The syntax is !8ball <question>',colour=discord.Colour.red())
		embed.add_field(name='Here is an example of how the command can be used',value='!8ball will it rain today?')
		await ctx.send(embed=embed)
@client.command()
async def invite(ctx):
	embed=discord.Embed(title='Invite me here',description='I am delighted you ran this command!',url='https://discordapp.com/api/oauth2/authorize?client_id=603893686140403712&permissions=8&scope=bot',colour=discord.Colour.green())
	embed.set_footer(text='Made by Apple™#5889')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/662236671198101514/666316330928177153/JPEG_20200109_193530.jpg')
	await ctx.send(embed=embed)

@client.command()
async def support(ctx):
	embed=discord.Embed(title='Join here for support', description='We are a fun community where we discuss about coding, gaming and what not. Join us to get live status updates of the bot and get sneak peeks of further updates!', url='https://discord.gg/NZ7seCb',colour=discord.Colour.green())
	embed.set_footer(text='Thanks for inviting me! Made by Apple™#5889')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/665873158288703501/666325649576689673/images-1.png')

	await ctx.send(embed=embed)

@client.command(aliases=[('purge')])
async def clear(ctx, amount :int):
	await ctx.channel.purge(limit=amount+1)
	embed=discord.Embed(title=f'Purged this channel{member.mention} !',description=f'Purged **{amount}** messages.',colour=discord.Colour.red())
	embed.set_footer(text='Invite me by running !invite. Made by Apple™#5889')
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/665873158288703501/666325649576689673/images-1.png')
	await ctx.send(embed=embed)
@clear.error
async def purge_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		embed=discord.Embed(title='Command: Purge',description='What it does: Clears the number of messages the user has asked to',colour=discord.Colour.red())
		embed.add_field(name='Command usage',value='!purge <number of messages>')
		await ctx.send(embed=embed)
@client.event
async def on_command_error(ctx,error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed=discord.Embed(title='Command=!ban',description='Bans a user from the server permanently, so they cannot join back again.',colour=discord.Colour.red())
		embed.add_field(name='Command syntax',value='!ban @user <optional reason>')
		embed.set_footer(text='Invite me by running !invite')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	embed=discord.Embed(title='Success!',description=f'Kicked **{member}** for **{reason}**.',colour=discord.Colour.red())
	embed.set_footer(text='Be sure to follow the rules, else this is what you get!')
	await ctx.send(embed=embed)
@kick.error
async def kick_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		embed=discord.Embed(title='Command: !kick',description='**Description:** Kicks a user so that they can join back with a invite link. \n **Usage:** !kick [user] [reason]',colour=discord.Colour.red())
		embed.add_field(name='Example',value='!kick @Apple get out!')
		embed.set_footer(text='Invite me by running !invite')
		await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	embed=discord.Embed(title='Success!',description=f'Banned **{member}** for **{reason}**.',colour=discord.Colour.red())
	embed.set_footer(text='Be sure to follow the rules, else this is what you get!')
	await ctx.send(embed=embed)
@ban.error
async def ban_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		embed=discord.Embed(title='Command: !ban',description='**Description:** Bans a user so that they cannnot join back with a invite link. \n **Usage:** !ban [user] [reason]',colour=discord.Colour.red())
		embed.add_field(name='Example',value='!ban @Apple get out!')
		embed.set_footer(text='Invite me by running !invite')
		await ctx.send(embed=embed)




@client.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message):
	await ctx.channel.purge(limit=1)
	await ctx.send(f'{message}')

@client.command()
async def speak(ctx, *, message):
	await ctx.channel.purge(limit=1)
	await ctx.send(f'**{ctx.author}** wants to say: {message}')
@speak.error
async def speak_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send(f'Please give me a message to send **{ctx.author}**')



@client.command()
@commands.has_permissions(administrator=True)
async def sayembed(ctx, *, message):
	await ctx.channel.purge(limit=1)
	embed=discord.Embed(description=f'{message}',colour=discord.Colour.green())

	await ctx.send(embed=embed)


@client.command()
async def help(ctx):
	 embed = discord.Embed(title="Help on the usage of the bot", description="Some useful commands",colour=discord.Colour.green())
	 embed.add_field(name="• !ping", value="Gives the latency of the bot.",inline=False)
	 embed.add_field(name="• !8ball", value="Ask a question and get a random answer",inline=False)
	 embed.add_field(name="• !invite",value="Invite this amazing bot!",inline=False)
	 embed.add_field(name="• !support",value="Join our support server from here.",inline=False)
	 embed.add_field(name="• !purge",value="Deletes the given number of messages. Syntax is !purge <no of messages>. Alias is !clear.",inline=False)
	 embed.add_field(name="• !kick",value="Kicks someone from the guild. The syntax is !kick <@user> <optional reason>",inline=False)
	 embed.add_field(name="• !ban",value="Bans someone from the server. The syntax is !ban <@user> <optional reason>",inline=False)
	 embed.add_field(name="• !say",value="Say something using the bot. Useful to say things you can't say directly, usable ONLY by administrators",inline=False)
	 embed.add_field(name="• !sayembed",value="Same as !say, just sends the message in an embed.",inline=False)
	 embed.add_field(name="• !softban",value="Bans and unbans a user immediately to delete their messages.",inline=False)
	 embed.add_field(name="• !speak",value="Say something using the bot. Can be used by anyone in the server.",inline=False)
	 embed.set_footer(text="Made by Apple™#5889")
	 await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def softban(ctx, member: discord.Member, *, reason=None):
	await ctx.channel.purge(limit=1)
	await member.ban(reason=reason)
	await member.unban(reason=reason)
	embed=discord.Embed(title="Success!",description=f'Succesfully softbanned {member}, i.e. banned and unbanned them immediately to delete their messages.',colour=discord.Colour.red())
	embed.set_footer('Made by Apple™#5889')
	await ctx.send(embed=embed)
@softban.error
async def softban_error(ctx,error):
	if isinstance(error,commands.MissingRequiredArgument):
		embed=discord.Embed(title='Command: !softban',description='**Description:** Bans a user and then unbans immediately to delete their messages. \n **Usage:** !softban [user] [reason]',colour=discord.Colour.red())
		embed.add_field(name='Example',value='!softban @Apple no spamming')
		embed.set_footer(text='Invite me by running !invite')
		await ctx.send(embed=embed)

@client.command(aliases=[('avatar')])
async def av(ctx, member: discord.Member):
	embed=discord.Embed(title=f'Avatar of {member}',colour=discord.Colour.blue())
	embed.set_image(url=author.avatar_url)
	await ctx.send(embed=embed)

@client.command
async def info(ctx):
	embed=discord.Embed(title=f'Information regiarding me',description='**Coded by:** Apple#5889 \n **Runs on:** Intel core i3 2370M',colour=discord.Colour.green())
	embed.set_footer(text='Invite by running !invite')
	await ctx.send(embed=embed)

client.run('NjAzODkzNjg2MTQwNDAzNzEy.Xhr1yQ.caLVKKF-kHBaCq-66h0uwgx9M2g')
