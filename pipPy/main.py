# from telegram import Update
from telegram.ext import Updater, CommandHandler # , CallbackContext
from bot_command import *




updater = Updater('5370088329:AAF4m3wT9gkPie933HgGgaMa38YIBhCC2Ho')

updater.dispatcher.add_handler(CommandHandler('hi', wazzup_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()
