def get_constellation(month: int, day: int) -> str:
    """
    根据传入的月、日判断对应星座
    :param month: 月份 1-12
    :param day: 日期 1-31
    :return: 星座名称
    """
    # 星座日期区间
    dates = ((1, 20, "水瓶座"), (2, 19, "双鱼座"), (3, 21, "白羊座"),
             (4, 20, "金牛座"), (5, 21, "双子座"), (6, 22, "巨蟹座"),
             (7, 23, "狮子座"), (8, 23, "处女座"), (9, 23, "天秤座"),
             (10, 24, "天蝎座"), (11, 23, "射手座"), (12, 22, "摩羯座")))

    # 遍历判断星座
    if day < dates[month-1][1]:
        return dates[month-2][2]
    else:
        return dates[month-1][2]


def check_birth_input(month_input, day_input):
    """
    输入合法性校验函数
    :param month_input: 用户输入月份
    :param day_input: 用户输入日期
    :return: bool, msg, month, day
    """
    # 判断是否为数字
    if not (month_input.isdigit() and day_input.isdigit()):
        return False, "输入错误！月份和日期必须为纯数字！", 0, 0

    month = int(month_input)
    day = int(day_input)

    # 月份范围校验
    if month< 1 or month > 12:
        return False, "月份输入非法！请输入1-12之间的月份！", 0, 0

    # 日期基础范围校验
    if day< 1 or day > 31:
        return False, "日期输入非法！请输入合法日期！", 0, 0

    # 小月日期精准校验
    if month in [4,6,9,11] and day > 30:
        return False, "当前月份没有31号，请重新输入！", 0, 0
    if month == 2 and day > 29:
        return False, "2月日期输入超限，请重新输入！", 0, 0

    return True, "输入合法", month, day
