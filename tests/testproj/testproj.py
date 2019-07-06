# i18n: Translator comment
_("test string")

ngettext("singular", "plural", 1)


class MyCog(commands.Cog, translator=_):
    """cog docstring"""

    @commands.command()
    @commands.is_owner()
    async def mycommand(self, ctx: commands.Context) -> None:
        """command docstring"""
        dgettext("string 1", "string 2")
        ngettext("string 3", "string 4", 3)
        dngettext("string 5", "string 6", "string 7", 4)

        await ctx.send(  # i18n: comment
            _(
                "String split "  
                "across lines"
            )
        )

        # i18n: multiline
        # comment for
        # translators
        _("string testing multiline translator comment")
        _("warning".format(x))
