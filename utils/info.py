#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "22349465"))
API_HASH     = os.environ.get("API_HASH", "3732e079c4125690226d8e7b4e028ca4")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "8182512235:AAEiiW-wRIbd8VgGJfpNjuvR9zHzDaPNWA8")
SESSION      = os.environ.get("SESSION", "BQFVBpkASHIHsJ848PU65EI5v03DjvJsMuC9919HsNG7Gcmu6-KgAnKL_CvrmVT-bkBrQdStc6TEpSShhAGtGgyVgEdNbzHhoh0sZ76BPT4RmK9xM4uEo9CE8vF3HHLOtOAgDNHutF-cjFYAwX6ZRCwl4bRU9CtX-8W-mPUEZTNtNvqfnjeciCqLI-sLCC4mKi7TkqQHLHp0NLXgmzioZaT6HOYvulQDRbmQhchghIhXFBYLD6dT_dMGiWlvVMnQa8nq7XySaKbmTGFZ-0E_FGA482QV4dKttCF_0jpDHZ-9TQM_kkmb_wOXVSstnKzcd67e9rsXf1m9ajpLPURpJ6nqAUACigAAAAFGAe3WAA")
TIME         = int(os.environ.get("TIME", 1))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://teekam9079:teekam@teekam.cludf.mongodb.net/?retryWrites=true&w=majority&appName=Teekam")
PORT         = os.environ.get("PORT", "8080")
