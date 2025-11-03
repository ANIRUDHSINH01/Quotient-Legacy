from discord.ext import commands


class EspotiveError(commands.CheckFailure):
    pass


class NotSetup(EspotiveError):
    def __init__(self):
        super().__init__(
            "This command requires you to have Espotive's private channel.\nKindly run `{ctx.prefix}setup` and try again."
        )


class NotPremiumGuild(EspotiveError):
    def __init__(self):
        super().__init__(
            "This command requires this server to be premium.\n\nCheckout Espotive Premium [here]({ctx.bot.prime_link})"
        )


class NotPremiumUser(EspotiveError):
    def __init__(self):
        super().__init__(
            "This command requires you to be a premium user.\nCheckout Espotive Premium [here]({ctx.bot.prime_link})"
        )


class InputError(EspotiveError):
    pass


class SMNotUsable(EspotiveError):
    def __init__(self):
        super().__init__("You need either the `scrims-mod` role or `Manage Server` permissions to use this command.")


class TMNotUsable(EspotiveError):
    def __init__(self):
        super().__init__("You need either the `tourney-mod` role or `Manage Server` permissions to use tourney manager.")


class PastTime(EspotiveError):
    def __init__(self):
        super().__init__(
            f"The time you entered seems to be in past.\n\nKindly try again, use times like: `tomorrow` , `friday 9pm`"
        )


TimeInPast = PastTime


class InvalidTime(EspotiveError):
    def __init__(self):
        super().__init__(f"The time you entered seems to be invalid.\n\nKindly try again.")
