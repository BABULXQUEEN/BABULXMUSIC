from JaniMusic.core.bot import Loy
from JaniMusic.core.dir import dirr
from JaniMusic.core.git import git
from JaniMusic.core.userbot import Userbot
from JaniMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Loy()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
