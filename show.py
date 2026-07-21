"""
show.py
星座运势控制台美化输出模块11
负责：美化控制台打印效果，统一星座运势展示格式
"""

# ==================== 样式常量定义 ====================

# 边框与分割线字符
TOP_BORDER = "╔" + "═" * 50 + "╗"
BOTTOM_BORDER = "╚" + "═" * 50 + "╝"
MIDDLE_BORDER = "╠" + "═" * 50 + "╣"
SIDE = "║"

# 颜色代码（ANSI转义序列）
COLOR_RESET = "\033[0m"
COLOR_GOLD = "\033[33m"      # 金色 - 标题
COLOR_CYAN = "\033[36m"      # 青色 - 星座名
COLOR_PINK = "\033[35m"      # 粉色 - 桃花
COLOR_GREEN = "\033[32m"     # 绿色 - 财运
COLOR_BLUE = "\033[34m"     # 蓝色 - 性格
COLOR_RED = "\033[31m"      # 红色 - 警告/错误
COLOR_WHITE = "\033[37m"    # 白色 - 正文


# ==================== 核心输出函数 ====================

def print_centered(text, width=50, color=COLOR_WHITE):
    """
    居中打印一行文本，带颜色
    
    参数:
        text: 要打印的文本
        width: 行宽（默认50）
        color: ANSI颜色代码
    """
    # 计算居中所需的左右空格
    padding = (width - len(text)) // 2
    left_pad = " " * padding
    right_pad = " " * (width - len(text) - padding)
    
    print(f"{SIDE}{color}{left_pad}{text}{right_pad}{COLOR_RESET}{SIDE}")


def print_section(title, content, title_color, content_color):
    """
    打印一个分模块的区块（标题+内容）
    
    参数:
        title: 区块标题
        content: 区块内容
        title_color: 标题颜色
        content_color: 内容颜色
    """
    print(f"{SIDE}{title_color}【{title}】{COLOR_RESET}{' ' * (46 - len(title) * 2)}{SIDE}")
    
    # 内容自动换行处理（每行最多46个字符）
    max_line_length = 46
    while len(content) > 0:
        if len(content) <= max_line_length:
            line = content
            content = ""
        else:
            # 尽量在空格处截断，避免截断单词
            cut_pos = content.rfind(" ", 0, max_line_length + 1)
            if cut_pos == -1:
                cut_pos = max_line_length
            line = content[:cut_pos]
            content = content[cut_pos:].strip()
        
        padding = " " * (max_line_length - len(line))
        print(f"{SIDE}  {content_color}{line}{padding}{COLOR_RESET}  {SIDE}")


def show_welcome():
    """
    打印程序欢迎界面
    """
    print("\n" + TOP_BORDER)
    print_centered("✨ 星 座 运 势 查 询 系 统 ✨", color=COLOR_GOLD)
    print(MIDDLE_BORDER)
    print_centered("请输入您的生日", color=COLOR_WHITE)
    print_centered("我们将为您解读专属星座运势", color=COLOR_WHITE)
    print(BOTTOM_BORDER + "\n")


def show_error(message):
    """
    打印错误提示信息（红色高亮）
    
    参数:
        message: 错误信息内容
    """
    print("\n" + TOP_BORDER)
    print_centered("⚠ 输 入 错 误 ⚠", color=COLOR_RED)
    print(MIDDLE_BORDER)
    print_centered(message, color=COLOR_RED)
    print(BOTTOM_BORDER + "\n")


def show_star_info(star_name, star_info):
    """
    主函数：展示星座完整运势信息
    
    参数:
        star_name: 星座名称（如"白羊座"）
        star_info: 字典，包含 birthday/character/love/wealth 等字段
    """
    print("\n" + TOP_BORDER)
    print_centered(f"⭐ {star_name} ⭐", color=COLOR_CYAN)
    print(MIDDLE_BORDER)
    
    # 打印生日区间
    birthday = star_info.get("birthday_range", "未知")
    print_centered(f"📅 生日区间: {birthday}", color=COLOR_WHITE)
    print(MIDDLE_BORDER)
    
    # 分模块展示：性格
    character = star_info.get("character", "暂无数据")
    print_section("性格特点", character, COLOR_BLUE, COLOR_WHITE)
    print(MIDDLE_BORDER)
    
    # 分模块展示：桃花
    love = star_info.get("love_luck", "暂无数据")
    print_section("桃花运势", love, COLOR_PINK, COLOR_WHITE)
    print(MIDDLE_BORDER)
    
    # 分模块展示：财运
    wealth = star_info.get("wealth_luck", "暂无数据")
    print_section("财运指数", wealth, COLOR_GREEN, COLOR_WHITE)
    
    print(BOTTOM_BORDER + "\n")


def show_goodbye():
    """
    打印程序结束语
    """
    print("\n" + TOP_BORDER)
    print_centered("🌟 感谢使用星座运势查询系统 🌟", color=COLOR_GOLD)
    print_centered("愿星辰指引你的方向", color=COLOR_WHITE)
    print(BOTTOM_BORDER + "\n")


# ==================== 测试代码 ====================

if __name__ == "__main__":
    # 模拟测试：展示欢迎界面 + 示例星座数据
    show_welcome()
    
    # 模拟从data.py获取的数据
    test_data = {
        "birthday": "3月21日 - 4月19日",
        "character": "热情开朗、勇敢直率、充满活力，喜欢冒险和挑战，做事果断有冲劲。",
        "love": "本月桃花运旺盛，单身者有望遇到心仪对象，有伴侣者感情甜蜜升温。",
        "wealth": "正财稳定，偏财小有收获，适合稳健投资，避免冲动消费。"
    }
    
    show_star_info("白羊座", test_data)
    show_goodbye()
    
    # 测试错误提示
    show_error("月份必须在 1-12 之间！")