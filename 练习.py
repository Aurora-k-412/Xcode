# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 电商系统需要根据用户选择的支付方式，计算订单最终支付金额，不同支付方式对应不同优惠/手续费，这是后端开发中最常用的多分支判断场景。

# 题目要求
# 输入：订单原始金额（正数）、支付方式编码（1/2/3/4）
# 业务规则：
# 	支付方式 1：微信支付 → 满 100 减 10 元
# 	支付方式 2：支付宝 → 打 95 折
# 	支付方式 3：银行卡 → 无优惠，原价支付
# 	支付方式 4：积分抵扣 → 立减 20 元（订单金额≥20 才可用）
# 	其他编码：输出「支付方式不合法，订单提交失败」
# 输出：支付方式名称、最终应付金额
# 边界：订单金额需大于 0，否则提示「订单金额无效」



money=int(input("金额:"))
pay_way=input("支付方式编码（1/2/3/4）:")
if money>0:
    match pay_way:
        case "1":
            if money>100:
                wei_money=money-10
                print("支付方式:微信支付")
                print("最终应付金额:",wei_money)
            else:
                wei_money=money
                print("支付方式:微信支付")
                print("最终应付金额:",wei_money)
        case "2":
            pay_money=0.95*money
            print("支付方式:支付宝")
            print("最终应付金额:",pay_money)
        case "3":
            card_money=money
            print("支付方式:银行卡")
            print("最终应付金额:",card_money)
        case "4":
            if money>=20:
                jf_money=money-20
                print("支付方式:积分抵扣")
                print("最终应付金额:",jf_money)
            else:
                jf_money=money
                print("支付方式:积分抵扣")
                print("最终应付金额:",jf_money)
        case _:
            print("「支付方式不合法，订单提交失败」")
else:
    print("「订单金额无效」")




# 快递系统需要根据包裹重量、寄件地区、是否会员计算运费，同时做合规校验。

# 输入
# 包裹重量（kg，正数）
# 寄件地区编号（1 - 华东，2 - 华南，3 - 华北，4 - 其他）
# 是否会员（1 = 是，0 = 否）

# 业务规则（嵌入所有分支类型）
# 单分支：包裹重量 > 50kg → 单独打印「⚠️ 包裹超重，需额外人工验收」
# 双分支：判断是否为会员（是 / 否）
# 多分支：根据地区划分基础运费单价
# 分支嵌套：在会员 / 非会员分支内，嵌套重量阶梯计价
# 异常处理：重量≤0 → 提示「重量无效」


weight = float(input("包裹重量（kg）: "))
region = int(input("寄件地区编号（1-华东，2-华南，3-华北，4-其他）: "))
is_vip = int(input("是否会员（1=是，0=否）: "))

if weight <= 0:
    print("重量无效")
    exit()

if weight > 50:
    print("⚠️ 包裹超重，需额外人工验收")

if region == 1:
    base_price = 5
    region_name = "华东"
elif region == 2:
    base_price = 6
    region_name = "华南"
elif region == 3:
    base_price = 4
    region_name = "华北"
elif region == 4:
    base_price = 7
    region_name = "其他"
else:
    print("地区编号不合法")
    exit()

if is_vip == 1:
    if weight <= 10:
        discount = 0.9
    elif weight <= 30:
        discount = 0.8
    else:
        discount = 0.7
    user_type = "会员"
else:
    if weight <= 10:
        discount = 1.0
    elif weight <= 30:
        discount = 0.9
    else:
        discount = 0.8
    user_type = "非会员"

final_price = base_price * weight * discount

print(f"\n寄件地区：{region_name}")
print(f"用户类型：{user_type}")
print(f"基础单价：{base_price} 元/kg")
print(f"折扣：{discount * 100:.0f}%")
print(f"最终运费：{final_price:.2f} 元")



# 题目：现需开发一个智能商场会员系统，该系统根据会员的消费金额、会员等级以及是否为特殊节日来计算折扣和最终应付金额。具体规则如下：
# 	会员等级：分为普通会员、银卡会员、金卡会员。
# 	消费金额：根据不同的消费区间有不同的折扣。
# 	特殊节日：在特殊节日，所有会员额外享受 5% 的折扣。
# 具体规则如下：
# 普通会员：
# 	消费金额低于 500 元，无折扣。
# 	消费金额在 500 元及以上、1000 元以下，享受 9.5 折优惠。
# 	消费金额在 1000 元及以上，享受 9 折优惠。
# 银卡会员：
# 	消费金额低于 800 元，享受 9.5 折优惠。
# 	消费金额在 800 元及以上、1500 元以下，享受 9 折优惠。
# 	消费金额在 1500 元及以上，享受 8.5 折优惠。
# 金卡会员：
# 	消费金额低于 1200 元，享受 9 折优惠。
# 	消费金额在 1200 元及以上、2000 元以下，享受 8.5 折优惠。
# 	消费金额在 2000 元及以上，享受 8 折优惠。


def calculate_discount(level: str, amount: float, is_holiday: bool = False) -> tuple:
    if level == '普通会员':
        if amount < 500:
            base_rate = 1.0
        elif amount < 1000:
            base_rate = 0.95
        else:
            base_rate = 0.90
    elif level == '银卡会员':
        if amount < 800:
            base_rate = 0.95
        elif amount < 1500:
            base_rate = 0.90
        else:
            base_rate = 0.85
    elif level == '金卡会员':
        if amount < 1200:
            base_rate = 0.90
        elif amount < 2000:
            base_rate = 0.85
        else:
            base_rate = 0.80
    else:
        raise ValueError("会员等级只能是 '普通会员', '银卡会员', '金卡会员'")

    if is_holiday:
        final_rate = base_rate * 0.95
    else:
        final_rate = base_rate

    final_amount = amount * final_rate
    return round(final_rate, 4), round(final_amount, 2)

if __name__ == "__main__":
    test_cases = [
        ('普通会员', 400, False),
        ('普通会员', 750, False),
        ('普通会员', 1200, False),
        ('银卡会员', 700, False),
        ('银卡会员', 1200, False),
        ('银卡会员', 1600, False),
        ('金卡会员', 1000, False),
        ('金卡会员', 1500, False),
        ('金卡会员', 2500, False),
        ('金卡会员', 2000, True),
    ]

    for level, amount, holiday in test_cases:
        rate, final = calculate_discount(level, amount, holiday)
        holiday_str = "是" if holiday else "否"
        print(f"{level}，消费{amount}元，特殊节日：{holiday_str}，折扣率：{rate*100:.1f}%，应付金额：{final}元")

# 题目：除上述例子、教材及课堂例题外，分别给出if单分支结构、if-else二分支结构、if-elif-else
# 多分支结构、if结构嵌套（多种方式）的源码例子及对应注释（每种情况给两个例子）。

#if单分支
# 例子1：
aqi = 135
if aqi > 100:
    print("空气质量较差，建议您出门佩戴口罩。")
# 例子2：
comment = "这个产品真垃圾"
sensitive_words = ["垃圾", "差劲", "骗人"]
if any(word in comment for word in sensitive_words):
    print("检测到敏感评论，已记录到审核日志。")

# if-else二分支结构
score = 68
if score >= 60:
    print("恭喜您，考试通过！")
else:
    print("很遗憾，考试未通过，请继续努力。")


password = "abc123"
if len(password) >= 8:
    print("密码长度符合要求。")
else:
    print(f"密码长度不足，当前长度为{len(password)}，请使用至少8位字符。")

# if-elif-else多分支结构
battery = 23
if battery >= 80:
    print("电量充足，无需充电。")
elif battery >= 50:
    print("电量适中，可正常使用。")
elif battery >= 20:
    print("电量较低，建议尽快充电。")
else:
    print("电量严重不足，请立即连接充电器！")


user_level = "黄金"
if user_level == "钻石":
    coupon = 100
elif user_level == "黄金":
    coupon = 60
elif user_level == "白银":
    coupon = 30
else:
    coupon = 10

print(f"您的等级为{user_level}，获得{coupon}元优惠券。")


# if结构嵌套
age = 22
is_real_name = True
if age >= 18:
    if is_real_name:
        print("您已成年且完成实名认证，可以参与抽奖活动。")
    else:
        print("您已成年，但需要先完成实名认证才能参与活动。")
else:
    print("您未满18岁，无法参与该活动。")

# 模拟一个周末早餐选择推荐系统
weather = "晴天"
time_morning = 9
if weather == "晴天":
    if time_morning < 8:
        print("天气晴朗且时间尚早，推荐去公园晨跑后吃早茶。")
    elif time_morning < 10:
        print("阳光正好，推荐户外咖啡馆吃西式早餐。")
    else:
        print("临近中午，建议吃早午餐（brunch）。")
elif weather == "阴天":
    if time_morning < 9:
        print("阴天稍凉，推荐在家煮热粥配煎蛋。")
    else:
        print("阴天不晒，适合去书店内的轻食店吃早餐。")
else:  # 雨天
    if time_morning < 8:
        print("下雨且很早，建议继续睡觉或点外卖早餐。")
    else:
        print("雨天不宜外出，推荐自制三明治搭配热饮。")



print("2026年3月")
print("  一 二 三 四 五 六 日")

first_day_weekday = 6  # 星期日对应索引6（周一=0，周日=6）
days_in_month = 31

day = 1
for row in range(6):
    for col in range(7):
        if row == 0 and col < first_day_weekday:
            print("   ", end=" ")
        elif day <= days_in_month:
            print(f"{day:2d}", end=" ")
            day += 1
        else:
            print("   ", end=" ")
    print()