from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply,Message
from pyrogram import Client, filters,enums,StopTransmission
import os ,re ,random ,shutil,asyncio 
bot = Client(
    "montagbot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E"
)
#6032076608:AAGhqffAlibHd7pipzA3HR2-0Ca3sDFlmdI 
#5782497998:AAFdx2dX3yeiyDIcoJwPa_ghY2h_dozEh_E
#6306753444:AAFnoiusUbny-fpy4xxZWYqGNh_c7yOioW8
#6709809460:AAGWWXJBNMF_4ohBNRS22Tg0Q3-vkm376Eo
#6466415254:AAE_m_mYGHFuu3MT4T0qzqVCm0WvR4biYvM
#6812722455:AAEjCb1ZwgBa8DZ4_wVNNjDZbe6EtQZOUxo
photolist = []
audiolist = []
videolist = []
audiolistconv = []
audioexs = [".mp3",".ogg",".m4a"]
photoexs = [".jpg",".png"]

async def downloadtoserver(x):
 global user_id ,file_path,filename,nom,ex,mp4file,mp3file,m4afile,spdrateaud,mergdir,trimdir,result,y
 file_path = await x.download(file_name="./downloads/")
 filename = os.path.basename(file_path)
 nom,ex = os.path.splitext(filename)
 mp4file = f"{random.randint(1,1000)}.mp4"
 mp3file = f"{random.randint(1,1000)}.mp3"
 user_id = x.from_user.id
 mergdir = f"./mergy/{mp3file}"
 trimdir = f"./trimmo/{mp3file}"
 y = f"./downloads/{random.randint(1,1000)}{ex}"
 os.rename(file_path,y) 

@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document | filters.photo | filters.animation )
async def _telegram_file(client, message):
   await downloadtoserver(message)
   if ex in photoexs : 
      photolist.append(y)
      videolist.append(mp4file)
   elif ex in audioexs : 
        audiolist.append(y)
        audiolistconv.append(mp3file)
   await message.reply("بعد الانتهاء أرسل الأمر /monow" , quote=True)
@bot.on_message(filters.command('monow') & filters.text & filters.private)
def command4(bot,message):
   for x in range(0,len(audiolist)):
    cmd(f'''ffmpeg -i "{audiolist[x]}" -q:a 0 -map a "{audiolistconv[x]}" -y ''')
    cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "{photolist[x]}" -i "{audiolistconv[x]}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{videolist[x]}"''')
    bot.send_video(user_id,videolist[x])
    os.remove(videolist[x])
    os.remove(photolist[x])
    os.remove(audiolist[x])
    os.remove(audiolistconv[x])
   audiolist.clear()
   videolist.clear()
   audiolistconv.clear()
   photolist.clear()
   message.reply("تمت المنتحة ✅" , quote=True)



bot.run()

      


   
