import numpy as np 
import matplotlib.pyplot as plt
from scipy import interpolate

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

########################################################
# 统计等级的收益以及经验值                                 #
########################################################

def sum_list(delta_list):
    sum_l = [delta_list[0]]
    for d in delta_list[1:]:
        sum_l.append(sum_l[-1]+d)
    return np.array(sum_l)

old_pack = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 
0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 
0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

new_pack = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
gold = [0, 0, 0, 0, 0, 100, 100, 0, 100, 0, 100, 0, 100, 100, 150, 100, 0, 100, 100, 0, 
100, 100, 0, 100, 0, 150, 0, 150, 150, 0, 150, 150, 0, 150, 150, 200, 0, 200, 200, 0, 
200, 0, 200, 200, 300, 0, 300, 0, 300, 0, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 
150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 
150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 
150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 
150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 
150, 150, 150, 150, 150, 150, 150, 150, 150, 150,
]
dust = [400, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

sum_old_pack = sum_list(old_pack)
sum_new_pack = sum_list(new_pack)
sum_gold = sum_list(gold)
sum_dust = sum_list(dust)

exp = [100, 150, 200, 300, 450, 600, 750, 900, 1050, 1250, 
1500, 1750, 2000, 2200, 2400, 2500, 2600, 2700, 2800, 2900, 
3000, 3100, 3200, 3300, 3450, 3600, 3750, 3900, 4050, 4250, 
4450, 4650, 4850, 5050, 5300, 5550, 5800, 6050, 6300, 6600, 
6900, 7200, 7500, 7800, 8100, 8400, 8700, 9000, 9300, 4000, 
4050, 4100, 4150, 4200, 4250, 4300, 4350, 4400, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 
4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500]
sum_exp = sum_list(exp)

sum_equ_gold = (sum_gold + sum_old_pack*70 + sum_new_pack*100 + sum_dust*1)

########################################################
# 计算折算成金币的经验收益曲线                              #
########################################################

plt.plot(sum_exp, sum_equ_gold)
plt.title('折算成金币的经验收益曲线')
plt.xlabel('经验值')
plt.ylabel('金币值')
plt.savefig('img/折算成金币的经验收益曲线.png')
plt.savefig('img/折算成金币的经验收益曲线.svg')
plt.close()


plt.plot(sum_exp[:50], sum_equ_gold[:50])
plt.title('折算成金币的经验收益曲线（前50级）')
plt.xlabel('经验值')
plt.ylabel('金币值')
plt.savefig('img/折算成金币的经验收益曲线（前50级）.png')
plt.savefig('img/折算成金币的经验收益曲线（前50级）.svg')
plt.close()

########################################################
# 计算每天花费不同的时间之后的金币收益                       #
########################################################
achievement_exp = 5000/(16*7)
base_exp = 13000/7

gold_exp = interpolate.interp1d(sum_exp, sum_gold, kind='cubic')

# 如果没有通行证
for hour_per_day in [0, 1, 2, 4, 8]:
    exp_days = sum_list(np.ones(16*7) * (base_exp+achievement_exp) + 350*hour_per_day)
    gold_days = gold_exp(exp_days)
    plt.plot(np.arange(1, 16*7+1), gold_days, label='每天%dh' % hour_per_day)

    plt.annotate('%d' % int(gold_days[-1]),
            xy=(16*7, gold_days[-1]),
            color='black',
            bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.8))

plt.legend()
plt.title('折算成金币的时间收益曲线（没有通行证）')
plt.xlabel('从新版本开始的天数')
plt.ylabel('金币值')
plt.savefig('img/折算成金币的时间收益曲线（没有通行证）.png')
plt.savefig('img/折算成金币的时间收益曲线（没有通行证）.svg')
plt.close()

# 如果有通行证
for hour_per_day in [0, 1, 2, 4, 8]:
    exp_days = sum_list(np.ones(16*7) * (base_exp+achievement_exp) + 350*hour_per_day)*1.1
    gold_days = gold_exp(exp_days)
    plt.plot(np.arange(1, 16*7+1), gold_days, label='每天%dh' % hour_per_day)

    plt.annotate('%d' % int(gold_days[-1]),
            xy=(16*7, gold_days[-1]),
            color='black',
            bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.8))

plt.legend()
plt.title('折算成金币的时间收益曲线（有通行证）')
plt.xlabel('从新版本开始的天数')
plt.ylabel('金币值')
plt.savefig('img/折算成金币的时间收益曲线（有通行证）.png')
plt.savefig('img/折算成金币的时间收益曲线（有通行证）.svg')
plt.close()


# ########################################################
# # 比较有没有战令的收益曲线                                 #
# ########################################################

# for hour_per_day in [0, 1, 2, 4, 8]:
#     exp_days = sum_list(np.ones(16*7) * (base_exp+achievement_exp) + 350*hour_per_day)
#     plt.plot(np.arange(1, 16*7+1), gold_exp(exp_days), label='没有通行证')
#     plt.plot(np.arange(1, 16*7+1), gold_exp(exp_days*1.1), label='有通行证')

#     plt.annotate('%d' % int(gold_exp(exp_days[-1])),
#             xy=(16*7, gold_exp(exp_days[-1])),
#             color='black',
#             bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.8))
#     plt.annotate('%d' % int(gold_exp(exp_days[-1]*1.1)),
#             xy=(16*7, gold_exp(exp_days[-1]*1.1)),
#             color='black',
#             bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.8))

#     plt.legend()
#     plt.title('折算成金币的收益比较-每天%d小时' % hour_per_day)
#     plt.xlabel('从新版本开始的天数')
#     plt.ylabel('金币值')
#     plt.savefig('img/折算成金币的收益比较-每天%d小时.png' % hour_per_day)
#     plt.savefig('img/折算成金币的收益比较-每天%d小时.svg' % hour_per_day)
#     plt.close()


########################################################
# 与之前的收益进行比较                                    #
########################################################

for hour_per_day in [0, 1, 2, 4, 8]:
    exp_days = sum_list(np.ones(16*7) * (base_exp+achievement_exp) + 350*hour_per_day)
    gold_days_new1 = gold_exp(exp_days)
    gold_days_new2 = gold_exp(exp_days*1.1)

    gold_days_normal = sum_list(np.ones(16*7)*(60 + min(hour_per_day/2*(60/15)*0.5*10/3, 100)))
    gold_days_py = sum_list(np.ones(16*7)*(60 + min(hour_per_day/2*(60/1)*0.5*10/3, 100)))

    plt.plot(np.arange(1, 16*7+1), gold_days_new1, label='战令收益（没有通行证）')
    plt.plot(np.arange(1, 16*7+1), gold_days_new2, label='战令收益（有通行证）')
    plt.plot(np.arange(1, 16*7+1), gold_days_normal, label='不互投')
    plt.plot(np.arange(1, 16*7+1), gold_days_py, label='互投')

    # plt.annotate('%d' % int(gold_days_new1[-1]),
    #         xy=(16*7, gold_days_new1[-1]),
    #         color='black',
    #         bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.5))
    # plt.annotate('%d' % int(gold_days_new2[-1]),
    #         xy=(16*7, gold_days_new2[-1]),
    #         color='black',
    #         bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.5))
    # plt.annotate('%d' % int(gold_days_normal[-1]),
    #         xy=(16*7, gold_days_normal[-1]),
    #         color='black',
    #         bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.5))
    # plt.annotate('%d' % int(gold_days_py[-1]),
    #         xy=(16*7, gold_days_py[-1]),
    #         color='black',
    #         bbox=dict(boxstyle='square,pad=0.5', fc='white', ec='k',lw=1 ,alpha=0.5))


    plt.annotate('%d' % int(gold_days_new1[-1]),
            xy=(16*7, gold_days_new1[-1]),
            color='blue')
    plt.annotate('%d' % int(gold_days_new2[-1]),
            xy=(16*7, gold_days_new2[-1]),
            color='orange')
    plt.annotate('%d' % int(gold_days_normal[-1]),
            xy=(16*7, gold_days_normal[-1]),
            color='green')
    plt.annotate('%d' % int(gold_days_py[-1]),
            xy=(16*7, gold_days_py[-1]),
            color='red')

    plt.legend()
    plt.title('收益比较-每天%d小时' % hour_per_day)
    plt.xlabel('从新版本开始的天数')
    plt.ylabel('金币值')
    plt.savefig('img/收益比较-每天%d小时.png' % hour_per_day)
    plt.savefig('img/收益比较-每天%d小时.svg' % hour_per_day)
    plt.close()