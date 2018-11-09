import telegram
from pytube import YouTube
import subprocess
import os


def main():
    token = '781330833:AAEyaTY2MiIq6411OmWJjARt0Gl61kk8jBQ'
    bot = telegram.Bot(token=token)

    from telegram.ext import Updater
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    from telegram.ext import MessageHandler, Filters
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    from telegram.ext import CommandHandler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    falae_handler = CommandHandler('falae', falae)
    dispatcher.add_handler(falae_handler)

    audio_handler = CommandHandler('audio', audio)
    dispatcher.add_handler(audio_handler)

    audio_handler = CommandHandler('search', search)
    dispatcher.add_handler(audio_handler)

    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    updater.start_polling()


id = ''


def search(bot, update):
    DEVELOPER_KEY = 'AIzaSyDGRbEc7qbGJ59Vsv68fL0aHml1FYpX_1g'
    import yapi
    api = yapi.YoutubeAPI(DEVELOPER_KEY)
    keyword = update.message.text.split('/search')[1]
    print(keyword)
    results = api.general_search(keyword, max_results=5)
    import json
    results = json.loads(results)
    result = ''
    global id
    id = ''
    for i in range(5):
        result += str(i) + " - " + results['items'][i]['snippet']['title'] + " \n \n"
        id += results['items'][i]['id']['videoId'] + " \n"
    print(result)
    bot.send_message(chat_id=update.message.chat_id, text=result)
    bot.send_message(chat_id=update.message.chat_id,
                     text='Você quer baixar o video? Qual resultado quer baixar?\nDigite Sim (e o número que deseja)\nExemplo: Sim 5')

    # bot.send_photo(chat_id=update.message.chat_id, photo=results['items'][0]['snippet']['thumbnails']['default']['url'])

    # print(results['items'][0]['snippet']['title'])
    # print(results['items'][0]['snippet']['thumbnails']['default']['url'])
    # print(results['items'][0]['id']['videoId'])


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Mande seu video")


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Se você já tem o link do video, mande para mim o link do video para baixar ele !! \n \nSe quiser procurar algum video digite\nExemplo: "
                          "/search meu mundo \n \n"
                          "Depois que você procurar ele vai te passar uma lista de resultado \n \n"
                          "Para baixar o video que deseja digite O número do video \nExemplo: 3")


def falae(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Mande seu video")
"""
def path():
    from os import listdir
    from os.path import isfile, join
    import subprocess
    mypath = 'C:\\Users\\thiago.alves.EXTRABOM\\Desktop\\pl'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # print(onlyfiles)

    for path in onlyfiles:
        print(path)
"""
def audio(bot, update):
    print("enviando")
    bot.send_audio(chat_id=update.message.chat_id, audio=open(r'C:\Users\thiago.alves.EXTRABOM\PycharmProjects\WhatsDown\ãb.mp3', 'rb')
                   , timeout=999,title= 'ãbc')
    print("enviado")


def echo(bot, update):
    print(update.message.text)
    if 'playlist' in update.message.text.lower():
        from pytube import Playlist
        import threading
        import time

        pl = Playlist('https://www.youtube.com/playlist?list=PLQuDmj3ez49wUERdKxZYfoDVESQuvppH2')
        bot.send_message(chat_id=update.message.chat_id, text="São " + str(len(pl.parse_links())) + " videos \nEstou baixando :D")
        for link in pl.parse_links():
            threading.Thread(target=download,args=(link,)).start()
            bot.send_message(chat_id=update.message.chat_id,
                             text="Estou baixando o video \n" + getTitle(link))
            time.sleep(5)

    elif 'https' in update.message.text:
        link = update.message.text
        title = getTitle(link)
        bot.send_message(chat_id=update.message.chat_id, text="Estou baixando seu video, " + title)
        music = download(link)
        bot.send_message(chat_id=update.message.chat_id, text="Seu video foi baixado, estou lhe enviando o seu audio")
        print("enviando")
        bot.send_audio(chat_id=update.message.chat_id, audio=open(music, 'rb'), title=title, timeout=999)
        print("enviado")
    elif int(update.message.text) < 5:

        print(int(update.message.text))
        global id
        id = id.split('\n')
        id = id[int(update.message.text)]
        link = 'https://youtu.be/' + id
        title = getTitle(link)
        bot.send_message(chat_id=update.message.chat_id, text="Estou baixando seu video, " + title)
        music = download(link)
        bot.send_message(chat_id=update.message.chat_id, text="Seu video foi baixado, estou lhe enviando o seu audio")
        print("enviando")
        bot.send_audio(chat_id=update.message.chat_id, audio=open(music, 'rb'), title=title.encode(encoding='utf-8'), timeout=999)
        print("enviado")
        os.remove(music)


def getTitle(link):
    return YouTube(link).title


def download(link):
    yt = YouTube(link)
    videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    print(videos.default_filename)
    music = videos.default_filename
    music = music[:len(music) - 1] + '3'
    print(music)
    videos.download()
    subprocess.call(['ffmpeg', '-i', videos.default_filename, music])
    os.remove(videos.default_filename)

    return music

    # bot.send_photo(chat_id=update.message.chat_id, photo=yt.example)

    # bot.send_video(chat_id=update.message.chat_id, video=open('MODETIA - Trip [ Official Video ] (Prod Da77ass & Kizzy).mp4', 'rb'), supports_streaming=True)
    # bot.send_video(chat_id=update.message.chat_id,audio=open(r'C:\Users\thiago.alves.EXTRABOM\Py\a.mp4','rb'),timeout=999,supports_streaming=True)

    # bot.send_video(chat_id=update.message.chat_id, audio=open(videos.default_filename, 'rb'),
    # timeout=999, supports_streaming=True)


main()
