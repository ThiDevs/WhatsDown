import telegram
from pytube import YouTube
import subprocess


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

    updater.start_polling()


id = ''


def search(bot, update):
    DEVELOPER_KEY = 'AIzaSyDGRbEc7qbGJ59Vsv68fL0aHml1FYpX_1g'
    import yapi
    api = yapi.YoutubeAPI(DEVELOPER_KEY)
    keyword = update.message.text.split('/search')[1]
    print(keyword)
    results = api.general_search(keyword, max_results=1)
    import json
    results = json.loads(results)
    result = results['items'][0]['snippet']['title']
    print(result)
    bot.send_message(chat_id=update.message.chat_id, text=result)
    bot.send_message(chat_id=update.message.chat_id, text='Você quer baixar-lo?')
    global id
    id = results['items'][0]['id']['videoId']
    bot.send_photo(chat_id=update.message.chat_id, photo=results['items'][0]['snippet']['thumbnails']['default']['url'])

    # print(results['items'][0]['snippet']['title'])
    # print(results['items'][0]['snippet']['thumbnails']['default']['url'])
    # print(results['items'][0]['id']['videoId'])


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Mande seu video")


def falae(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Mande seu video")


def audio(bot, update):
    print("enviando")
    bot.send_audio(chat_id=update.message.chat_id, audio=open(r'C:\Users\thiago.alves.EXTRABOM\Py\abc.mp3', 'rb'),
                   title="abc223", timeout=999)
    print("enviado")


def echo(bot, update):
    print(update.message.text)
    if 'https' in update.message.text:
        yt = YouTube(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text="Estou baixando seu video, " + yt.title)
        videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(videos.default_filename)
        music = videos.default_filename
        music = music[:len(music) - 1] + '3'
        print(music)
        videos.download()
        subprocess.call(['ffmpeg', '-i', videos.default_filename, music])

        bot.send_message(chat_id=update.message.chat_id, text="Seu video foi baixado, estou lhe enviando o seu audio")
        # bot.send_photo(chat_id=update.message.chat_id, photo=yt.example)
        print("enviando")
        # bot.send_video(chat_id=update.message.chat_id, video=open('MODETIA - Trip [ Official Video ] (Prod Da77ass & Kizzy).mp4', 'rb'), supports_streaming=True)
        # bot.send_video(chat_id=update.message.chat_id,audio=open(r'C:\Users\thiago.alves.EXTRABOM\Py\a.mp4','rb'),timeout=999,supports_streaming=True)
        bot.send_audio(chat_id=update.message.chat_id, audio=open(music, 'rb'), title=yt.title, timeout=999)
        print("enviado")
    elif (update.message.text == 'Sim') or (update.message.text == 'sim'):
        global id
        yt = YouTube('https://youtu.be/' + id)
        bot.send_message(chat_id=update.message.chat_id, text="Estou baixando seu video, " + yt.title)
        videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        print(videos.default_filename)
        music = videos.default_filename
        music = music[:len(music) - 1] + '3'
        print(music)
        videos.download()
        subprocess.call(['ffmpeg', '-i', videos.default_filename, music])

        bot.send_message(chat_id=update.message.chat_id, text="Seu video foi baixado, estou lhe enviando o seu audio")
        # bot.send_photo(chat_id=update.message.chat_id, photo=yt.example)
        print("enviando")
        # bot.send_video(chat_id=update.message.chat_id, video=open('MODETIA - Trip [ Official Video ] (Prod Da77ass & Kizzy).mp4', 'rb'), supports_streaming=True)
        # bot.send_video(chat_id=update.message.chat_id,audio=open(r'C:\Users\thiago.alves.EXTRABOM\Py\a.mp4','rb'),timeout=999,supports_streaming=True)
        bot.send_audio(chat_id=update.message.chat_id, audio=open(music, 'rb'), title=yt.title, timeout=999)
        print("enviado")


main()