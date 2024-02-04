'''
Author: hibana2077 hibana2077@gmail.com
Date: 2024-02-04 16:22:51
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2024-02-04 17:58:35
FilePath: /nexus/src/backend/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from fugle import Fugle
client = Fugle('MTJiNTVmYzgtYThlNC00MjAyLWFlYzAtMDBhMzMzMGVhMTZiIGYwODA4MzFiLTQxNzMtNDMzOC1hZDgyLTFkYzJkZGUwNmZhOA==')
temp_data = client.get_index_price()
print('\n'.join([f'{k} has {len(v[:180])} klines' for k,v in temp_data.items()]))
temp_data = {k:v[:180] for k,v in client.get_index_price().items()}
output_list = []
for k,v in temp_data.items():
    for i in v:
        i.pop('open')
        i.pop('high')
        i.pop('low')
        i.pop('volume')
        i['group'] = k
        output_list.append(i)

print(f"total {len(output_list)} klines, should be 180*{len(temp_data)} = {180*len(temp_data)}")
# print(client.get_all_index())