#works fine
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = '!', intents =discord.Intents.all())

IDSERVER = 813828150098133022


async def onRoleAddAction(myClient, myPayload):
    RRMESSAGEID = 819582773547106304
    message_id = myPayload.message_id
    if message_id == RRMESSAGEID:
        guild = myClient.get_guild(IDSERVER)
        ROLENAME = myPayload.emoji.name
        roleid = discord.utils.get(guild.roles, name = ROLENAME)
        role = guild.get_role(roleid.id)

        if role is not None:
            member = guild.get_member(myPayload.user_id)
            member = myPayload.member
            if member is not None:
                await member.add_roles(role)
                print('The role is added')
            else:
                print('Member not found')
        else:
                print('Role not found')


@client.event
async def on_raw_reaction_add(payload):
    return await onRoleAddAction(client, payload)
    
            
async def onRoleRemoveAction(myClient, myPayload):
    RRMESSAGEID = 819582773547106304
    message_id = myPayload.message_id
    if message_id == RRMESSAGEID:
        guild = myClient.get_guild(IDSERVER)
        ROLENAME = myPayload.emoji.name
        roleid = discord.utils.get(guild.roles, name = ROLENAME)
        role = guild.get_role(roleid.id)

        if role is not None:
            member = guild.get_member(myPayload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print('The role is removed')
            else:
                print('Member not found')
        else:
                print('Role not found')

@client.event
async def on_raw_reaction_remove(payload):
   return await onRoleRemoveAction(client, payload)

client.run('TOKEN')