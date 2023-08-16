from pyrogram import Client, filters
import subprocess
import os
from os import system as cmd
import shutil


bot = Client(
    "vidmaker",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5714654934:AAEVIR8baWhJcgUOtWeNmrSjvdRfYRiY7tI"
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

@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice )
def _telegram2_file(client, message):
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
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.audio
  global file_path
  file_path = message.download(file_name="aud")
  global mp4file
  mp4file="mp4file.mp4"
  cmd(f'''ffmpeg -r 1 -loop 1 -y -i  downloads/pic -i downloads/aud -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "mp4file.mp4"''')

  with open(f'{mp4file}', 'rb') as f:
        bot.send_video(user_id, f)
  shutil.rmtree('./downloads/')
  cmd(f'rm {mp4file}')


bot.run()
