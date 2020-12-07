import json
import urllib.request
import crawler
api_url = 'https://api.exchangeratesapi.io/latest'

with urllib.request.urlopen(api_url) as f:
    api_out = f.read()
    
to_json = api_out.decode('utf8').replace("'",'"') # Convert Byte To Str

final_exported_json = json.loads(to_json)

json_export_loop = final_exported_json.values()

dict_counter = 0
for a in json_export_loop:
    dict_counter += 1
    currency = a # adding keys and values to a dict
    if dict_counter == 1:
        break
# GET USD VALUE FROM DICT
currency_USD_key = ['USD',]
currency_USD_value = list(map(currency.get, currency_USD_key))
USD_TO_EUR_value = str(currency_USD_value)
USD_float = float(USD_TO_EUR_value[1:7])

# USD TO EURO CACULATION
USD_API_T_FLOAT = float(crawler.usd_crawler())
EURO = USD_float * USD_API_T_FLOAT
# Currency Converter Loop
cur_out = list()
for cur in list(currency.values()):
    cur_usd_base = float(EURO) / float(cur)
    cur_usd_base_str = str(cur_usd_base)
    cur_out.append(cur_usd_base_str[0:8])
    
cur_keys_list = (list(currency.keys()))
# Convert Data To Dict
final_dict = dict()
for o in range(len(cur_keys_list)):
    ckl_ka = str(cur_keys_list[o])
    co_va = cur_out[o]
    final_dict[ckl_ka] = cur_out[o]

# Convert To json And Export
with open('currency-data.json', 'w', encoding='utf-8') as outfile:
    json.dump(final_dict, outfile, ensure_ascii=False, indent=4)