old_pack = []
new_pack = []
gold = []
dust = []

with open('bonus.txt', 'r', encoding='utf8') as fin:
    index = 0
    for line in fin.readlines():
        index += 1
        bonus_str = line.split(' ')[1]

        if '暗月包' in bonus_str:
            new_pack.append(1)
        else:
            new_pack.append(0)

        if '包' in bonus_str and '暗月包' not in bonus_str:
            old_pack.append(1)
        else:
            old_pack.append(0)

        if '金币' in bonus_str:
            gold.append(int(bonus_str[:-2]))
        elif '旅店通票' in bonus_str:
            gold.append(150)
        else:
            gold.append(0)

        if '传说' in bonus_str:
            dust.append(400)
        elif '史诗' in bonus_str:
            dust.append(100)
        else:
            dust.append(0)

print(old_pack)
print(new_pack)
print(gold)
print(dust)
