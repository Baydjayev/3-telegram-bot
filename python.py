import asyncio

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from tugmalar import *

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


# 1-Handler
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"sizga qanday yordam bera olaman", 
    reply_markup=menyu
)


# Callback uchun Handler
@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.message.edit_text("brendlardan birini tanlang: ", reply_markup=brendlar)

@dp.callback_query(F.data == 'apple')
async def applede(callback: CallbackQuery):
    await callback.message.edit_text("Apple telefonlaridan birini tanlang", reply_markup=iphone1)


@dp.callback_query(F.data == 'orqaga2')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text(f"sizga qanday yordam bera olaman", 
    reply_markup=menyu
)


@dp.callback_query(F.data == 'samsung')
async def samsungde(callback: CallbackQuery):
    await callback.message.edit_text("Samsung telefonlaridan birini tanlang", reply_markup=samsung2)


@dp.callback_query(F.data == 'xiaomi')
async def xiaomide(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi telefonlaridan birini tanlang", reply_markup=xiaomi3)


@dp.callback_query(F.data == 'huawei')
async def huaweide(callback: CallbackQuery):
    await callback.message.edit_text("Huawei telefonlaridan birini tanlang", reply_markup=huawei4)


@dp.callback_query(F.data == 'oppo')
async def oppode(callback: CallbackQuery):
    await callback.message.edit_text("OPPO telefonlaridan birini tanlang", reply_markup=oppo5)


@dp.callback_query(F.data == 'vivo')
async def vivode(callback: CallbackQuery):
    await callback.message.edit_text("Vivo telefonlaridan birini tanlang", reply_markup=vivo6)


@dp.callback_query(F.data == 'realme')
async def realmede(callback: CallbackQuery):
    await callback.message.edit_text("Realme telefonlaridan birini tanlang", reply_markup=realme7)


@dp.callback_query(F.data == 'onePlus')
async def onePlusde(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus telefonlaridan birini tanlang", reply_markup=oneplus8)


@dp.callback_query(F.data == 'honor')
async def honorde(callback: CallbackQuery):
    await callback.message.edit_text("Honor telefonlaridan birini tanlang", reply_markup=honor9)


@dp.callback_query(F.data == 'google')
async def googlede(callback: CallbackQuery):
    await callback.message.edit_text("Google (Pixel) telefonlaridan birini tanlang", reply_markup=google_pixel10)


@dp.callback_query(F.data == 'help')
async def boshsahifa(callback: CallbackQuery):
    await callback.message.edit_text("sizga qanday yordam kerak yoki botdan shikoyatingiz bormi etirozingiz yoki bot haqida gaplaringiz bolsa admingga murojat qiling", reply_markup=heplorqaga)


@dp.callback_query(F.data == 'orqaga')
async def orqagaback(callback: CallbackQuery):
    await callback.message.edit_text("brendlardan birini tanlang: ", reply_markup=brendlar)


@dp.callback_query(F.data == 'ip15pmax')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 15 Pro Max Apple’ning eng kuchli flagmani. Titan korpus, A17 Pro chipi, 5x telefoto kamera va eng ilg‘or iOS tajribasini taklif etadi. Katta ekran va kuchli batareya uni premium foydalanuvchilar uchun mukammal tanlovga aylantiradi.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip15pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 15 Pro Titan korpus, A17 Pro protsessor va Dynamic Island bilan jihozlangan. Kamera sifati yuqori darajada, ProRAW va ProRes formatlarini qo‘llaydi. Dizayn ixchamroq, lekin flagman imkoniyatlarini to‘liq beradi.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip15plus')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 15 Plus Katta 6.7 dyuymli ekran, uzoq batareya muddati va yaxshi kamera tizimiga ega. A16 Bionic chipida ishlaydi. Narxi Pro versiyalardan arzonroq, lekin kattaroq ekranli telefon izlaydiganlar uchun yaxshi variant.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip15')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 15 Eng yangi avlodning asosiy modeli. Dynamic Island dizayni, A16 Bionic chipi va yaxshi kamera imkoniyatlariga ega. Narx va imkoniyatlar o‘rtasida muvozanat izlaydiganlar uchun eng maqbul tanlov.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip14pmax')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 14 Pro Max ProMotion displey va Dynamic Island bilan jihozlangan avvalgi flagman. 48MP asosiy kamera va kuchli A16 chipi bilan mashhur. Hozir ham ko‘plab foydalanuvchilar orasida ommabop.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip14pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 14 Pro Ixchamroq flagman modeli. 48MP asosiy kamera, ProMotion ekran va Dynamic Island imkoniyatlariga ega. Hali ham kuchli ishlash qobiliyati bilan talab katta.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip14plus')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 14 Plus 6.7 dyuymli katta ekran, yaxshi batareya ishlash muddati va barqaror ishlash imkoniyatlarini taklif etadi. A15 Bionic chipi bilan ishlaydi. Narxi maqbulroq bo‘lgan katta ekranli iPhone.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip14')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 14 Klassik iPhone dizayni va barqaror ishlash imkoniyatlari. A15 Bionic chipi, yaxshi kamera va uzoq muddatli dasturiy yangilanish qo‘llab-quvvatlashi bilan mashhur. O‘rtacha byudjet uchun mos.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ipse')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone SE (2022) Arzonroq iPhone varianti. Klassik Home tugmachasi, A15 chipi va iOS imkoniyatlari bilan jihozlangan. Ixcham dizayn va kuchli protsessorni arzon narxda izlaydiganlar uchun mos.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'ip13')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("iPhone 13 Hali ham mashhur va ommaviy telefon. Kuchli ishlash, yaxshi kamera va uzoq batareya muddati bilan ajralib turadi. Narxi yangi modellarga nisbatan pastroq, shuning uchun ko‘plab xaridorlar uni tanlashadi.", reply_markup=appleorqaga)


@dp.callback_query(F.data == 'gls24ul')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy S24 Ultra Samsung’ning eng yangi flagmani. Snapdragon 8 Gen 3 chipi, 200MP asosiy kamera va S Pen bilan jihozlangan. Qalin titan korpus va yuqori sifatli Dynamic AMOLED 2X displey bilan premium tajriba beradi.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'gls24pl')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy S24+ 6.7 dyuymli Dynamic AMOLED displey, kuchli Snapdragon chipi va yaxshi kamera tizimiga ega. Ultra’dan ixchamroq, ammo yuqori darajadagi imkoniyatlarni taqdim etadi.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'gls24')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy S24 Asosiy flagman modeli. Ixcham dizayn, kuchli ishlash va sifatli kamera tizimi bilan ajralib turadi. Narx jihatidan biroz arzonroq, lekin flagman tajribasini beradi.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'glzfd5')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy Z Fold5 Bukiluvchi telefon. 7.6 dyuymli ichki ekran va 6.2 dyuymli tashqi ekran bilan jihozlangan. Multitasking va yuqori samaradorlik uchun mos, premium segmentdagi innovatsion qurilma.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'glzfp5')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy Z Flip5 Kompakt bukiluvchi dizayn. Katta tashqi displey va kuchli ichki ekran bilan ajralib turadi. Selfie va vlog olish uchun juda qulay. Yoshlar orasida mashhur.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'gls23ul')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy S23 Ultra 200MP kamera va S Pen bilan mashhur flagman. Snapdragon 8 Gen 2 chipi va kuchli AMOLED ekrani bilan yuqori samaradorlikni taqdim etadi. 2023 yilning eng mashhur Android telefoni.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'gla545g')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy A54 5G O‘rta segmentdagi mashhur model. 120Hz AMOLED displey, kuchli kamera tizimi va katta batareya bilan ta’minlangan. Narx va sifat jihatidan juda yaxshi balansga ega.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'gla345g')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy A34 5G Yaxshi ishlash, barqaror dizayn va sifatli kamera bilan arzonroq variant. Kundalik foydalanish uchun ishonchli smartfon sifatida ko‘plab xaridorlarga yoqadi.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'glm145g')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy M14 5G Hamyonbop, ammo kuchli batareya (6000mAh) bilan mashhur. Uzoq ishlash muddati va barqaror ishlash qobiliyati tufayli byudjet segmentida juda talabgir.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'gls21fe')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Galaxy S21 FE S-seriya imkoniyatlarini arzonroq narxda taklif qiladi. Yaxshi kamera, kuchli protsessor va AMOLED ekran bilan jihozlangan. Hali ham ko‘plab foydalanuvchilar orasida mashhur.", reply_markup=samsungorqaga)


@dp.callback_query(F.data == 'xi14ul')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi 14 Ultra Flagman darajasidagi model. Leica kamerasi, Snapdragon 8 Gen 3 chipi va kuchli AMOLED displey bilan jihozlangan. Premium dizayn va yuqori ishlash qobiliyati uni fotografiya va kuchli smartfon izlovchilar uchun ideal qiladi.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'xi14pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi 14 Pro Kuchli Snapdragon chipi va 120Hz AMOLED ekranga ega. Leica bilan hamkorlikdagi kamerasi professional suratga olish imkoniyatini beradi. Flagman darajasidagi ishlashni ixchamroq dizayn bilan taklif etadi.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'xi14')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi 14 Arzonroq, lekin flagman darajasidagi ishlash imkoniyatlarini beradi. Kuchli chip, sifatli ekran va yaxshi kameraga ega. Narx va imkoniyatlar jihatidan muvozanatli tanlov.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'xi13ul')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi 13 Ultra Leica bilan ishlangan kamera tizimi tufayli fotografiya ixlosmandlari uchun eng yaxshi variantlardan biri. Kuchli ishlash va premium dizayn bilan mashhur. Xiaomi brendining eng ilg‘or modellari qatoriga kiradi.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'xi13pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi 13 Pro Snapdragon 8 Gen 2 chipi va Leica kamerasi bilan mashhur. Kuchli displey va tezkor zaryadlash funksiyasi bilan foydalanuvchilar orasida yuqori bahoga ega.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'xi13')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi 13 Ixchamroq flagman modeli. Kuchli ishlash, yaxshi kamera va sifatli dizayn bilan ta’minlangan. Narxi Pro va Ultra modellarga qaraganda pastroq.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'reno13prop')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Redmi Note 13 Pro+ O‘rta segmentdagi mashhur model. 200MP kamera, tezkor zaryadlash va kuchli AMOLED displey bilan jihozlangan. Byudjet va flagman imkoniyatlarini uyg‘unlashtiradi.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'reno13pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Redmi Note 13 Pro Narxi maqbul, lekin kuchli ishlash imkoniyatlari va yaxshi kamera tizimiga ega. O‘rta segment xaridorlari orasida mashhur.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'reno13')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Redmi Note 13 Arzonroq variant. Kundalik foydalanish uchun qulay, yaxshi kamera va katta batareyaga ega. Oddiy foydalanuvchilar uchun mos.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'pof5pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Poco F5 Pro Poco liniyasining mashhur flagmani. Kuchli Snapdragon chipi, yaxshi kamera va yuqori yangilanish chastotali ekran bilan jihozlangan. Narxi hamyonbop, ammo ishlashi yuqori.", reply_markup=xiaomiorqaga)


@dp.callback_query(F.data == 'hup60pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei P60 Pro Flagman darajasidagi kamera tizimi va kuchli ishlash bilan mashhur. Portret va tungi suratlarda yuqori sifat beradi. Premium dizayn va kuchli batareya bilan Huawei’ning eng ilg‘or modellari qatorida turadi.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'hup60')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei P60 P60 Pro’dan biroz ixchamroq va arzonroq, lekin yuqori sifatli kamera va kuchli ishlash imkoniyatlariga ega. Kundalik foydalanish uchun qulay va premium tajribani taqdim etadi.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'huma60prop')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Mate 60 Pro+ Eng yuqori darajadagi flagman. Kuchli chip, katta ekran va ilg‘or kamera tizimi bilan jihozlangan. Innovatsion dizayn va premium funksiyalarni birlashtiradi.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'huma60pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Mate 60 Pro Pro+’dan biroz pastroq, lekin flagman darajasida ishlash qobiliyatiga ega. Katta AMOLED displey, kuchli kamera va premium dizayni bilan mashhur.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'huma60')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Mate 60 Asosiy Mate 60 modeli. Kuchli ishlash, yaxshi kamera va uzoq batareya muddati bilan o‘rta-flagman segmentida yaxshi tanlov hisoblanadi.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'huno11pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Nova 11 Pro Yosh foydalanuvchilar uchun mo‘ljallangan dizayn va kuchli kamera imkoniyatlari bilan mashhur. Tezkor zaryadlash va AMOLED displey bilan jihozlangan.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'huno11')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Nova 11 Ixchamroq, lekin kuchli ishlash qobiliyatiga ega model. Narxi Pro versiyaga nisbatan arzonroq. Kundalik foydalanishda tezkor va ishonchli.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'huno10pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Nova 10 Pro O‘rta segmentda mashhur bo‘lgan model. Kuchli selfie kamera va dizayn bilan ajralib turadi. Yoshlar orasida mashhur bo‘lib qolgan.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'hunoy90')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei Nova Y90 Hamyonbop segment uchun mo‘ljallangan model. Katta ekran, yaxshi batareya va kundalik foydalanishga mos ishlash imkoniyatlariga ega.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'hup50po')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei P50 Pocket Bukiluvchi dizaynga ega premium model. Ixcham va chiroyli dizayn bilan birga kuchli kamera va yaxshi ishlash imkoniyatlarini beradi. Innovatsion qurilma sifatida Huawei’ning premium segmentida turadi.", reply_markup=huaweiorqaga)


@dp.callback_query(F.data == 'opfix7ul')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Find X7 Ultra OPPO’ning flagman modeli. Hasselblad bilan hamkorlikda ishlab chiqilgan ilg‘or kameralar, Snapdragon chipi va premium dizayni bilan mashhur. Fotografiya va yuqori ishlashni izlovchilar uchun mukammal tanlov.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opfix7')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Find X7 Find X7 Ultra’dan arzonroq, ammo flagman imkoniyatlarini taklif etadi. Kuchli displey, yaxshi kamera va tezkor zaryadlash funksiyasi bilan o‘rta-flagman segmentida mashhur.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opfin3fp')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Find N3 Flip Bukiluvchi kompakt telefon. Katta tashqi ekran va yaxshi kamera tizimi bilan ajralib turadi. Ixcham dizaynni yoqtiradigan foydalanuvchilar uchun mos variant.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opfin3')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Find N3 Katta ekranli bukiluvchi flagman. Multitasking va yuqori samaradorlikni taqdim etadi. Innovatsion dizayni bilan OPPO’ning premium segmentdagi yetakchi modeli hisoblanadi.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opre10prop')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Reno 10 Pro+ Reno seriyasining flagman modeli. Kuchli kamera, yaxshi ishlash va tezkor zaryadlash imkoniyatlari bilan mashhur. Narx va imkoniyatlar jihatidan juda muvozanatli.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opre10pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Reno 10 Pro Pro+’dan biroz arzonroq, ammo yuqori sifatli kamera va kuchli ishlash imkoniyatlariga ega. O‘rta segment foydalanuvchilari uchun juda yaxshi tanlov.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opre10')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO Reno 10 Narxi yanada arzonroq bo‘lsa-da, yaxshi kamera va barqaror ishlash imkoniyatlarini taqdim etadi. Dizayni chiroyli va kundalik foydalanishga mos.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opa985g')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO A98 5G O‘rta segmentdagi mashhur model. Katta batareya, tezkor zaryadlash va sifatli ekran bilan jihozlangan. Narxi hamyonbop, lekin ishlashi yuqori.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opa78')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO A78 Hamyonbop segment uchun ishlab chiqarilgan. Yaxshi ishlash, katta batareya va oddiy dizayni bilan ko‘plab foydalanuvchilarni jalb qiladi.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'opa58')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO A58 Eng arzon OPPO modellardan biri. Kundalik foydalanish uchun yetarli imkoniyatlarga ega. Katta ekran va uzoq batareya muddati bilan mashhur.", reply_markup=oppoorqaga)


@dp.callback_query(F.data == 'vix100pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo X100 Pro Flagman darajasidagi kamera va ishlash imkoniyatlari bilan mashhur. OIS stabilizatsiyali kamera, AMOLED displey va yuqori samaradorlikka ega chip bilan jihozlangan. Fotografiya ixlosmandlari uchun mukammal tanlov.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'vix100')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo X100 X100 Pro’dan biroz arzonroq, lekin kuchli ishlash imkoniyatlari va yuqori sifatli displeyga ega. Tezkor zaryadlash va kuchli kamera tizimi bilan kundalik foydalanishga juda mos.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'vix90prop')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo X90 Pro+ Eng ilg‘or flagman modellardan biri. Snapdragon chipi, ZEISS bilan hamkorlikda ishlab chiqilgan kamera tizimi va premium dizayni bilan mashhur. Mobil fotografiyada yetakchi hisoblanadi.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'vix90pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo X90 Pro Pro+’dan arzonroq, ammo o‘rta-flagman segmentida juda kuchli imkoniyatlarni taqdim etadi. Kamera sifati va kuchli ishlash bilan foydalanuvchilarni jalb qiladi.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'viv29pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo V29 Pro O‘rta segmentga mo‘ljallangan. Kuchli kamera, AMOLED displey va chiroyli dizayni bilan mashhur. Narx va sifat jihatidan muvozanatli tanlov.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'viv29')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo V29 Pro versiyasidan arzonroq, ammo yaxshi kamera va uzoq batareya muddati bilan ajralib turadi. Yosh foydalanuvchilar orasida mashhur model.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'viv27pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo V27 Pro Kamera imkoniyatlari va dizayni bilan mashhur. Selfie va tungi suratlarda yuqori sifat beradi. O‘rta-flagman segmentda raqobatbardosh.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'viv27')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo V27 Pro versiyasidan oddiyroq, lekin hamyonbop narxda yaxshi ishlash va kamera imkoniyatlarini taqdim etadi. Katta ekran va tezkor zaryadlash mavjud.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'viy100')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo Y100 O‘rta segment uchun mo‘ljallangan hamyonbop model. Kuchli ishlash, rangli dizayn va tezkor zaryadlash funksiyasi bilan ajralib turadi.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'viy78')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo Y78 Hamyonbop segmentdagi model. Katta ekran, yaxshi kamera va uzoq batareya muddati bilan kundalik foydalanish uchun qulay.", reply_markup=vivoorqaga)


@dp.callback_query(F.data == 'regt5pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme GT 5 Pro Realme’ning eng kuchli flagman modeli. Snapdragon chipi, ilg‘or kamera va tezkor zaryadlash imkoniyatlari bilan mashhur. Premium dizayni va yuqori ishlash samaradorligi bilan ajralib turadi.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 'regt5')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme GT 5 Pro versiyasidan biroz arzonroq, ammo flagman darajasida ishlash va kuchli displeyga ega. O‘yin va kundalik foydalanish uchun juda qulay.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 're12prop')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme 12 Pro+ O‘rta-flagman segmentidagi mashhur model. Kuchli kamera tizimi va AMOLED displey bilan jihozlangan. Narxi va imkoniyatlari muvozanatli.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 're12pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme 12 Pro Pro+’dan arzonroq, ammo yaxshi ishlash va sifatli kamera bilan mashhur. O‘rta segment foydalanuvchilari uchun mos variant.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 're11prop')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme 11 Pro+ Kamerasi bilan ajralib turadigan model. Tezkor zaryadlash, yuqori sifatli displey va samaradorligi bilan mashhur. Fotografiya uchun yaxshi tanlov.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 're11pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme 11 Pro Pro+’dan arzonroq, lekin yaxshi ishlash va qulay narx bilan mashhur. Kundalik foydalanishga mos va yoshlar orasida keng tarqalgan.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 're11')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme 11 O‘rta segmentdagi oddiyroq model. Katta ekran, uzoq batareya muddati va hamyonbop narxi bilan e’tiborga loyiq.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 'rena60pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme Narzo 60 Pro Narzo seriyasining flagman modeli. Kuchli ishlash, yaxshi kamera va tezkor zaryadlash imkoniyatlari bilan mashhur. O‘yin ixlosmandlari uchun ham mos.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 'rena60')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme Narzo 60 Pro versiyasidan arzonroq, ammo yaxshi ishlash va zamonaviy dizayni bilan mashhur. Kundalik foydalanishga juda mos.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 'rec55')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme C55 Eng hamyonbop modellardan biri. Oddiy ishlash, katta ekran va kuchli batareyaga ega. Narxi qulay bo‘lgani uchun keng omma uchun mos.", reply_markup=realmeorqaga)


@dp.callback_query(F.data == 'onp12')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus 12 OnePlus’ning eng yangi flagman modeli. Snapdragon chipi, ilg‘or kamera va AMOLED displey bilan jihozlangan. Kuchli ishlash samaradorligi va premium dizayni bilan mashhur.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onp11')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus 11 Flagman darajasidagi model, lekin biroz arzonroq. Kuchli ishlash, yuqori sifatli kamera va uzoq batareya muddati bilan ajralib turadi.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onp10pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus 10 Pro Katta ekran, kuchli kamera va tezkor zaryadlash funksiyasi bilan mashhur. Fotografiya va o‘yin ixlosmandlari uchun yaxshi tanlov.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onp10t')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus 10T 10 Pro’dan biroz arzonroq, ammo tezkor ishlash va katta ekran imkoniyatlari bilan mashhur. Hamyonbop flagman sifatida qadrlanadi.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onpno3')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus Nord 3 O‘rta segment flagmani. Yaxshi ishlash, sifatli displey va samarali kamera tizimiga ega. Narxi ham o‘rtacha.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onpnoce3li')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus Nord CE 3 Lite Hamyonbop model. Oddiy ishlash, katta ekran va qulay narx bilan mashhur. Yosh foydalanuvchilar uchun mos.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onpno2t')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus Nord 2T O‘rta segmentdagi mashhur model. Tezkor zaryadlash, yaxshi kamera va o‘yinlar uchun yetarli samaradorlikka ega.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onp9pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus 9 Pro Oldingi flagman model. Kuchli kamera tizimi va yuqori sifatli displey bilan mashhur. Hozir ham o‘z ahamiyatini yo‘qotmagan.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onp9')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus 9, Pro versiyasidan arzonroq, ammo yaxshi ishlash va kamera imkoniyatlari bilan ajralib turadi. Kundalik foydalanishga qulay.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'onpace2')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus Ace 2 O‘rta-flagman segmentida. Kuchli ishlash, yaxshi kamera va tezkor zaryadlash funksiyasi bilan mashhur. Dizayni ham zamonaviy.", reply_markup=oneplusorqaga)


@dp.callback_query(F.data == 'homav2')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor Magic V2 Honor’ning katlanadigan flagman telefoni. Ultra yupqa dizayni, ilg‘or Snapdragon chipi va kuchli kamera tizimi bilan mashhur. Premium segmentga kiradi.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'homavs')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor Magic Vs Magic V2’dan avvalgi katlanadigan model. Katta displey, kuchli ishlash va yuqori sifatli kameralar bilan jihozlangan. Innovatsion dizayni bilan ajralib turadi.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'homa5pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor Magic 5 Pro Flagman darajasidagi model. Kuchli kamera, yuqori sifatli AMOLED displey va tezkor ishlash imkoniyatlari bilan mashhur. Fotografiya ixlosmandlari uchun mos.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'homa5')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor Magic 5 Pro versiyasidan arzonroq, ammo yaxshi ishlash samaradorligi va sifatli kamera tizimiga ega. Premium ko‘rinishga ega.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'homa4pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor Magic 4 Pro Oldingi flagman seriyadan. Kuchli kamera, yaxshi ishlash va premium dizayni bilan mashhur. Hali ham keng qo‘llaniladi.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'homa4')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor Magic 4, Pro versiyasidan arzonroq. Yuqori samarali chip va zamonaviy dizaynga ega. Kundalik foydalanishda qulay.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'ho90pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor 90 Pro Yangi o‘rta-flagman modeli. Kuchli kamera, yaxshi ishlash va tezkor zaryadlash imkoniyatlari bilan mashhur. Yoshlar orasida ommalashgan.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'ho90')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor 90, Pro versiyasidan arzonroq, ammo yaxshi kamera va kuchli batareyaga ega. Narx va sifat muvozanati yaxshi.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'ho70pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor 70 Pro O‘rta-flagman segmenti. Sifatli kamera tizimi, AMOLED displey va tezkor zaryadlash imkoniyatlari bilan mashhur. Fotografiya uchun qulay.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'ho70')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor 70, Pro versiyasidan arzonroq. Oddiyroq kamera tizimi va kuchli ishlash samaradorligi bilan ajralib turadi. Hamyonbop tanlov.", reply_markup=honororqaga)


@dp.callback_query(F.data == 'gopi8pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 8 Pro Google’ning eng yangi flagmani. Tensor G3 chipi, ilg‘or sun’iy intellekt imkoniyatlari va yuqori darajadagi kamera tizimi bilan mashhur. Premium segmentda.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi8')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 8 Pro versiyasidan arzonroq. Kuchli ishlash, yaxshi kamera va toza Android tajribasi bilan mashhur. Narx va sifat muvozanati yaxshi.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi7pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 7 Pro Oldingi flagman modeli. Kuchli Tensor chipi, ilg‘or kamera imkoniyatlari va katta AMOLED displey bilan jihozlangan. Fotografiya ixlosmandlari uchun mos.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi7')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 7, Pro versiyasidan arzonroq, ammo Tensor chipi va yuqori sifatli kamera tizimi bilan mashhur. Kundalik foydalanishda ideal.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi7a')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 7a O‘rta segment flagmani. Tensor chipi, yaxshi kamera va qulay narxi bilan mashhur. Google’ning hamyonbop telefoni sifatida qadrlanadi.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi6pro')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 6 Pro Kuchli kamera tizimi va Tensor chipining birinchi avlodidan foydalanilgan. Premium ko‘rinishi va yuqori samaradorligi bilan mashhur.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi6')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 6, Pro versiyasidan arzonroq, ammo Tensor chipi va sifatli kamera bilan jihozlangan. Toza Android tajribasi taqdim etadi.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi6a')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 6a Hamyonbop Pixel modeli. Tensor chipi va yaxshi kameraga ega, lekin narxi o‘rtacha. Yoshlar orasida keng tarqalgan.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopifold')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel Fold Google’ning birinchi katlanadigan telefoni. Katta displey, kuchli chip va ilg‘or kamera tizimi bilan mashhur. Innovatsion dizaynni afzal ko‘ruvchilar uchun mos.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'gopi5a')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google Pixel 5a Avvalgi avlod o‘rta segment modeli. Tezkor ishlash, yaxshi kamera va qulay narx bilan mashhur. Kundalik foydalanishda ideal.", reply_markup=googleorqaga)


@dp.callback_query(F.data == 'appleorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Apple telefonlaridan birini tanlang", reply_markup=iphone1)


@dp.callback_query(F.data == 'samsungorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Samsung telefonlaridan birini tanlang", reply_markup=samsung2)


@dp.callback_query(F.data == 'xiaomiorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Xiaomi telefonlaridan birini tanlang", reply_markup=xiaomi3)


@dp.callback_query(F.data == 'huaweiorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Huawei telefonlaridan birini tanlang", reply_markup=huawei4)


@dp.callback_query(F.data == 'oppoorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OPPO telefonlaridan birini tanlang", reply_markup=oppo5)


@dp.callback_query(F.data == 'vivoorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Vivo telefonlaridan birini tanlang", reply_markup=vivo6)


@dp.callback_query(F.data == 'realmeorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Realme telefonlaridan birini tanlang", reply_markup=realme7)


@dp.callback_query(F.data == 'oneplusorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("OnePlus telefonlaridan birini tanlang", reply_markup=oneplus8)


@dp.callback_query(F.data == 'honororq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Honor telefonlaridan birini tanlang", reply_markup=honor9)


@dp.callback_query(F.data == 'googleorq')
async def orqaga(callback: CallbackQuery):
    await callback.message.edit_text("Google (Pixel) telefonlaridan birini tanlang", reply_markup=google_pixel10)













































async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to'xtadi!")

# Error code

# @AiogramUchunBot
