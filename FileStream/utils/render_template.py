#utils/render_template.py

import aiohttp
import jinja2
import urllib.parse
import base64
from FileStream.config import Telegram, Server
from FileStream.utils.database import Database
from FileStream.utils.human_readable import humanbytes

db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

async def render_page(db_id):
    file_data = await db.get_file(db_id)
    
    # Codifica la URL de descarga en base64
    download_url = urllib.parse.urljoin(Server.URL, f'dl/{file_data["_id"]}')
    encoded_url = base64.b64encode(download_url.encode()).decode()

    # Construye la URL final
    src = f"{Server.URL}?url={encoded_url}"
    
    file_size = humanbytes(file_data['file_size'])
    file_name = file_data['file_name'].replace("_", " ")

    if str((file_data['mime_type']).split('/')[0].strip()) == 'video':
        template_file = "FileStream/template/play.html"
    else:
        template_file = "FileStream/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = humanbytes(int(u.headers.get('Content-Length')))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size
    )