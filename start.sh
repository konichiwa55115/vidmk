echo "Cloning Repo...."
cd /LazyDeveloper
git clone https://github.com/konichiwa55115/vidmk
git clone https://github.com/GregorR/rnnoise-models
pip3 install -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 bot.py
