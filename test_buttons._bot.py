import time
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
 
BOT_TOKEN='1429113658:AAEi5BmzzzV4jGKXWE3z8GabcA5MGSiVOgg'
 
updater = Updater( token=BOT_TOKEN, use_context=True )
dispatcher = updater.dispatcher
 
def cmd_task_buttons(update, context):
    task_buttons = [[
        InlineKeyboardButton( '1.네이버 뉴스', callback_data=1 )
        , InlineKeyboardButton( '2.직방 매물', callback_data=2 )
    ], [
        InlineKeyboardButton( '3.취소', callback_data=3 )
    ]]
    
    reply_markup = InlineKeyboardMarkup( task_buttons )
    
    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='작업을 선택해주세요.'
        , reply_markup=reply_markup
    )
    

    
def crawl_navernews():
    time.sleep( 5 )
    print( '네이버에서 뉴스를 수집했다.' )
    
def crawl_zigbang():
    time.sleep( 5 )
    print( '직방에서 매물을 수집했다.' )
    
task_buttons_handler = CommandHandler( 'tasks', cmd_task_buttons )
  
 
dispatcher.add_handler( task_buttons_handler )

 
updater.start_polling()
updater.idle()
