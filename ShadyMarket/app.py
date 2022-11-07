from datetime import datetime
import os
import json
import random
import discord

from flask import Flask


file = open("items.json")
items = json.load(file)
mundaneItems = []
commonItems = []
uncommonItems = []
rareItems = []
veryRareItems = []
otherItems = []
name="name"

for item in items:
    if "rarity" in item:
        if item["rarity"] == "none":
            mundaneItems.append(item)
        elif item["rarity"] == "common":
            commonItems.append(item)
        elif item["rarity"] == "uncommon":
            uncommonItems.append(item)
        elif item["rarity"] == "rare":
            rareItems.append(item)
        elif item["rarity"] == "very rare":
            veryRareItems.append(item)
        else:
            otherItems.append(item)
    else:
        otherItems.append(item)


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$peruse"):
        currentTime = datetime.utcnow()
        random.seed(currentTime.year*10000 + currentTime.month * 100 + currentTime.day)
        finalMessage = "Here's what's up for grabs today:\n"
        highValueMessage = ""

        mundaneItem1 = mundaneItems[random.randint(0, len(commonItems)-1)]
        mundaneItem2 = mundaneItems[random.randint(0, len(commonItems)-1)]
        mundaneItem3 = mundaneItems[random.randint(0, len(commonItems)-1)]

        common1 = commonItems[random.randint(0, len(commonItems)-1)]
        common2 = commonItems[random.randint(0, len(commonItems)-1)]

        uncommon1 = uncommonItems[random.randint(0, len(uncommonItems)-1)]

        rare1 = rareItems[random.randint(0, len(rareItems)-1)]

        veryRare1 = veryRareItems[random.randint(0, len(veryRareItems)-1)]

        other1 = otherItems[random.randint(0, len(otherItems)-1)]

        finalMessage += f"• {mundaneItem1[name]}\n" \
                        f"• {mundaneItem2[name]}\n" \
                        f"• {mundaneItem3[name]}\n" \
                        f"• {common1[name]}\n" \
                        f"• {common2[name]}\n" \
                        f"• {uncommon1[name]}\n" \

        # Reset the seed so we can roll pseudo-randomly
        random.seed()
        if(random.randint(1, 25) == 1):
            highValueMessage += f"• {rare1[name]}\n"
        if (random.randint(1, 50) == 1):
            highValueMessage += f"• {veryRare1[name]}\n"
        if (random.randint(1, 33) == 1):
            highValueMessage += f"• {other1[name]}\n"

        if len(highValueMessage) > 0:
            finalMessage += f"What you're about to see next is special.  Won't be around on your next visit, " \
                            f"I guarantee.\n{highValueMessage}"

        await message.channel.send(finalMessage)

client.run(DISCORD_TOKEN)