import telebot
import constants
import psycopg2


con = psycopg2.connect(
  database = constants.database, 
  user = constants.user, 
  password = constants.password, 
  host = constants.host, 
  port = constants.port
)
print("Database opened successfully!")

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Users  
     (id INT Primary key NOT NULL,
     user_id TEXT NOT NULL,
     name TEXT NOT NULL,
     phone TEXT NOT NULL,
     is_deleted BOOLEAN);''')

cur.execute('''CREATE TABLE IF NOT EXISTS Registration  
     (id INT Primary key NOT NULL,
     user_id TEXT NOT NULL,
     name TEXT NOT NULL,
     phone TEXT NOT NULL,
     is_procesed BOOLEAN );''')

print("Table created successfully")

postgreSQL_select_user_found = "SELECT user_id from Users where user_id = %s"
postgreSQL_select_user_phone = "SELECT user_id from Users where phone = %s"

con.commit()  
con.close()

bot = telebot.TeleBot(constants.token)

# '/start'
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboardcontact = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
    button_phone = telebot.types.KeyboardButton(text="Send", request_contact=True)
    keyboardcontact.add(button_phone) 
    bot.send_message(message.chat.id, 'Send the phone number', reply_markup=keyboardcontact) 

# '/help'
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, '/start'
    '/help')
    
bot.polling()