import discord
from discord.ext import commands
import json
import asyncio

class Activity(commands.Cog):
    def __init__(self,client):
        self.client = client
        
        self.client.loop.create_task(self.save())
        
        #with open(r'C:\Users\Robert\Desktop\pybot\cogs\json\users.json','r') as f:
        with open('cogs/json/users.json','r') as f:
            self.users = json.load(f)
        
    
    async def save(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            #with open(r'C:\Users\Robert\Desktop\pybot\cogs\json\users.json', 'w') as f:
            with open('cogs/json/users.json', 'w') as f:
                json.dump(self.users, f, indent=3) 
                
            await asyncio.sleep(5)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("[Bot Shiaanah] Active Ready")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        author_id = str(message.author)
        
        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]["CountM"] = 1
            
        self.users[author_id]["CountM"] +=1
        
async def setup(client):
    await client.add_cog(Activity(client))