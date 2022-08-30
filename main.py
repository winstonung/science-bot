import json, discord, os, random, asyncio
from discord.ext import commands, tasks
from itertools import cycle
#from keep_alive import keep_alive

'''
physicsc = 13191013
chemc = 5938914
bioc = 13392949
'''


statuses = cycle(["s.help", "c.help"])
links = cycle(["https://www.youtube.com/watch?v=X1Q3J3g6X2w", "https://www.youtube.com/watch?v=7Up7DIPkTzo&list=PLCiOXwirraUAEhj4TUjMxYm4593B2dUPF"])


client = commands.Bot(command_prefix=["s.", "S."], case_insensitive=True, allowed_mentions = discord.AllowedMentions(everyone=False, users=True, roles=False), help_command=None)


@tasks.loop(seconds=30)
async def change_status():
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Streaming(name=next(statuses), url=next(links), platform="YouTube"))


@client.event
async def on_ready():
    print("Bot is ready!")


@client.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


@client.event
async def on_message(message):
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    colours = [physicsc, chemc, bioc]
    colour = random.choice(colours)
    if message.author.bot:
        return
    if message.content == "<@!862359356812951593>":
        embed = discord.Embed(title="My prefix is `s.`", colour=colour)
        embed.set_footer(text="Bot created by Pick A Username#8826")
        await message.channel.send(embed=embed)
    await client.process_commands(message)


@client.command(aliases=["topic"])
async def topics(ctx):
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    colour = [physicsc, chemc, bioc]
    embed = discord.Embed(title="Science Topics", description="**B1 - Cell Biology:** Cell structure(cells), Cell transport\n"
                                                              "**B4 - Bioenergetics:** Photosynthesis(photo), Respiration\n"
                                                              "**P3 - Particle Model of Matter** "
                          , color=random.choice(colour))
    embed.set_footer(text="You can run s.r <topic> to get a bunch of questions related to that topic or run s.eq <module> to get equations on that physics module!")
    await ctx.send(embed=embed)


@client.command(aliases=["i-v"])
async def iv(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/837726549255258132/unknown.png")


@client.command(aliases=["periodictable", "periodic-table"])
async def pt(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/863168059140866119/unknown.png")


@client.command(aliases=["electricalsymbols", "esymbol", "esymbols", "electricsymbol", "electricsymbols", "electricalsymbol"])
async def esym(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/792777621582643240/837045200693100615/unknown.png")


@client.command(aliases=["circuit", "circuits"])
async def c(ctx, *, args=None):
    if ctx.author.bot:
        return
    if args is not None:
        args = args.lower()
        parallel = args.startswith("p")
        series = args.startswith("s")
        if parallel is True:
            await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/863428681778593802/Parallel.png")
            return
        if series is True:
            await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/863429029674876948/Series.jpg")
            return
    await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/863428681778593802/Parallel.png")
    await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/863429029674876948/Series.jpg")


@client.command(aliases=["alpha", "beta", "gamma", "radiate"])
async def radiation(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/827511279114649601/863434502851657728/Radiation_.png")


@client.command(aliases=["reactionprofiles", "reaction", "reaction-profile"])
async def rp(ctx, *, args=None):
    exo = discord.Embed(title="__**Exothermic graph**__")
    exo.set_image(url="https://cdn.discordapp.com/attachments/862368134157566002/867138322354405386/Reaction-Profile-Exo.png")
    endo = discord.Embed(title="__**Endothermic graph**__")
    endo.set_image(url="https://cdn.discordapp.com/attachments/862368134157566002/867138380953681980/Reaction-Profile-Endo.png")
    if args is None:
        await ctx.send(embed=exo)
        await ctx.send(embed=endo)
        return
    args = args.lower()
    if args.startswith("ex") is True:
        await ctx.send(embed=exo)
        return
    if args.startswith("en") is True:
        await ctx.send(embed=endo)
        return
    await ctx.send(embed=exo)
    await ctx.send(embed=endo)


@client.command()
async def cell(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/862368134157566002/867302420827865098/sdxLPfkM5DJ7NSpHxP4hWFw.png")


@client.command(aliases=["transportation", "osmosis", "diffusion", "active-transport", "activetransport"])
async def transport(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/833795260672507945/870606096539189258/Transport_.png")


@client.command()
@commands.is_owner()
async def add(ctx):
    await ctx.send("Topic:")

    def check0(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author

    topic = await client.wait_for("message", check=check0)
    topic = topic.content.lower()

    if topic == "photo":
        topic = "photosynthesis"
    if topic == "cellstructure" or topic == "cells":
        topic = "cell structure"
    if topic == "transport" or topic == "transportation" or topic == "cell transportation":
        topic = "cell transport"
    if topic == "particle" or topic == "matter":
        topic = "particle model of matter"

    await ctx.send("Question:")

    def check1(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author

    question = await client.wait_for('message', check=check1)
    question = question.content
    await ctx.send("Answer:")

    def check2(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author

    answer = await client.wait_for('message', check=check2)
    answer = answer.content
    await ctx.send(f"```Topic: {topic}\nQuestion: {question}\nAnswer: {answer}```\nWould you like to add this?")

    def check3(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author

    msg_final = await client.wait_for("message", check=check3)
    if msg_final.content.lower() == "yes" or msg_final.content.lower() == "y":

        with open("main.json", "r+") as f:
            data = json.load(f)
            y = {
                "question": question,
                "answer": answer
            }
            if topic not in data:
                data[topic] = []
                data[topic].append(y)
                f.seek(0)
                json.dump(data, f, indent=4)
            else:
                data[topic].append(y)
                f.seek(0)
                json.dump(data, f, indent=4)
        channel = discord.utils.get(client.get_all_channels(), guild__name='Idk', name='science-bot')
        await channel.send(f"<@!614871652714545281>, update the main.json file.```Type : add\nTopic: {topic}\nQuestion: {question}\nAnswer: {answer}```")
        await ctx.send("Done!")
    else:
        await ctx.send("Sure thing.")


@client.command()
@commands.is_owner()
async def remove(ctx):
    await ctx.send("Topic:")

    def check0(m):
        return m.content and m.author == ctx.author and m.channel == ctx.channel

    topic = await client.wait_for("message", check=check0)
    topic = topic.content.lower()

    if topic == "photo":
        topic = "photosynthesis"
    if topic == "cellstructure" or topic == "cells":
        topic = "cell structure"
    if topic == "transport" or topic == "transportation" or topic == "cell transportation":
        topic = "cell transport"
    if topic == "particle" or topic == "matter":
        topic = "particle model of matter"

    await ctx.send("Question:")

    def check1(m):
        return m.content and m.author == ctx.author and m.channel == ctx.channel

    question = await client.wait_for("message", check=check1)
    question = question.content
    with open("main.json", "r") as f:
        data = json.load(f)
    i = 0
    try:
        while True:
            questions = data[topic][i]["question"]
            if questions == question:
                break
            else:
                i += 1
    except (IndexError, KeyError) as e:
        await ctx.send("Nothing found.")
        return
    answer = data[topic][i]["answer"]
    await ctx.send(f"```Topic: {topic}\nQuestion: {question}\nAnswer: {answer}```\nAre you sure you want to remove this?")

    def check2(m):
        return m.content and m.author == ctx.author and m.channel == ctx.channel

    yesno = await client.wait_for("message", check=check2)
    yesno = yesno.content.lower()

    if yesno == "y" or yesno == "yes":
        data[topic].pop(i)

        with open("main.json", "w") as f:
            json.dump(data, f, indent=4)
        channel = discord.utils.get(client.get_all_channels(), guild__name='Idk', name='science-bot')
        await channel.send(f"<@!614871652714545281>, update the main.json file.```Type: remove\nTopic: {topic}\nQuestion: {question}\nAnswer: {answer}```")
        await ctx.send("Done!")
    else:
        await ctx.send("Sure thing.")


@client.command(aliases=["change"])
@commands.is_owner()
async def edit(ctx):
    await ctx.send("Topic:")

    def check0(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author

    topic = await client.wait_for("message", check=check0)
    topic = topic.content.lower()

    if topic == "photo":
        topic = "photosynthesis"
    if topic == "cellstructure" or topic == "cells":
        topic = "cell structure"
    if topic == "transport" or topic == "transportation" or topic == "cell transportation":
        topic = "cell transport"
    if topic == "particle" or topic == "matter":
        topic = "particle model of matter"

    await ctx.send("Question:")

    def check1(m):
        return m.content and m.channel == ctx.channel and m.author == ctx.author

    question = await client.wait_for("message", check=check1)
    question = question.content
    i = 0
    with open("main.json") as f:
        data = json.load(f)
    try:
        while True:
            questions = data[topic][i]["question"]
            if questions == question:
                break
            else:
                i += 1
    except (KeyError, IndexError) as e:
        await ctx.send("Nothing found.")
        return
    answer = data[topic][i]["answer"]
    await ctx.send(f"```Topic: {topic}\nQuestion: {question}\nAnswer: {answer}```\nWould you like to edit the question or answer?")

    def check2(m):
        return m.content and m.author == ctx.author and m.channel == ctx.channel

    yesno = await client.wait_for("message", check=check2)
    yesno = yesno.content.lower()

    if yesno == "ans" or yesno == "answer":
        with open("main.json", "r") as f:
            data = json.load(f)

            def check3(m):
                return m.content and m.author == ctx.author and m.channel == ctx.channel

            await ctx.send("Enter new answer:")
            answer = await client.wait_for("message", check=check3)
            answer = answer.content
            data[topic][i]["answer"] = answer
            with open("main.json", "w") as fs:
                json.dump(data, fs, indent=4)
        channel = discord.utils.get(client.get_all_channels(), guild__name='Idk', name='science-bot')
        await channel.send(f"<@!614871652714545281>, update the main.json file.```Type :change (answer)\nTopic: {topic}\nQuestion: {question}\nAnswer: {answer}```")
        await ctx.send("Done!")
        return
    elif yesno == "quest" or yesno == "que" or yesno == "question":
        with open("main.json", "r+") as f:
            data = json.load(f)

            def check4(m):
                return m.content and m.author == ctx.author and m.channel == ctx.channel

            await ctx.send("Enter new question:")
            question = await client.wait_for("message", check=check4)
            question = question.content
            data[topic][i]["question"] = question
            with open("main.json", "w") as fs:
                json.dump(data, fs, indent=4)
        await ctx.send("Done!")
        channel = discord.utils.get(client.get_all_channels(), guild__name='Idk', name='science-bot')
        await channel.send(f"<@!614871652714545281>, update the main.json file.```Type: change (question)\nTopic: {topic}\nQuestion: {question}\nAnswer: {answer}```")
        return
    else:
        await ctx.send("Sure thing.")


@client.command(aliases=["r", "retrieval"])
@commands.cooldown(1, 2, commands.BucketType.user)
async def retrieve(ctx, *, args=None):
    
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    colours = [physicsc, chemc, bioc]
    colour = random.choice(colours)
    if args is None:
        embed = discord.Embed(title="Run `s.topics` to see all the available topics!", colour=colour)
        embed.set_footer(text="Bot created by Pick A Username#8826")
        await ctx.send(embed=embed)
        return
    args = args.lower()
    global message_retrieve
    message_retrieve = await ctx.send("<a:loading:873550513101213697>")

    if args == "photo":
        args = "photosynthesis"
    if args == "cellstructure" or args == "cells":
        args = "cell structure"
    if args == "transport" or args == "transportation" or args == "cell transportation":
        args = "cell transport"

    if args == "particle" or args == "matter":
        args = "particle model of matter"

    #colours
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    physics = []
    chem = []
    bio = ["photosynthesis", "respiration", "cell structure", "cell transport"]

    #returns if bot ran command
    if ctx.author.bot:
        return

    with open("main.json", "r") as f:
        data = json.load(f)

    if args == "b1" or args == "cell biology":
        biglist = ["cell structure", "cell transport"]
    elif args == "b4" or args == "bioenergetics":
        biglist = ["photosynthesis", "respiration"]
    elif args == "p3":
        biglist=["particle model of matter"]
    else:
            biglist = [args]
    async with ctx.typing():
        k = 0
        for args in biglist:
            text = f"_ _\n__**Questions about {args}**__\n\n"
            i = 0
            member = ctx.author
            channel = await member.create_dm()

            #check index
            try:
                while True:
                    try:
                        questions = data[args][i]["question"]
                        answers = data[args][i]["answer"]
                        i += 1
                    except IndexError:
                        break
            except KeyError:
                embed = discord.Embed(title="Run `s.topics` to see all the available topics!", colour=colour)
                embed.set_footer(text="Bot created by Pick A Username#8826")
                await message_retrieve.edit(embed=embed, content="This topic does not exist.")
                return
            list = []
            while True:
                list.append(i-1)
                i -= 1
                if i == 0:
                    random.shuffle(list)
                    break

            #create messages to send

            for j in list:
                questions = data[args][j]["question"]
                answers = data[args][j]["answer"]
                text = f"{text}**{questions}**\n{answers}\n\n"
                #this happens so message limit doesnt break
                if len(text) >= 1500:
                    if k != 1:
                        messagelink = await channel.send(text)
                        k = 1
                    else:
                        await channel.send(text)
                    text = "_ _\n"
            if k != 1:
                messagelink = await channel.send(text)
            else:
                await channel.send(text)

            images = f"{args}image"
            i = 0

            try:
                data[images][0]["image"]
            except KeyError:
                await channel.send("**End of questions**")
                await asyncio.sleep(1.5)
                continue

            # checks index
            while True:
                try:
                    image = data[images][i]["image"]
                    questions = data[images][i]["question"]
                    answers = data[images][i]["answer"]
                    i += 1
                except IndexError:
                    break

            list = []

            while True:
                list.append(i-1)
                i -= 1
                if i == 0:
                    random.shuffle(list)
                    break

            if args in bio:
                colour = bioc
            elif args in chem:
                colour = chemc
            elif args in physics:
                colour = physicsc
            else:
                pass

            # sends embeds
            while True:
                for i in list:
                    image = data[images][i]["image"]
                    questions = data[images][i]["question"]
                    answers = data[images][i]["answer"]
                    embed = discord.Embed(description=f"**{questions}**\n\n{answers}", colour=colour)
                    embed.set_image(url=image)
                    embed.set_footer(text="Bot created by Pick A Username#8826")
                    await channel.send(embed=embed)
                await channel.send("**End of questions**")
                await asyncio.sleep(1.5)
                break
    embed2 = discord.Embed(description=f"[Questions have been sent to your DMs! (Click to go to them quickly)]({messagelink.jump_url})")
    await message_retrieve.edit(embed=embed2, content=None)


@retrieve.error
async def retrieve_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown for {error.retry_after:.2f}s")
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await message_retrieve.edit(content="The bot, for some reason, cannot DM you <a:think_spin:873560369174564915>.")


@client.command(aliases=["flash", "flashcard"])
@commands.cooldown(1, 2, commands.BucketType.user)
async def flashcards(ctx, *, args=None):
    
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    colours = [physicsc, chemc, bioc]
    colour = random.choice(colours)
    if args is None:
        embed = discord.Embed(title="Run `s.topics` to see all the available topics!", colour=colour)
        embed.set_footer(text="Bot created by Pick A Username#8826")
        await ctx.send(embed=embed)
        return
    args = args.lower()
    global message_retrieve
    message_retrieve = await ctx.send("<a:loading:873550513101213697>")

    if args == "photo":
        args = "photosynthesis"
    if args == "cellstructure" or args == "cells":
        args = "cell structure"
    if args == "transport" or args == "transportation" or args == "cell transportation":
        args = "cell transport"

    if args == "particle" or args == "matter":
        args = "particle model of matter"

    #colours
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    physics = []
    chem = []
    bio = ["photosynthesis", "respiration", "cell structure", "cell transport"]

    #returns if bot ran command
    if ctx.author.bot:
        return

    with open("flashcards.json", "r") as f:
        data = json.load(f)

    if args == "b1" or args == "cell biology":
        biglist = ["cell structure", "cell transport"]
    elif args == "b4" or args == "bioenergetics":
        biglist = ["photosynthesis", "respiration"]
    elif args == "p3":
        biglist=["particle model of matter"]
    else:
            biglist = [args]
    async with ctx.typing():
        k = 0
        for args in biglist:
            text = f"_ _\n__**Questions about {args}**__\n\n"
            i = 0
            member = ctx.author
            channel = await member.create_dm()

            #check index
            try:
                while True:
                    try:
                        questions = data[args][i]["question"]
                        answers = data[args][i]["answer"]
                        i += 1
                    except IndexError:
                        break
            except KeyError:
                embed = discord.Embed(title="Run `s.topics` to see all the available topics!", colour=colour)
                embed.set_footer(text="Bot created by Pick A Username#8826")
                await message_retrieve.edit(embed=embed, content="This topic does not exist.")
                return
            list = []
            while True:
                list.append(i-1)
                i -= 1
                if i == 0:
                    random.shuffle(list)
                    break

            #create messages to send

            for j in list:
                questions = data[args][j]["question"]
                answers = data[args][j]["answer"]
                if answers.startswith("1)") or answers.startswith("Solid:") or answers.startswith("-"):
                    something = ""
                else:
                    something = "||"
                text = f"{text}**{questions}**\n{something}{answers}||\n\n"
                #this happens so message limit doesnt break
                if len(text) >= 1500:
                    if k != 1:
                        messagelink = await channel.send(text)
                        k = 1
                    else:
                        await channel.send(text)
                    text = "_ _\n"
            if k != 1:
                messagelink = await channel.send(text)
            else:
                await channel.send(text)

            images = f"{args}image"
            i = 0

            try:
                data[images][0]["image"]
            except KeyError:
                await channel.send("**End of questions**")
                await asyncio.sleep(1.5)
                continue

            # checks index
            while True:
                try:
                    image = data[images][i]["image"]
                    questions = data[images][i]["question"]
                    answers = data[images][i]["answer"]
                    i += 1
                except IndexError:
                    break

            list = []

            while True:
                list.append(i-1)
                i -= 1
                if i == 0:
                    random.shuffle(list)
                    break

            if args in bio:
                colour = bioc
            elif args in chem:
                colour = chemc
            elif args in physics:
                colour = physicsc
            else:
                pass

            # sends embeds
            while True:
                for i in list:
                    image = data[images][i]["image"]
                    questions = data[images][i]["question"]
                    answers = data[images][i]["answer"]
                    if answers.startswith("1)") or answers.startswith("Solid:") or answers.startswith("-"):
                        something = ""
                    else:
                        something = "||"
                    embed = discord.Embed(description=f"**{questions}**\n\n{something}{answers}||", colour=colour)
                    embed.set_image(url=image)
                    embed.set_footer(text="Bot created by Pick A Username#8826")
                    await channel.send(embed=embed)
                await channel.send("**End of questions**")
                await asyncio.sleep(1.5)
                break
    embed2 = discord.Embed(description=f"[Questions have been sent to your DMs! (Click to go to them quickly)]({messagelink.jump_url})")
    await message_retrieve.edit(embed=embed2, content=None)


@flashcards.error
async def flashcards_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown for {error.retry_after:.2f}s")
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await message_retrieve.edit(content="The bot, for some reason, cannot DM you <a:think_spin:873560369174564915>.")



# don't forget to update topic list!
@client.command(aliases=["eq"])
@commands.cooldown(1, 2, commands.BucketType.user)
async def equation(ctx, *, equation=None):
    if equation is None:
        await ctx.send("https://cdn.discordapp.com/attachments/792777621582643240/832558697884024852/unknown.png")
        return
    equation = equation.lower()
    physicsc = 13191013
    with open("equations.json") as f:
        data = json.load(f)
    if equation == "kinetic" or equation == "ek" or equation == "p1":
        equation = "kinetic energy"
    if equation == "gpe" or equation == "gravity" or equation == "gravitational":
        equation = "gravitational potential energy"
    if equation == "work":
        equation = "work done"
    if equation == "energy t":
        equation = "energy transferred"
    if equation == "particle" or equation == "particle model" or equation == "matter" or equation == "p3":
        equation = "particle model of matter"
    if equation == "shc" or equation == "specific heat":
        equation = "specific heat capacity"
    if equation == "specific latent" or equation == "slh":
        equation = "specific latent heat"
    if equation == "volume" or equation == "mass":
        equation = "density"
    if equation == "epe" or equation == "elastic" or equation == "elastic potential":
        equation = "elastic potential energy"
    if equation == "volt":
        equation = "voltage"
    if equation == "electric" or equation == "elec" or equation == "p2":
        equation = "electricity"
    if equation.startswith("hooke"):
        equation = "hooke's law"
    if equation.startswith("newton") or equation == "f=ma":
        equation = "newton's second law"

    topics = ["electricity", "energy", "particle model of matter", "forces"]
    i = 0

    if equation == "power":
        channel = await ctx.author.create_dm()
        with open("equations.json") as f:
            data = json.load(f)
        power1 = data["energy"][0]["image"]
        await channel.send(power1)
        i = [3, 4, 5]
        for item in i:
            power2 = data["electricity"][item]["image"]
            await channel.send(power2)
        await ctx.send("Equations have been sent to your DMs!")
        return

    if equation == "charge":
        with open("equations.json") as f:
            data = json.load(f)
        i = [0, 1]
        for item in i:
            charge = data["electricity"][item]["image"]
            await ctx.send(charge)
        return

    if equation == "energy transferred":
        with open("equations.json") as f:
            data = json.load(f)
        i = [6, 7]
        for item in i:
            et = data["electricity"][item]["image"]
            await ctx.send(et)
        return

    for topic in topics:
        if equation == topic:
            i = 0
            while True:
                try:
                    equations = data[equation][i]["equation"]
                    images = data[equation][i]["image"]
                    i += 1
                except IndexError:
                    break
            list = []
            while True:
                list.append(i-1)
                i -= 1
                if i == 0:
                    list.sort()
                    break
            text = ""
            for j in list:
                equations = data[equation][j]["equation"]
                images = data[equation][j]["image"]
                text = f"{text}[{equations.capitalize()}]({images})\n"
            embed = discord.Embed(title=f"Equations for {equation.capitalize()}", description=text, colour=physicsc)
            if equation == "energy":
                embed.set_footer(text="Did you want to find the equations for energy transferred? Try 's.eq energy t' instead")
            else:
                embed.set_footer(text="Bot created by Pick A Username#8826")
            await ctx.send(embed=embed)
            return

    for topic in topics:
        i = 0
        while True:
            try:
                equations = data[topic][i]["equation"]
                if equations == equation:
                    images = data[topic][i]["image"]
                    await ctx.send(images)
                    break
                else:
                    i += 1
            except IndexError:
                break


@equation.error
async def equation_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown for {error.retry_after:.2f}s")
    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
        await ctx.send("This equation doesn't exist yet.")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")


@client.command()
@commands.is_owner()
async def invite(ctx):
    embed = discord.Embed(title="Invite the bot to your server (if you're the owner)", description="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=862359356812951593&permissions=2148005952&scope=bot)")
    embed.set_footer(text="Bot created by Pick A Username#8226")
    await ctx.send(embed=embed)


@client.command(aliases=["h"])
async def help(ctx, *, args=None):
    physicsc = 13191013
    chemc = 5938914
    bioc = 13392949
    colours = [physicsc, chemc, bioc]
    colour = random.choice(colours)
    embed_all = discord.Embed(title="Commands for Science Bot", description="__**All/Other**__\n"
                                                                            "`topics`\n`retrieve`\n`ping`\n`help`\n\n"
                                                                            "__**Physics**__\n"
                                                                            "`equation`\n`esym`\n`iv`\n`circuit`\n`radiation`\n\n"
                                                                            "__**Chemistry**__\n"
                                                                            "`pt`\n`rp`\n\n"
                                                                            "__**Biology**__\n"
                                                                            "`cell`\n`transport`\n", colour=colour)
    embed_all.set_footer(text="Run s.help <command> to get more information on a command!")
    if args is None:
        await ctx.send(embed=embed_all)
        return

    args = args.lower()
    #topic
    embed_topic = discord.Embed(title="__**Topics**__", colour=colour)
    embed_topic.add_field(name="__**Usage**__", value="`s.topics`\n_ _", inline=False)
    embed_topic.add_field(name="__**Description**__", value="Gives you all the topics added to this bot.\n_ _", inline=False)
    embed_topic.add_field(name="__**Aliases**__", value="`topics`, `topic`\n_ _", inline=False)
    embed_topic.set_footer(text="Bot created by Pick A Username#8826")
    if args == "topics" or args == "topic":
        await ctx.send(embed=embed_topic)
        return
    #retrieve
    embed_retrieve = discord.Embed(title="__**Retrieve**__", colour=colour)
    embed_retrieve.add_field(name="__**Usage**__", value="`s.retrieve <topic>`\n_ _", inline=False)
    embed_retrieve.add_field(name="__**Description**__", value="Gives you questions related to your topic. The bot must be able to DM you.\n_ _", inline=False)
    embed_retrieve.add_field(name="__**Aliases**__", value="`r`, `retrieve`, `retrieval`\n_ _", inline=False)
    embed_retrieve.set_footer(text="Bot created by Pick A Username#8826")
    if args == "r" or args == "retrieve" or args == "retrieval":
        await ctx.send(embed=embed_retrieve)
        return
    #ping
    embed_ping = discord.Embed(title="__**Ping**__", colour=colour)
    embed_ping.add_field(name="__**Usage**__", value="`s.ping`\n_ _", inline=False)
    embed_ping.add_field(name="__**Description**__", value="Gives you the bot latency in ms.\n_ _", inline=False)
    embed_ping.set_footer(text="Bot created by Pick A Username#8826")
    if args == "ping":
        await ctx.send(embed=embed_ping)
        return
    #help
    embed_help = discord.Embed(title="__**Help**__", colour=colour)
    embed_help.add_field(name="__**Usage**__", value="`s.help [command=None]`\n_ _", inline=False)
    embed_help.add_field(name="__**Description**__", value="Brings up the help embed. Can be used to get more information on a command.\n_ _", inline=False)
    embed_help.add_field(name="__**Aliases**__", value="`help`, `h`\n_ _", inline=False)
    embed_help.set_footer(text="Bot created by Pick A Username#8826")
    if args == "h" or args == "help":
        await ctx.send(embed=embed_help)
        return
    #equation
    embed_eq = discord.Embed(title="__**Equation**__", colour=physicsc)
    embed_eq.add_field(name="__**Usage**__", value="`s.equation [module|equation=None]`\n_ _", inline=False)
    embed_eq.add_field(name="__**Description**__", value="Gives you physics equations. One of the equations will need your DMs on.\n_ _", inline=False)
    embed_eq.add_field(name="__**Aliases**__", value="`eq`, `equation`\n_ _", inline=False)
    embed_eq.set_footer(text="Bot created by Pick A Username#8826")
    if args == "eq" or args == "equation":
        await ctx.send(embed=embed_eq)
        return
    #esym
    embed_esym = discord.Embed(title="__**Esym**__", colour=physicsc)
    embed_esym.add_field(name="__**Usage**__", value="`s.esym`\n_ _", inline=False)
    embed_esym.add_field(name="__**Description**__", value="Shows you all the electrical symbols used in circuits.\n_ _", inline=False)
    embed_esym.add_field(name="__**Aliases**__", value="`esym`, `electricalsymbols`, `esymbol`, `esymbols`, `electricsymbol`, `electricsymbols`, `electricalsymbol`\n_ _", inline=False)
    embed_esym.set_footer(text="Bot created by Pick A Username")
    esym_list = ['esym', 'electricalsymbols', 'esymbol', 'esymbols', 'electricsymbol', 'electricsymbols', 'electricalsymbol']
    if args in esym_list:
        await ctx.send(embed=embed_esym)
        return
    #iv
    embed_iv = discord.Embed(title="__**IV**__", colour=physicsc)
    embed_iv.add_field(name="__**Usage**__", value="`s.iv`\n_ _", inline=False)
    embed_iv.add_field(name="__**Description**__", value="Shows the three I-V graphs.\n_ _", inline=False)
    embed_iv.add_field(name="__**Aliases**__", value="`iv`, `i-v`\n_ _", inline=False)
    embed_iv.set_footer(text="Bot created by Pick A Username#8226")
    if args == "iv" or args == "i-v":
        await ctx.send(embed=embed_iv)
        return
    #circuit
    embed_circuit = discord.Embed(title="__**Circuit**__", colour=physicsc)
    embed_circuit.add_field(name="__**Usage**__", value="`s.circuit [parallel|series|None]`\n_ _", inline=False)
    embed_circuit.add_field(name="__**Description**__", value="Shows how voltage, amps and resistance are calculated in parallel and series circuits.\n_ _", inline=False)
    embed_circuit.add_field(name="__**Aliases**__", value="`c`, `circuit`, `circuits`\n_ _", inline=False)
    embed_circuit.set_footer(text="Bot created by Pick A Username#8826")
    if args == "c" or args == "circuits" or args == "circuit":
        await ctx.send(embed=embed_circuit)
        return
    #radiation
    embed_radiation = discord.Embed(title="__**Radiation**__", colour=physicsc)
    embed_radiation.add_field(name="__**Usage**__", value="`s.radiation`\n_ _", inline=False)
    embed_radiation.add_field(name="__**Description**__", value="Shows the properties of alpha, beta and gamma radiation.\n_ _", inline=False)
    embed_radiation.add_field(name="__**Aliases**__", value="`radiation`, `radiate`, `alpha`, `beta`, `gamma`\n_ _", inline=False)
    embed_radiation.set_footer(text="Bot created by Pick A Username#8826")
    radiation_list = ['radiation', 'radiate', 'alpha', 'gamma', 'beta']
    if args in radiation_list:
        await ctx.send(embed=embed_radiation)
        return
    #pt
    embed_pt = discord.Embed(title="__**pt**__", colour=chemc)
    embed_pt.add_field(name="__**Usage**__", value="`s.pt`\n_ _", inline=False)
    embed_pt.add_field(name="__**Description**__", value="Shows the periodic table.\n_ _", inline=False)
    embed_pt.add_field(name="__**Aliases**__", value="`pt`, `p-t`, `periodictable`\n_ _", inline=False)
    embed_pt.set_footer(text="Bot created by Pick A Username#8826")
    if args == "pt" or args == "p-t" or args == "periodictable":
        await ctx.send(embed=embed_pt)
        return
    #rp
    embed_rp = discord.Embed(title="__**rp**__", colour=chemc)
    embed_rp.add_field(name="__**Usage**__", value="`s.rp [exo|endo|None]`\n_ _", inline=False)
    embed_rp.add_field(name="__**Description**__", value="Shows you reaction profiles.\n_ _", inline=False)
    embed_rp.add_field(name="__**Aliases**__", value="`rp`, `reactionprofies`, `reaction`, `reaction-profile`\n_ _", inline=False)
    embed_rp.set_footer(text="Bot created by Pick A Username#8826")
    if args == "rp" or args == "reactionprofiles" or args == "reaction" or args == "reaction-profile":
        await ctx.send(embed=embed_rp)
        return
    #cell
    embed_cell = discord.Embed(title="__**Cell**__", colour=bioc)
    embed_cell.add_field(name="__**Usage**__", value="`s.cell`\n", inline=False)
    embed_cell.add_field(name="__**Description**__", value="Shows you the sub-cellular structures of a plant and animal cell.\n", inline=False)
    embed_cell.set_footer(text="Bot created by Pick A Username#8826")
    if args == "cell":
        await ctx.send(embed=embed_cell)
        return
    #transport
    embed_transport = discord.Embed(title="__**Transport**__", colour=bioc)
    embed_transport.add_field(name="__**Usage**__", value="`s.transport`\n", inline=False)
    embed_transport.add_field(name="__**Description**__", value="Shows you how particles and water molecules move with the different types of transport.\n", inline=False)
    embed_transport.add_field(name="__**Aliases**__", value="`transport, `transportation`, `diffusion`, `osmosis`, `active-transport`, `activetransport`\n_ _", inline=False)
    embed_transport.set_footer(text="Bot created by Pick A Username#8826")
    if args == "transport":
        await ctx.send(embed=embed_transport)
        return
    await ctx.send("No help command for `{}`.".format(args))

change_status.start()

#keep_alive()

client.run("TOKEN")
