from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.bdrl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Bdrl`")
    sleep(3)
    await typew.edit("`20 Tahun`")
    sleep(3)
    await typew.edit("`JOMBLO`")
    sleep(1)
    await typew.edit("`Tinggal Di Jawa, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.trio(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai saya trio kontol `")
    sleep(5)
    await typew.edit("`perkenalkan saya @TripleNineee Bawok, lanjut.`")
    sleep(3)
    await typew.edit("`saya @SangDappaa memek`")
    sleep(3)
    await typew.edit("`Dan saya @Bdrlllll Jembut`")
    sleep(1)
    await typew.edit("`Kami bertiga tolol dan donggo π₯΅`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "πΎπ€π’π’ππ£π: `bdrl`\
    \nβ³ : perkenalan Bdrl\
    \n\nπΎπ€π’π’ππ£π: `.sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `.semangat`\
    \nβ³ : Jan Lupa Semangat."
})
