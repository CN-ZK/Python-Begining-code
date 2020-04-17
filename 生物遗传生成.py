'''
用于实现:生物后代遗传生成
F1: AAss-AaSs
F2: ['AAsS', 'AAss', 'AasS', 'Aass']

程序:  
本1: AAss
本2: AaSs
['AAsS', 'AAss', 'AasS', 'Aass']
AAsS: 25.0%
AAss: 25.0%
AasS: 25.0%
Aass: 25.0%

缺点: 
无法实现 像'Aa x aa' 这样的生成
'''
def generate(fa, mo):
    result = []
    fa_num = -1
    mo_num = -1
    for a in range(2):
        fa_num += 1
        for b in range(2):
            mo_num += 1
            result.append(fa[a] + mo[b])
    fa_num = 1
    mo_num = 2
    for a in range(2):
        fa_num += 1
        for b in range(2):
            result.append(fa[fa_num] + mo[mo_num])
            mo_num += 1
        mo_num = 2
    res = []
    for a in range(4):
        for b in range(4, 8):
            res.append(result[a] + result[b])
    delete(res)


def delete(old_):
    new = []
    for old in old_:
        if old not in new:
            new.append(old)
    report(old_, new)


def report(old: list, new: list):
    print(new)
    for a in new:
        print(f'{a}: {(old.count(a)/len(old))*100}%')


print('自交请输入 ! + 基因\n')
while True:
    fa_ = input('本1: ')
    if fa_[0] == '!':
        big(fa_.replace('!', ''), fa_.replace('!', ''))
        continue
    big(fa_, input('本2: '))
