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
SESSION      = os.environ.get("SESSION", "BQGd24oAOq06Q6MSok4FcaqegusJzbKQXjhPFwtwycA5PCpVjlOyD3W_vAWX8RRCtnaIgVg6eP_GZa2FZfz6EqeXI0tePuOdJl_LH3Jx_lSYj7mTvNWYh9un1Hm0Mzaq9gDzTkK4kD18XnYAMbpbZuWI20YsEffRtRyYOYzTZWjJORGQhgz1E7-V3ZeilVVMWRBaXxBt5eB9ptuq-5WS8-BktvYk0vUA6_OzIyBSpMHsxRykbeWS9E1MzrkdF1g7cKH1LxM_3m9Ga7IXcnynuKrEgyCmV-OCxMeKe0HUml4JoIczyN79L6aZeC6rDUeUoJKFHYLPytWi-QvwLVgWCtFXy3UwhAAAAAHHz7TjAA")
TIME         = int(os.environ.get("TIME", 1))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002354529839").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://teekam9079:teekam@teekam.cludf.mongodb.net/?retryWrites=true&w=majority&appName=Teekam")
PORT         = os.environ.get("PORT", "8080")
