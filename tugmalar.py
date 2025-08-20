from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

menyu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='brendlar', callback_data='catalog')
    ],

    [
        InlineKeyboardButton(text='Yordam', callback_data='help')
    ]
]
)


brendlar = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Apple", callback_data='apple'), 
            InlineKeyboardButton(text="Samsung", callback_data='samsung'),
            InlineKeyboardButton(text="Xiaomi", callback_data='xiaomi')
        ],    
        [
            
            InlineKeyboardButton(text="Huawei", callback_data='huawei'), 
            InlineKeyboardButton(text="OPPO", callback_data='oppo'),
            InlineKeyboardButton(text="Vivo", callback_data='vivo')
        ],
        [
            
            InlineKeyboardButton(text="Realme", callback_data='realme'), 
            InlineKeyboardButton(text="OnePlus", callback_data='onePlus'),
            InlineKeyboardButton(text="Honor", callback_data='honor'),
            InlineKeyboardButton(text='Google (Pixel)', callback_data='google')
        ],
        [
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

iphone1 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="iPhone 15 Pro Max", callback_data='ip15pmax'), 
            InlineKeyboardButton(text="iPhone 15 Pro", callback_data='ip15pro'),
            InlineKeyboardButton(text="iPhone 15 Plus", callback_data='ip15plus')
        ],    
        [
            
            InlineKeyboardButton(text="iPhone 15", callback_data='ip15'), 
            InlineKeyboardButton(text="iPhone 14 Pro Max", callback_data='ip14pmax'),
            InlineKeyboardButton(text="iPhone 14 Pro", callback_data='ip14pro')
        ],
        [
            
            InlineKeyboardButton(text="iPhone 14 Plus", callback_data='ip14plus'), 
            InlineKeyboardButton(text="iPhone 14", callback_data='ip14'),
            InlineKeyboardButton(text="iPhone SE (2022)", callback_data='ipse'),
            InlineKeyboardButton(text='iPhone 13', callback_data='ip13')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

samsung2 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Galaxy S24 Ultra", callback_data='gls24ul'), 
            InlineKeyboardButton(text="Galaxy S24+", callback_data='gls24pl'),
            InlineKeyboardButton(text="Galaxy S24", callback_data='gls24')
        ],    
        [
            
            InlineKeyboardButton(text="Galaxy Z Fold5", callback_data='glzfd5'), 
            InlineKeyboardButton(text="Galaxy Z Flip5", callback_data='glzfp5'),
            InlineKeyboardButton(text="Galaxy S23 Ultra", callback_data='gls23ul')
        ],
        [
            
            InlineKeyboardButton(text="Galaxy A54 5G", callback_data='gla545g'), 
            InlineKeyboardButton(text="Galaxy A34 5G", callback_data='gla345g'),
            InlineKeyboardButton(text="Galaxy M14 5G", callback_data='glm145g'),
            InlineKeyboardButton(text='Galaxy S21 FE', callback_data='gls21fe')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

xiaomi3 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Xiaomi 14 Ultra", callback_data='xi14ul'), 
            InlineKeyboardButton(text="Xiaomi 14 Pro", callback_data='xi14pro'),
            InlineKeyboardButton(text="Xiaomi 14", callback_data='xi14')
        ],    
        [
            
            InlineKeyboardButton(text="Xiaomi 13 Ultra", callback_data='xi13ul'), 
            InlineKeyboardButton(text="Xiaomi 13 Pro", callback_data='xi13pro'),
            InlineKeyboardButton(text="Xiaomi 13", callback_data='xi13')
        ],
        [
            
            InlineKeyboardButton(text="Redmi Note 13 Pro+", callback_data='reno13prop'), 
            InlineKeyboardButton(text="Redmi Note 13 Pro", callback_data='reno13pro'),
            InlineKeyboardButton(text="Redmi Note 13", callback_data='reno13'),
            InlineKeyboardButton(text='Poco F5 Pro', callback_data='pof5pro')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

huawei4 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Huawei P60 Pro", callback_data='hup60pro'), 
            InlineKeyboardButton(text="Huawei P60", callback_data='hup60'),
            InlineKeyboardButton(text="Huawei Mate 60 Pro+", callback_data='huma60prop')
        ],    
        [
            
            InlineKeyboardButton(text="Huawei Mate 60 Pro", callback_data='huma60pro'), 
            InlineKeyboardButton(text="Huawei Mate 60", callback_data='huma60'),
            InlineKeyboardButton(text="Huawei Nova 11 Pro", callback_data='huno11pro')
        ],
        [
            
            InlineKeyboardButton(text="Huawei Nova 11", callback_data='huno11'), 
            InlineKeyboardButton(text="Huawei Nova 10 Pro", callback_data='huno10pro'),
            InlineKeyboardButton(text="Huawei Nova Y90", callback_data='hunoy90'),
            InlineKeyboardButton(text='Huawei P50 Pocket', callback_data='hup50po')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

oppo5 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="OPPO Find X7 Ultra", callback_data='opfix7ul'), 
            InlineKeyboardButton(text="OPPO Find X7", callback_data='opfix7'),
            InlineKeyboardButton(text="OPPO Find N3 Flip", callback_data='opfin3fp')
        ],    
        [
            
            InlineKeyboardButton(text="OPPO Find N3", callback_data='opfin3'), 
            InlineKeyboardButton(text="OPPO Reno 10 Pro+", callback_data='opre10prop'),
            InlineKeyboardButton(text="OPPO Reno 10 Pro", callback_data='opre10pro')
        ],
        [
            
            InlineKeyboardButton(text="OPPO Reno 10", callback_data='opre10'), 
            InlineKeyboardButton(text="OPPO A98 5G", callback_data='opa985g'),
            InlineKeyboardButton(text="OPPO A78", callback_data='opa78'),
            InlineKeyboardButton(text='OPPO A58', callback_data='opa58')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

vivo6 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Vivo X100 Pro", callback_data='vix100pro'), 
            InlineKeyboardButton(text="Vivo X100", callback_data='vix100'),
            InlineKeyboardButton(text="Vivo X90 Pro+", callback_data='vix90prop')
        ],    
        [
            
            InlineKeyboardButton(text="Vivo X90 Pro", callback_data='vix90pro'), 
            InlineKeyboardButton(text="Vivo V29 Pro", callback_data='viv29pro'),
            InlineKeyboardButton(text="Vivo V29", callback_data='viv29')
        ],
        [
            
            InlineKeyboardButton(text="Vivo V27 Pro", callback_data='viv27pro'), 
            InlineKeyboardButton(text="Vivo V27", callback_data='viv27'),
            InlineKeyboardButton(text="Vivo Y100", callback_data='viy100'),
            InlineKeyboardButton(text='Vivo Y78', callback_data='viy78')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

realme7 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Realme GT 5 Pro", callback_data='regt5pro'), 
            InlineKeyboardButton(text="Realme GT 5", callback_data='regt5'),
            InlineKeyboardButton(text="Realme 12 Pro+", callback_data='re12prop')
        ],    
        [
            
            InlineKeyboardButton(text="Realme 12 Pro", callback_data='re12pro'), 
            InlineKeyboardButton(text="Realme 11 Pro+", callback_data='re11prop'),
            InlineKeyboardButton(text="Realme 11 Pro", callback_data='re11pro')
        ],
        [
            
            InlineKeyboardButton(text="Realme 11", callback_data='re11'), 
            InlineKeyboardButton(text="Realme Narzo 60 Pro", callback_data='rena60pro'),
            InlineKeyboardButton(text="Realme Narzo 60", callback_data='rena60'),
            InlineKeyboardButton(text='Realme C55', callback_data='rec55')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

oneplus8 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="OnePlus 12", callback_data='onp12'), 
            InlineKeyboardButton(text="OnePlus 11", callback_data='onp11'),
            InlineKeyboardButton(text="OnePlus 10 Pro", callback_data='onp10pro')
        ],    
        [
            
            InlineKeyboardButton(text="OnePlus 10T", callback_data='onp10t'), 
            InlineKeyboardButton(text="OnePlus Nord 3", callback_data='onpno3'),
            InlineKeyboardButton(text="OnePlus Nord CE 3 Lite", callback_data='onpnoce3li')
        ],
        [
            
            InlineKeyboardButton(text="OnePlus Nord 2T", callback_data='onpno2t'), 
            InlineKeyboardButton(text="OnePlus 9 Pro", callback_data='onp9pro'),
            InlineKeyboardButton(text="OnePlus 9", callback_data='onp9'),
            InlineKeyboardButton(text='OnePlus Ace 2', callback_data='onpace2')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

honor9 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Honor Magic V2", callback_data='homav2'), 
            InlineKeyboardButton(text="Honor Magic Vs", callback_data='homavs'),
            InlineKeyboardButton(text="Honor Magic 5 Pro", callback_data='homa5pro')
        ],    
        [
            
            InlineKeyboardButton(text="Honor Magic 5", callback_data='homa5'), 
            InlineKeyboardButton(text="Honor Magic 4 Pro", callback_data='homa4pro'),
            InlineKeyboardButton(text="Honor Magic 4", callback_data='homa4')
        ],
        [
            
            InlineKeyboardButton(text="Honor 90 Pro", callback_data='ho90pro'), 
            InlineKeyboardButton(text="Honor 90", callback_data='ho90'),
            InlineKeyboardButton(text="Honor 70 Pro", callback_data='ho70pro'),
            InlineKeyboardButton(text='Honor 70', callback_data='ho70')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])

google_pixel10 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Google Pixel 8 Pro", callback_data='gopi8pro'), 
            InlineKeyboardButton(text="Google Pixel 8", callback_data='gopi8'),
            InlineKeyboardButton(text="Google Pixel 7 Pro", callback_data='gopi7pro')
        ],    
        [
            
            InlineKeyboardButton(text="Google Pixel 7", callback_data='gopi7'), 
            InlineKeyboardButton(text="Google Pixel 7a", callback_data='gopi7a'),
            InlineKeyboardButton(text="Google Pixel 6 Pro", callback_data='gopi6pro')
        ],
        [
            
            InlineKeyboardButton(text="Google Pixel 6", callback_data='gopi6'), 
            InlineKeyboardButton(text="Google Pixel 6a", callback_data='gopi6a'),
            InlineKeyboardButton(text="Google Pixel Fold", callback_data='gopifold'),
            InlineKeyboardButton(text='Google Pixel 5a', callback_data='gopi5a')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
            InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
        ]

])


appleorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='appleorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


samsungorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='sansungorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


xiaomiorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='xiaomiorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


huaweiorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='huaweiorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


oppoorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='oppoorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


vivoorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='vivoorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


realmeorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='realmeorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


oneplusorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='oneplusorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


honororqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='honororq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])


googleorqaga =InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='orqaga', callback_data='googleorq'),
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])

heplorqaga = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='bosh sahifa', callback_data='orqaga2')
    ]
])

# # Reply Keyboard
# reply_katalog = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(text="Anor")
#     ],
#     [
#         KeyboardButton(text="Olma"), 
#         KeyboardButton(text="Anjir")
#     ],
#     [
#         KeyboardButton(text="Banan"), 
#         KeyboardButton(text="Uzum"), 
#         KeyboardButton(text="Shaftoli")
#     ]
# ],
# resize_keyboard=True,
# input_field_placeholder="Kerakli tugmani bosing...")











































# mevalar = ['Anor', 'Olma', 'Anjir', 'Banan', 'Uzum', 'Shaftoli']

# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for meva in mevalar:
#         keyboard.add(InlineKeyboardButton(text=meva, url='...'))
#     return keyboard.adjust(3).as_markup()



# Uyga vazifa: Unikal mavzuda Bot yarating, unda 10 ta Handler yarating, ularning har birida 10 tadan tugma bo'lsin!

# Statik
# 2 ta Handler Reply keyboard orqali yaratilsin!
# 3 ta Handler Inline keyboard orqali yaratilsin!

# Dinamik
# 5 ta Handlerda for orqali button bo'lsin!
# 2 ta Handler Reply keyboard orqali yaratilsin!
# 3 ta Handler Inline keyboard orqali yaratilsin!
