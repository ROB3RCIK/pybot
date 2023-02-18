import discord
from discord.ext import commands

roblox_words = ['ROBLOX', 'HUGE', 'PSX', 'PSC', 'PET', 'GEM']

class Moderation(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("[Bot Shiaanah] Moderation Ready")
 
    @commands.Cog.listener()
    async def on_message(self, message):
        for word in roblox_words:
            if word in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention} Strefa Roblox znajduje sie niżej!", delete_after = 30)
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, reason="Brak"):
        await ctx.guild.ban(reason=reason)
        embed=discord.Embed(title="Zbanowano", color=0xff0000)
        embed.add_field(name="Ban: ", value=f"{member.mention} został zbanowany przez {ctx.author.memention}", inline=False)
        embed.add_field(name="Powód:", value=reason, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, reason="Brak"):
        await ctx.guild.kick(reason=reason)
        embed=discord.Embed(title="Wyrzucono", color=0xff0000)
        embed.add_field(name="Kick: ", value=f"{member.mention} został wyrzucony przez {ctx.author.memention}", inline=False)
        embed.add_field(name="Powód:", value=reason, inline=False)
        await ctx.send(embed=embed)
    
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, ilosc = 5):
        await ctx.channel.purge(limit=ilosc+1)
        #await ctx.channel.send(f"Usunięto {ilosc} wiadomości", delete_after=5)
        embed=discord.Embed(title="Sprzątanie", color=0x0000ff)
        embed.add_field(name=f"Usunięto {ilosc} wiadomości", value="", inline=False)
        await ctx.send(embed=embed, delete_after=5)
        
        
        
    
async def setup(client):
    await client.add_cog(Moderation(client))