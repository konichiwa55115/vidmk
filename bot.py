from pyrogram import Client, filters
import subprocess
import os
from os import system as cmd
import shutil


bot = Client(
    "vidmaker",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6251349619:AAHWY6-_BIwHqTUzvH62ukVUThjohP13d5k"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, "  السلام عليكم أنا بوت منتجة الفيديوهات . فقط أرسل التصميم ( الغلاف) بدون ضغط للحفاظ على جودة الفيديو \n\n Send without compression \n\n لبقية البوتات هنا \n\n https://t.me/sunnay6626/2",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.document | filters.photo)
def _telegram_file(client, message):
  try: 
    with open('mp4file.mp4', 'r') as fh:
        if os.stat('mp4file.mp4').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك عملية منتجة تتم الآن . أرسل بعد مدة من فضلك ', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id
  sent_message = message.reply_text('الآن أرسل الصوتية', quote=True)
  file = message.document
  file_path = message.download(file_name="pic")
  cmd(f'mkdir picy && mv ./downloads/pic ./picy')
  global picture
  pictrue="./picy/pic"
  shutil.rmtree('./downloads/')

    
    

@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice )
def _telegram_file(client, message):
  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية  بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  user_id = message.from_user.id
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.audio
  global file_path
  file_path = message.download(file_name="aud")
  global mp4file
  mp4file="mp4file.mp4"
  global picture
  picture = "./picy/pic"
  cmd(f'''ffmpeg -r 1 -loop 1 -y -i "{picture}" -i "{file_path}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')

  with open(f'{mp4file}', 'rb') as f:
        bot.send_video(user_id, f)
  shutil.rmtree('./downloads/')
  shutil.rmtree('./picy/')
  cmd(f'rm {mp4file}')


bot.run()
