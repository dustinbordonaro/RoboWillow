from .admin_cog import Admin

def setup(bot):
    bot.add_cog(Admin(bot))
