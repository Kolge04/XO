from pyrogram import Client
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent

api_id = 3330082
api_hash = 'a8c8207cff88b514f9906e2f58ddb123'
bot_token = '1602446423:AAGzEXvQiLgC8AE-rT9emdcTsJmffcg1e2c'

##############################################################################################################################################

round = 0
table = [[('1','block00'), ('2','block01'), ('3','block02')],[('4','block10'), ('5','block11'), ('6','block12')],[('7','block20'), ('8','block21'), ('9','block22')]]

def IKM2D(table):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd) for text, cbd in row] for row in table])
def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd) for text, cbd in row] for row in data])


client = Client(session_name = 'My_Bot', bot_token = bot_token, api_id = api_id, api_hash = api_hash)
Ps = []

#====================================================================================================================================================

@client.on_message()
def handle_message(bot,message) :
    if message.text :
        if message.text == '/start' :
            bot.send_message(message.chat.id, '''👋  Hi

👍  Thanks for playing with my XO Bot !''', reply_markup = ReplyKeyboardMarkup([['❌⭕️ Play ⭕️❌'], ['🌐 Credit 📝']]))

        elif message.text == '🌐 Credit 📝' :
            bot.send_message(message.chat.id, '''🔥  Written & Developed by  🔥
            
            😎 Yousof Asadi 😎 :
               @Yousof_Asadi''')

        elif message.text == '❌⭕️ Play ⭕️❌':
            bot.send_message(message.chat.id,'''😢 Sorry , this bot is inline.
☺️ You can use it by typing @XO_YA_bot in a group or private chat of your friends. ''', reply_markup = ReplyKeyboardRemove())

########################################################################################################################################

def check_winner (table) :

    if table[0][0][0] == table[0][1][0] == table[0][2][0] :
        return table[0][0][0]
    elif table[1][0][0] == table[1][1][0] == table[1][2][0] :
        return table[1][0][0]
    elif table[2][0][0] == table[2][1][0] == table[2][2][0] :
        return table[2][0][0]
    elif table[0][0][0] == table[1][0][0] == table[2][0][0] :
        return table[0][0][0]
    elif table[0][1][0] == table[1][1][0] == table[2][1][0] :
        return table[0][1][0]
    elif table[0][2][0] == table[1][2][0] == table[2][2][0] :
        return table[0][2][0]
    elif table[1][1][0] == table[2][2][0] == table[0][0][0] :
        return table[1][1][0]
    elif table[1][1][0] == table[2][0][0] == table[0][2][0] :
        return table[1][1][0]

###########################################################################################################################
round = 0
@client.on_callback_query()
def handle_callback_query(bot, query) :
    global round, Ps, table

    if not query.from_user.username in Ps :
       Ps += [query.from_user.username]

    if query.data.startswith('block') :

        i = int(query.data[5])
        j = int(query.data[6])


        if round % 2 == 0 and query.from_user.username == Ps[1] :
            if table[i][j][0] == '🅾️️' or table[i][j][0] == '❎':
                bot.answer_callback_query(query.id, '''😑 Please choose another block
    This one is chosen !!!''', show_alert=True)
            else :
                table[i][j] = ('❎', query.data)
                round += 1
                bot.edit_inline_text(query.inline_message_id, f'''❎🅾️ Game
                            
⏭ Turn: @{Ps[0]} as 🅾️''', reply_markup=IKM2D(table))

        elif round % 2 != 0 and query.from_user.username == Ps[0] :
            if table[i][j][0] == '🅾️️' or table[i][j][0] == '❎' :
                bot.answer_callback_query(query.id, '''😑 Please choose another block
    This one is chosen !!!''' , show_alert=True)
            else :
                table[i][j] = ('🅾️️', query.data)
                round += 1
                bot.edit_inline_text(query.inline_message_id, f'''❎🅾️ Game

⏭ Turn: @{Ps[1]} as ❎''', reply_markup=IKM2D(table))

        elif round % 2 != 0 and query.from_user.username == Ps[1] :
            bot.answer_callback_query(query.id, '😕 It`s not your turn !!! ', show_alert=True)

        elif round % 2 == 0 and query.from_user.username == Ps[0] :
            bot.answer_callback_query(query.id, '😕 It`s not your turn !!! ', show_alert=True)

        if check_winner(table) :
            bot.edit_inline_text(query.inline_message_id , f'''🥳 @{query.from_user.username} Wins as {check_winner(table)}
            
Play Again :)!!! 💪''', reply_markup= IKM([[('❌⭕️ Play Again ⭕️❌','start0')]]))
            bot.answer_callback_query(query.id, '🥳🥳🥳 You won !!!!!', show_alert=True)
            Ps = []
            round = 0
            table = [[('1', 'block00'), ('2', 'block01'), ('3', 'block02')], [('4', 'block10'), ('5', 'block11'), ('6', 'block12')], [('7', 'block20'), ('8', 'block21'), ('9', 'block22')]]

        elif round == 9 :
            bot.edit_inline_text(query.inline_message_id , '🎲 Tie! Play Again :)', reply_markup= IKM([[('❌⭕️ Play Again ⭕️❌','start0')]]))
            Ps = []
            round = 0
            table = [[('1', 'block00'), ('2', 'block01'), ('3', 'block02')], [('4', 'block10'), ('5', 'block11'), ('6', 'block12')], [('7', 'block20'), ('8', 'block21'), ('9', 'block22')]]

    elif query.data == 'start0' and query.from_user.username == Ps[0]:
        bot.edit_inline_text(query.inline_message_id,'🥱 Waiting for second player ...', reply_markup=IKM([[('❌⭕️ Tap to Play ⭕️❌', 'start1')]]))
        bot.answer_callback_query(query.id, '''🥱 Wait for another player ...
You are the first player !!''', show_alert=True)

    elif query.data == 'start1' and query.from_user.username == Ps[0] :
        bot.answer_callback_query(query.id, '🥱 Wait for another player ...', show_alert=True)

    elif query.data == 'start1' and query.from_user.username == Ps[1]:
        bot.answer_callback_query(query.id, '''😉 Accepted ...
You are the second player !!''', show_alert=True)
        bot.edit_inline_text(query.inline_message_id, f'''❎🅾️ Game
        
📜 Rule: Second player always starts the match as ❎ !!

⏭ Turn:  @{query.from_user.username} as ❎''', reply_markup=IKM2D(table))
    elif query.data == 'start0' and query.from_user.username == Ps[1]:
        bot.edit_inline_text(query.inline_message_id, '🥱 Waiting for second player ...', reply_markup=IKM([[('❌⭕️ Tap to Play ⭕️❌', 'start1')]]))
        bot.answer_callback_query(query.id, '''🥱 Wait for another player ...
You are the first player !!''', show_alert=True)


##############################################################################################################################################################
@client.on_inline_query()
def handle_inline_query(bot, query) :
    results = [InlineQueryResultArticle('🌐 Credit 📝', InputTextMessageContent('''🔥  Written & Developed by  🔥
            
            😎 Yousof Asadi 😎 :
               @Yousof_Asadi''')), InlineQueryResultArticle('👥 Play with Friends 🎲', InputTextMessageContent('''👋  Hi

👍  Thanks for playing with my ❎🅾️ Bot !

📜 Rule: Second player always starts the math as ❎ !!'''), reply_markup= IKM([[('❌⭕️ Tap to Play ⭕️❌','start0')]]))]
    bot.answer_inline_query(query.id, results)

################################################################################################################################

client.run()