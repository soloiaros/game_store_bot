from dataclasses import dataclass
from typing import List
from aiogram.types import LabeledPrice
from aiogram import types
from config import YOUKASSA_TEST_PAYMENT_API

@dataclass
class Item:
   title: str
   description: str
   start_parameter: str
   currency: str
   prices: List[LabeledPrice]
   provider_data: dict = None
   photo_url: str = None
   photo_size: int = None
   photo_width: int = None
   photo_height: int = None
   need_name: bool = False
   need_phone_number: bool = False
   need_email: bool = False
   need_shipping_address: bool = False
   send_phone_number_to_provider: bool = False
   send_email_to_provider: bool = False
   is_flexible: bool = False
   provider_token: str = YOUKASSA_TEST_PAYMENT_API

   def generate_invoices(self):
      return self.__dict__


invoices_dict = {
    'mortal_combat': Item(
       title='Mortal Combat',
       description='a mortal combat cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Mortal Combat 11',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_mortal_combat',
       photo_url="https://i.pinimg.com/originals/37/a2/0c/37a20c86614f489a1659e90cde471d3c.png",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'street_fighter': Item(
       title='Street Fighter 5',
       description='a street fighter cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Street Fighter 5',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_street_fighter',
       photo_url="https://content.rozetka.com.ua/goods/images/original/189376417.jpg",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'crusader_kings': Item(
       title='Crusader Kings III',
       description='a crusader kings cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Crusader Kings III',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_crusader_kings',
       photo_url="https://d1lss44hh2trtw.cloudfront.net/assets/article/2022/01/26/crusader-kings-3-headed-to-ps5-xbox-series-x-s-in-march_feature.jpg",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'civilization': Item(
       title='The Civilization VI',
       description='a civilization 6 cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра The Civilization VI',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_the_civilization',
       photo_url="https://store-images.s-microsoft.com/image/apps.9132.14403675424199419.fe954dc9-c050-4de0-85e2-2f588b83ad99.2a036cfc-d1a0-49b5-a3a3-5289cad19d4c",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'skyrim': Item(
       title='The Elder Scrolls V: Skyrim',
       description='a skyrim cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра The Elder Scrolls V: Skyrim',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_the_elder_scrolls_v',
       photo_url="https://img3.goodfon.ru/original/2560x1024/0/66/bethesda-the-elder-scrolls.jpg",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'warcraft': Item(
       title='World of Warcraft',
       description='a wow cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра World of Warcraft',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_world_of_warcraft',
       photo_url="https://i.ytimg.com/vi/LYu6QlyaF1g/maxresdefault.jpg",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'cities_skylines': Item(
       title='Cities Skylines',
       description='a cities skylines cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Cities Skylines',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_cities_skylines',
       photo_url="https://avatars.mds.yandex.net/get-mpic/5233339/img_id30449053015162518.jpeg/orig",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'minecraft': Item(
       title='Minecraft',
       description='a minecraft cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Minecraft',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_minecraft',
       photo_url="https://gamefaqs.gamespot.com/a/box/5/4/6/150546_front.jpg",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'gta': Item(
       title='Grand theft Auto V',
       description='a gta v cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Grand theft Auto V',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_gtav',
       photo_url="https://dailygame.at/wp-content/uploads/2020/05/ps5-gta-5-packshot.jpg",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
    'rdr': Item(
       title='Red Dead Redemption 2',
       description='a rdr 2 cd disk',
       currency='RUB',
       prices=[
          LabeledPrice(
             label='Игра Red Dead Redemption 2',
             amount=1000_00
          ),
          LabeledPrice(
             label='Доставка',
             amount=500_00
          ),
          LabeledPrice(
             label='Скидка',
             amount=-100_00
          )
       ],

       start_parameter='create_invoice_rdrii',
       photo_url="https://preview.redd.it/11trlrdc0bo51.jpg?auto=webp&s=621d70afb14eb9b72666368c050933080d11f711",
       photo_size=600,
       need_shipping_address=True,
       is_flexible= True
    ),
}


POST_REGULAR_SHIPPING = types.ShippingOption(
   id='post_reg',
   title='Почтой',
   prices=[
      types.LabeledPrice(
         'Обычная коробка', 0
      ),
      types.LabeledPrice(
         'Почтой', 500_00
      ),
   ]
)

POST_FAST_SHIPPING = types.ShippingOption(
   id='post_fast',
   title='Почтой ускоренная',
   prices=[
      types.LabeledPrice(
         'Прочная упаковка', 200_00
      ),
      types.LabeledPrice(
         'Срочной почтой', 1000_00
      ),
   ]
)

# самовывоз
PICKUP_SHIPPING = types.ShippingOption(
   id='pickup',
   title='Самовывоз',
   prices=[
      types.LabeledPrice(
         "Самовывоз из магазина", - 0
      ),

   ]
)
