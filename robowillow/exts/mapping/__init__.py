from .mapping_cog import Mapper

def setup(bot):
    bot.add_cog(Mapper(bot))
