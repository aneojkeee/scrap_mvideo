import requests
import json

def get_data():

    cookies = {
        '_ym_uid': '1671300938141373320',
        '_ym_d': '1671300938',
        '__lhash_': '65f7fb64926b0a180b6ab033958c1662',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_15500',
        'MVID_COOKIE': '3500',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_IMG_RESIZE': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '4800000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MCLICK_NEW': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '33',
        'MVID_REGION_SHOP': 'S939',
        'MVID_SERVICES': '111',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_sp_ses.d61c': '*',
        '_ga': 'GA1.2.442201527.1675418286',
        '_gid': 'GA1.2.1265163382.1675418286',
        '_ym_isad': '2',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': 'a8bc6cb2cdbefd869a839e47104d56b4',
        'tmr_lvidTS': '1671300941593',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '13a54abf-212a-46c1-9b67-3874f8fd7032',
        'advcake_track_id': '29e8bcbd-2aea-81a8-39fc-96863657dd06',
        'advcake_session_id': '92ca250a-de48-1f52-251b-ab9263fd7e99',
        'adrdel': '1',
        'adrcid': 'APyAeReH-uyoPmUq65--05Q',
        'flocktory-uuid': 'a8c1dc80-4e08-4721-b2ac-ed7089a799b2-1',
        'afUserId': '4b934eed-ccb1-4f41-b4df-111277267ba3-p',
        'AF_SYNC': '1675418290164',
        'tmr_detect': '0%7C1675418291401',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_sp_id.d61c': '75420e10-1245-4592-ae78-89f4685fd151.1671300938.2.1675418413.1671301006.e4ee8f04-c315-4d95-8014-fb1bfe856695.add5e5c0-ae51-427d-b21d-ebee08b07d4a.580104e5-0502-4d20-8f44-3f4e1dcce2e7.1675418285638.32',
        '_ga_CFMZTSS5FM': 'GS1.1.1675418285.1.1.1675418449.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1675418285.1.1.1675418449.60.0.0',
        'MVID_ENVCLOUD': 'prod1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9,en-US;q=0.8',
        'baggage': 'sentry-release=23.1.31.1,sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=afabafde863f4439b3e37da8fba38c2d,sentry-sample_rate=0.5',
        # 'cookie': '_ym_uid=1671300938141373320; _ym_d=1671300938; __lhash_=65f7fb64926b0a180b6ab033958c1662; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_15500; MVID_COOKIE=3500; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=4800000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=33; MVID_REGION_SHOP=S939; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _sp_ses.d61c=*; _ga=GA1.2.442201527.1675418286; _gid=GA1.2.1265163382.1675418286; _ym_isad=2; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; tmr_lvid=a8bc6cb2cdbefd869a839e47104d56b4; tmr_lvidTS=1671300941593; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=13a54abf-212a-46c1-9b67-3874f8fd7032; advcake_track_id=29e8bcbd-2aea-81a8-39fc-96863657dd06; advcake_session_id=92ca250a-de48-1f52-251b-ab9263fd7e99; adrdel=1; adrcid=APyAeReH-uyoPmUq65--05Q; flocktory-uuid=a8c1dc80-4e08-4721-b2ac-ed7089a799b2-1; afUserId=4b934eed-ccb1-4f41-b4df-111277267ba3-p; AF_SYNC=1675418290164; tmr_detect=0%7C1675418291401; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _sp_id.d61c=75420e10-1245-4592-ae78-89f4685fd151.1671300938.2.1675418413.1671301006.e4ee8f04-c315-4d95-8014-fb1bfe856695.add5e5c0-ae51-427d-b21d-ebee08b07d4a.580104e5-0502-4d20-8f44-3f4e1dcce2e7.1675418285638.32; _ga_CFMZTSS5FM=GS1.1.1675418285.1.1.1675418449.0.0.0; _ga_BNX5WPP3YK=GS1.1.1675418285.1.1.1675418449.60.0.0; MVID_ENVCLOUD=prod1',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'afabafde863f4439b3e37da8fba38c2d-a649eb23096a3727-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-set-application-id': '013d603b-1ae4-41ad-8745-387c7c991721',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open ('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()
    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()

if __name__ == '__main__':
    main()