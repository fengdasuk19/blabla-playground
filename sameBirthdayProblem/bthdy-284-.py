import math # Using Stirling's_approximation 使用 斯特林公式

P0 = 1 - math.sqrt(365.0 / 81.0) * math.pow((365.0 / 81.0), 81) * math.exp(-284)#284 人中 至少两个人同一天生日的概率 P0

print "P0 =", P0

P1 = (284 * 283.0 / (2 * 365.0)) * math.sqrt(365.0 / 83.0) * math.pow((365.0 / 83.0), 83) * math.exp(-282)

#284 人中 恰好 2 人生日相同的概率 P1

print "P1 =", P1

P2 = P0 - P1

#284 人中 至少 3 人生日相同的概率 P2

print "P2 =",P2
