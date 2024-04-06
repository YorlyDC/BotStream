from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 ¡Hola!</b> {}\n 
<b>Soy un bot de transmisión de archivos y generador de enlaces directos de Telegram</b>\n
<b>Trabajo en canales y chats privados</b>\n
<b>💕 @{}</b>\n"""

    HELP_TEXT = """
<b>- Añádeme como administrador en el canal</b>
<b>- Envía cualquier archivo o medio</b>
<b>- Te proporcionaré un enlace para transmitirlo</b>\n
<b>🔞 Contenido para adultos estrictamente prohibido.</b>\n
<i><b>Reporta errores a <a href='https://telegram.me/AvishkarPatil'>el desarrollador</a></b></i>"""

    ABOUT_TEXT = """
<b>⚜ Nombre: {}</b>\n
<b>✦ Versión: {}</b>
<b>✦ Actualizado en: 06 de enero de 2024</b>
<b>✦ Desarrollador: <a href='https://telegram.me/AvishkarPatil'>Avishkar Patil</a></b>\n
"""

    STREAM_TEXT = """
<i><u>¡Tu enlace!</u></i>\n
<b>📂 Archivo:</b> <b>{}</b>\n
<b>📦 Tamaño:</b> <code>{}</code>\n
<b>📥 Descargar:</b> <code>{}</code>\n
<b>🖥 Ver:</b> <code>{}</code>\n
<b>🔗 Compartir:</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>¡Tu enlace!</u></i>\n
<b>📂 Archivo:</b> <b>{}</b>\n
<b>📦 Tamaño:</b> <code>{}</code>\n
<b>📥 Descargar:</b> <code>{}</code>\n
<b>🔗 Compartir:</b> <code>{}</code>\n"""

    BAN_TEXT = "__Lo siento, estás baneado para usar este bot.__\n\n**[Contacta al desarrollador](tg://user?id={}) para ayuda**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
