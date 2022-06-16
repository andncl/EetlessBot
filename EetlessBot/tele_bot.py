import logging
from telegram import Update
from telegram.ext import filters, MessageHandler,ApplicationBuilder, CallbackContext, CommandHandler
from meal_class import Meal
from message_analysis_rt import message_analyser
import splitwise

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

meal = Meal()


help_text = """The following commands are available:
    /help -> This message.
    /status -> Prints a snapshot of the current meal.
    /howmany -> Tells you the current amount of eaters.
    k -> Creates a new meal with you as a cook.
    e -> Adds you as a member of an announced meal.
    +N -> Adds N external people on your bill to the meal.
    x -> Removes you as a member from the meal.
    si -> Closes the eating inquiry if you are cooking.
    name -> Adds person wih the given first name (must live at Atlas).
    /price XX.XX -> Registers XX.XX Euro as payed by the person sending this command and splits the costs accordingliy among the participants.

    /"""
    

async def help(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message( chat_id=update.effective_chat.id,text=help_text)

async def status(update: Update, context: CallbackContext.DEFAULT_TYPE):
    response = meal.show_member_list()
    print(response)
    await context.bot.send_message( chat_id=update.effective_chat.id,text=response)

async def how_many(update: Update, context: CallbackContext.DEFAULT_TYPE):
    response = meal.calc_total_members()
    await context.bot.send_message( chat_id=update.effective_chat.id,text=response)

async def normal_msg(update: Update, context: CallbackContext.DEFAULT_TYPE):
    msg = update.message.text
    user = update.message.from_user
    user_name = user['first_name']
    print(msg,user_name)
    reply_list = meal.message_analyser(user_name, msg)

    for answer in reply_list:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

async def price(update: Update, context: CallbackContext.DEFAULT_TYPE):
    
    print(context.args)
    if len(context.args)==1:
        response = meal.calc_balance(update.message.from_user['first_name'],float(context.args[0]))
    else:
        response = "Please give me jusr one number, separated by a dot like: /price 12.20"

    print(response)
    await context.bot.send_message( chat_id=update.effective_chat.id,text=response)


if __name__ == '__main__':
    

    application = ApplicationBuilder().token('5595874439:AAHwLb6NOoObZq5nvf-k3CcazYQ6SPNCfYE').build()

    help_handler = CommandHandler('help', help)
    status_handler = CommandHandler('status', status)
    howmany_handler = CommandHandler('howmany', how_many)
    price_handler = CommandHandler('price', price)
    cmd_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), normal_msg)

    application.add_handler(help_handler)
    application.add_handler(status_handler)
    application.add_handler(howmany_handler)
    application.add_handler(price_handler)
    application.add_handler(cmd_handler)
    
    application.run_polling()
