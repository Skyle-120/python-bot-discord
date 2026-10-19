import discord
from discord.ext import commands
from bot_logic import gen_pass, flip_coin, gen_emodji

# Configurazione degli intents
intents = discord.Intents.default()
intents.message_content = True

# Creazione del bot con prefisso '$'
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')

@bot.command(name='ciao')
async def ciao(ctx):
    await ctx.send("Ciao!")

@bot.command(name='arrivederci')
async def arrivederci(ctx):
    await ctx.send("\U0001f642")

@bot.command(name='smile')
async def smile(ctx):
    await ctx.send(gen_emodji())

@bot.command(name='coin')
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(name='password')
async def password(ctx):
    await ctx.send("La tua password " + gen_pass(30))

@bot.command(name='comandi')
async def comandi(ctx):
    await ctx.send("""**I comandi disponibili sono:**
- Lancio moneta: `$coin`
- Genera password: `$password`
- Emoji casuale: `$smile`
- Benvenuto: `$ciao`
- Arrivederci: `$arrivederci`""")

# Gestione dei comandi non riconosciuti
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("""**Comando non riconosciuto. I comandi disponibili sono:**
- Lancio moneta: `$coin`
- Genera password: `$password`
- Emoji casuale: `$smile`
- Benvenuto: `$ciao`
- Arrivederci: `$arrivederci`""")

bot.run("MTU1OTI1Nzc5NTI0MzY3NTc2OA.GUMBEu.9MY7OcFF6bvWTSH7bxNHLDdoW5K1XCu0sloTT8")
