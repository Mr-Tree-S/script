#coding=utf-8
import socket,threading

# try:
#     level=open('.level').read()
#     level=int(level)
# except:
#     level=1




global level,res1,res2
level = 1
res1 = 1
res2 = 1

def battle():
    global level
    class user():
        HP=int(100+(4*level))
        Danger=int(10+(3*level))
        Defence=int(5+(1*level))
    class npc():
        name = '穿山甲'
        HP = (3 ** 15)
        Danger = (3 ** 10)
        Defence = 100

    print('面板\t血量\t攻击力\t防御力\t\n'),
    print('玩家 %s\t%s\t%s\t\n'%(user.HP,user.Danger,user.Defence)),
    print('怪物 %s\t%s\t%s\t\n'%(npc.HP,npc.Danger,npc.Defence)),
    user.Danger=user.Danger-npc.Defence
    npc.Danger=npc.Danger-user.Defence
    if user.Danger <=0:
        user.Danger=1
    if npc.Danger <=0:
        npc.Danger=1

    print("开始战斗".center(41,'^'))
    while 1:
        npc.HP=npc.HP-user.Danger
        print('你对%s造成了%s 怪物剩余血量 %s\t\n'%(npc.name,user.Danger,npc.HP))
        user.HP=user.HP-npc.Danger
        print('%s对你造成了%s 你剩余血量 %s\t\n'%(npc.name,npc.Danger,user.HP))
        if npc.HP<=0 and user.HP<=0:
            print('平局!!!')
            break
        if npc.HP <=0:
            print('你赢了!!!,你剩余血量 %s\t\n'%(user.HP)),
            break
        if user.HP <=0:
            print('你死了!!!%s剩余血量 %s\t\n'%(npc.name,npc.HP)),
            break
    print(("战斗结束 等级+1 您目前等级%s"%(int(level)+1)).center(49,'^'))
    level=level+1
    global res1,res2
    res1=npc.HP
    res2=user.HP
    # open('.level','w').write(str(level+1))
while res1>0 or res2<0:
    battle()




# import math, base64
#
# def battle(level):
#     HP = 4 * level + 100
#     ATK = max(3 * level - 90, 1)
#     M_ATK = max(3 ** 10 - level - 5, 1)
#     return True if math.ceil(3 ** 15 / ATK) < HP / M_ATK else False
#
# geitaoshenketou = 3 ** 100  # 超大
# l = [0, geitaoshenketou]
# while True:
#     if l[1] - l[0] == 1:
#         res = base64.b64encode(str(l[1]).encode())
#         print('flag{' + res.decode() + '}')
#         break
#     elif battle(sum(l) // 2):
#         l = [l[0], sum(l) // 2]
#     else:
#         l = [sum(l) // 2, l[1]]