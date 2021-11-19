import os
from pyrogram import Client, filters
import rapidjson as json
import requests
import time

@app.on_message(filters.command("smug", PREFIX))
def smug(_, message):
    smug = requests.get("https://nekos.life/api/v2/img/smug").json()
    smug = url.get("smug")
    message.reply_video(smug)

@app.on_message(filters.command("solog", PREFIX))
def solog(_, message):
    solog = requests.get("https://nekos.life/api/v2/img/solog").json()
    solog = url.get("solog")
    message.reply_video(solog)

@app.on_message(filters.command("neko", PREFIX))
def neko(_, message):
    neko = requests.get("https://nekos.life/api/v2/img/neko").json()
    neko = url.get("neko")
    message.reply_photo(neko)

@app.on_message(filters.command("feet", PREFIX))
def feet(_, message):
    feet = requests.get("https://nekos.life/api/v2/img/feet").json()
    feet = url.get("feet")
    message.reply_photo(feet)


@app.on_message(filters.command("yuri", PREFIX))
def yuri(_, message):
    yuri = requests.get("https://nekos.life/api/v2/img/yuri").json()
    yuri = url.get("yuri")
    message.reply_photo(yuri)

@app.on_message(filters.command("trap", PREFIX))
def trap(_, message):
    trap = requests.get("https://nekos.life/api/v2/img/trap").json()
    trap = url.get("trap")
    message.reply_photo(trap)

@app.on_message(filters.command("futanari", PREFIX))
def futanari(_, message):
    futanari = requests.get("https://nekos.life/api/v2/img/futanari").json()
    futanari = url.get("futanari")
    message.reply_photo(futanari)

@app.on_message(filters.command("hololewd", PREFIX))
def hololewd(_, message):
    hololewd = requests.get("https://nekos.life/api/v2/img/hololewd").json()
    hololewd = url.get("hololewd")
    message.reply_photo(hololewd)

@app.on_message(filters.command("lewdkemo", PREFIX))
def lewdkemo(_, message):
    lewdkemo = requests.get("https://nekos.life/api/v2/img/lewdkemo").json()
    lewdkemo = url.get("lewdkemo")
    message.reply_photo(lewdkemo)

@app.on_message(filters.command("sologif", PREFIX))
def solog(_, message):
    solog = requests.get("https://nekos.life/api/v2/img/solog").json()
    solog = url.get("solog")
    message.reply_video(solog)

@app.on_message(filters.command("feetgif", PREFIX))
def feetg(_, message):
    feetg = requests.get("https://nekos.life/api/v2/img/feetg").json()
    feetg = url.get("feetg")
    message.reply_video(feetg)

@app.on_message(filters.command("cumgif", PREFIX))
def cum(_, message):
    cum = requests.get("https://nekos.life/api/v2/img/cum").json()
    cum = url.get("cum")
    message.reply_video(cum)

@app.on_message(filters.command("erokemo", PREFIX))
def erokemo(_, message):
    erokemo = requests.get("https://nekos.life/api/v2/img/erokemo").json()
    erokemo = url.get("erokemo")
    message.reply_photo(erokemo)

@app.on_message(filters.command("les", PREFIX))
def les(_, message):
    les = requests.get("https://nekos.life/api/v2/img/les").json()
    les = url.get("les")
    message.reply_video(les)

@app.on_message(filters.command("wallpaper", PREFIX))
def wallpaper(_, message):
    wallpaper = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
    wallpaper = url.get("wallpaper")
    message.reply_photo(wallpaper)

@app.on_message(filters.command("lewdk", PREFIX))
def lewdk(_, message):
    lewdk = requests.get("https://nekos.life/api/v2/img/lewdk").json()
    lewdk = url.get("lewdk")
    message.reply_photo(lewdk)

@app.on_message(filters.command("ngif", PREFIX))
def ngif(_, message):
    ngif = requests.get("https://nekos.life/api/v2/img/ngif").json()
    ngif = url.get("ngif")
    message.reply_video(ngif)

@app.on_message(filters.command("tickle", PREFIX))
def tickle(_, message):
    tickle = requests.get("https://nekos.life/api/v2/img/tickle").json()
    tickle = url.get("tickle")
    message.reply_video(tickle)

@app.on_message(filters.command("lewd", PREFIX))
def lewd(_, message):
    lewd = requests.get("https://nekos.life/api/v2/img/lewd").json()
    lewd = url.get("lewd")
    message.reply_photo(lewd)

@app.on_message(filters.command("feed", PREFIX))
def feed(_, message):
    feed = requests.get("https://nekos.life/api/v2/img/feed").json()
    feed = url.get("feed")
    message.reply_video(feed)

@app.on_message(filters.command("eroyuri", PREFIX))
def eroyuri(_, message):
    eroyuri = requests.get("https://nekos.life/api/v2/img/eroyuri").json()
    eroyuri = url.get("eroyuri")
    message.reply_photo(eroyuri)

@app.on_message(filters.command("eron", PREFIX))
def eron(_, message):
    eron = requests.get("https://nekos.life/api/v2/img/eron").json()
    eron = url.get("eron")
    message.reply_photo(eron)

@app.on_message(filters.command("cum", PREFIX))
def cumjpg(_, message):
    cum_jpg = requests.get("https://nekos.life/api/v2/img/cum_jpg").json()
    cum_jpg = url.get("cum_jpg")
    message.reply_photo(cum_jpg)

@app.on_message(filters.command("bjgif", PREFIX))
def bj(_, message):
    bj = requests.get("https://nekos.life/api/v2/img/bj").json()
    bj = url.get("bj")
    message.reply_video(bj)

@app.on_message(filters.command("blowjob", PREFIX))
def blowjob(_, message):
    blowjob = requests.get("https://nekos.life/api/v2/img/blowjob").json()
    blowjob = url.get("blowjob")
    message.reply_photo(blowjob)

@app.on_message(filters.command("nekogif", PREFIX))
def nekogif(_, message):
    nsfw_neko_gif = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()
    nsfw_neko_gif = url.get("nsfw_neko_gif")
    message.reply_video(nsfw_neko_gif)
