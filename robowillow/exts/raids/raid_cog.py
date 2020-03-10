"""Commands for raid organization and information."""
from discord.ext.commands import Cog, command, has_permissions
from robowillow.utils import pokemap
from robowillow.utils import database as db
from . import raid_checks
import requests


class Raids(Cog):
    """Cog for raid help commands."""

    def __init__(self, bot):
        """Start the raid cog."""
        self.bot = bot
        response = requests.get("https://fight.pokebattler.com/raids")
        self.raids = response.json()['tiers']

    @command()
    @raid_checks.raid_channel()
    async def infographic(self, ctx, pokemon=None):
        """Return the pokebattler infographic for a pokemon if it exists."""
        if pokemon is None:
            pass
        else:
            match = pokemap.match_pokemon(pokemon)
            if match is None:
                await ctx.send("Pokemon not found.")
                return
            for tier in self.raids:
                for index in self.raids[tier]['raids']:
                    if match.upper() in self.raids[tier]['raids'][index]['pokemon']:
                        if self.raids[tier]['raids'][index]['article'] is None:
                            pass
                        else:
                            url = self.raids[tier]['raids'][index]['article']['infographicShareURL']
                            await ctx.send(url)
                            return
            await ctx.send("Pokemon not found in pokebattler.")
