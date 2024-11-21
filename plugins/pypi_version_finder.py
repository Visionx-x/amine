import requests
from pyrogram import Client, filters
from pyrogram.types import Message

def version(package_name):
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            latest_version = data["info"]["version"]
            return package_name, latest_version
    except Exception as e:
            print(e)

@Client.on_message(filters.command("pypi") & filters.private)
async def pypi_package(client:Client, message:Message):
    msg = message.text.split()[1::]
    msge = "".join(msg)
    pckage_name, latest_version = version(msge)
    await message.reply_text(f"{pckage_name} version: {latest_version}")
