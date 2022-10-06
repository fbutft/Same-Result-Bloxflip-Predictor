#GET LEAKED BY VANQUISH

from discord.ext import commands
import discord
import random
import uuid
from pymongo import MongoClient



bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())


@bot.command()
async def mines(ctx, mine_amount, round_id):
    mine_amount = int(mine_amount)
    round_id = str(round_id)
    round_length = len(round_id)
    if round_length == 36: #64 if you want server hash
        mongo_url = 'urlhere'
        cluster = MongoClient(mongo_url)
        db = cluster['namehere']
        collection = db['namehere']

        check_for_roundid = collection.find({"round_id": round_id})

        valid = False
        for check_for_roundid in check_for_roundid:
            valid = True
            result = check_for_roundid['result']
            em = discord.Embed(color=0x2525ff)
            em.add_field(name="Mines Predictor", value=f"Round ID\n```{round_id}```\nPrediction\n`{result}`")
            await ctx.send(embed=em)
        
        if valid == False:
            if mine_amount == 1:
                empty = []
                for x in range(5):
                    grid = [
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴"
                    ]
                    create_grid = random.randrange(0, len(grid))
                    grid[create_grid] = random.choice(
                        ["🟢"])
                    empty.append("".join(grid))

            elif mine_amount == 2:
                empty = []
                for x in range(5):
                    grid = [
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴"
                    ]
                    create_grid = random.randrange(0, len(grid))
                    grid[create_grid] = random.choice([
                        "🟢", "🔴"
                    ])
                    empty.append("".join(grid))

            elif mine_amount == 3:
                empty = []
                for x in range(5):
                    grid = [
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴"
                    ]
                    create_grid = random.randrange(0, len(grid))
                    grid[create_grid] = random.choice([
                        "🟢","🔴", "🟢"
                    ])
                    empty.append("".join(grid))

            elif mine_amount == 4:
                empty = []
                for x in range(5):
                    grid = [
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴"
                    ]
                    create_grid = random.randrange(0, len(grid))
                    grid[create_grid] = random.choice([
                        "🟢", "🔴",
                        "🔴","🟢"
                    ])
                    empty.append("".join(grid))

            elif mine_amount == 5:
                for x in range(5):
                    grid = [
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴",
                        "🔴"
                    ]
                    create_grid = random.randrange(0, len(grid))
                    grid[create_grid] = random.choice([
                        "🟢", "🔴",
                        "🔴"
                    ])
                    empty.append("".join(grid))

            result = "\n".join(empty)
            post = {"round_id": round_id, "result": result}
            collection.insert_one(post)
            em = discord.Embed(color=0x2525ff)
            em.add_field(name="Mines Predictor", value=f"Round ID\n```{round_id}```\nPrediction\n`{result}`")
            await ctx.send(embed=em)
    else:
        await ctx.send("Invalid Round ID")

bot.run('token')

#GET LEAKED BY VANQUISH
