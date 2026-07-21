def get_constellation(month: int, day: int) -> str:
    """
    根据传入的月、日判断对应星座
    :param month: 月份 1-12
    :param day: 日期 1-31
    :return: 星座名称
    """
    # 星座分界 (月, 分界日, 星座名)
    constell_cutoff = [
        (1, 20, "水瓶座"),
        (2, 19, "双鱼座"),
        (3, 21, "白羊座"),
        (4, 20, "金牛座"),
        (5, 21, "双子座"),
        (6, 22, "巨蟹座"),
        (7, 23, "狮子座"),
        (8, 23, "处女座"),
        (9, 23, "天秤座"),
        (10, 24, "天蝎座"),
        (11, 23, "射手座"),
        (12, 22, "摩羯座")
    ]

    # 遍历匹配正确星座，修复原索引-1崩溃、Pylance语法报错问题
    for idx, (m, d, name) in enumerate(constell_cutoff):
        if month < m:
            continue
        if month == m and day < d:
            # 1月上一个星座是摩羯座，避免负数索引
            if idx == 0:
                return constell_cutoff[-1][2]
            return constell_cutoff[idx - 1][2]
    # 12月下旬固定返回摩羯座
    return constell_cutoff[-1][2]


def check_birth_input(month_input, day_input):
    """
    输入合法性校验函数，修复非数字输入直接崩溃报错问题
    :param month_input: 用户输入月份字符串
    :param day_input: 用户输入日期字符串
    :return: bool, msg, month, day
    """
    # 先强制校验输入必须是字符串类型
    if not isinstance(month_input, str) or not isinstance(day_input, str):
        return False, "输入错误！月份和日期必须输入数字文本", 0, 0
    # 拦截字母、符号、混合字符输入
    if not (month_input.isdigit() and day_input.isdigit()):
        return False, "输入错误！月份和日期必须为纯数字，不能包含文字/符号", 0, 0

    try:
        month = int(month_input)
        day = int(day_input)
    except ValueError:
        return False, "数字转换失败，请输入纯数字", 0, 0

    # 月份范围校验
    if month < 1 or month > 12:
        return False, "月份输入非法！请输入1-12之间的月份！", 0, 0

    # 日期基础范围校验
    if day < 1 or day > 31:
        return False, "日期输入非法！请输入1~31的有效日期！", 0, 0

    # 大小月精准校验
    if month in [4, 6, 9, 11] and day > 30:
        return False, f"{month}月只有30天，无{day}号，请重新输入！", 0, 0
    if month == 2 and day > 29:
        return False, "2月最大日期为29天，请重新输入！", 0, 0

    return True, "输入合法", month, day
