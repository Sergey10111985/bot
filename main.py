import requests
import telebot
from bs4 import BeautifulSoup

t_token = '1258725940:AAEd8aDB33v_6e30tWHa18jf1A1Mo4p7VdQ'


def find(country, lis):
    for i in range(len(lis)):
        if country.lower() == str(lis[i][1]).lower():
            return i
    return 0


def get_one(user_request):
    url1 = "https://www.worldometers.info/coronavirus"
    r = requests.get(url1)
    soap = BeautifulSoup(r.text, 'html.parser')

    table = soap.find("table")
    row = table.find_all("tr")
    li = []

    for i in row:
        li.append(i.text.split('\n'))

    if find(str(user_request), li):
        return (li[find(str(user_request), li)])
    else:
        return []


def gether_data(mas):
    if mas:
        for i in range(len(mas)):
            if mas[i] == '':
                mas[i] = 'No Data'
        mes = ("Country: {0}\nTotal Cases: {1}\nNew Cases: "
               "{2}\nTotal Deaths:{3}\nTotal Recovered: {4}\nActive Cases: {5}").format(mas[1],
                                                                                        mas[2],
                                                                                        mas[3],
                                                                                        mas[4],
                                                                                        mas[6],
                                                                                        mas[7], )

    else:
        mes = "No such country in our base..."

    return mes


bot = telebot.TeleBot(t_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Greetengs!!!\nEnter the country that you are "
                          "interested in situation COVID-19")


@bot.message_handler()
def send_data(message):
    country = message.text
    mas = get_one(country)

    bot.send_message(message.chat.id, gether_data(mas))


bot.polling(none_stop=True)
