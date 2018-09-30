class Loc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '{} {}'.format(self.x, self.y)

# ========== Key Map ==========
# BTN
QUEST = Loc(359, 1035)
SORT = Loc(359, 1120)
MAKE_EQUIP = Loc(359, 1220)

# SKILL
SKILL1 = Loc(664, 796)
SKILL2 = Loc(664, 898)
SKILL3 = Loc(664, 997)
SKILL4 = Loc(664, 1096)

# OPT
L_OPT = Loc(230, 922)
M_OPT = Loc(360, 922)
R_OPT = Loc(490, 922)

# SHOP
SHOP_1 = Loc(191, 630)
SHOP_2 = Loc(359, 630)
SHOP_3 = Loc(530, 630)
SHOP_4 = Loc(191, 794)
SHOP_5 = Loc(359, 794)
SHOP_6 = Loc(530, 794)
SHOP_ALL = [SHOP_1, SHOP_2, SHOP_3, SHOP_4, SHOP_5, SHOP_6]
# ========== Key Map ==========
