# -*- encoding:utf-8 -*-
from GuDice import Event


class PluginEvent(Event):
    def private_message(self, data, bot):
        if data.message == "咕":
            bot.send_private_msg(2432115441, "咕")
