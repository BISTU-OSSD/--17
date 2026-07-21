from show import print_section, print_centered

# 测试数据
star_info = {
    "name": "金牛座",
    "character": "性格温和，做事踏实",
    "love": "近期桃花运稳定",
    "money": "财运平稳无大额支出"
}

# 调用打印函数，补上颜色参数
print_centered("十二星座运势")
print_section("性格分析", star_info["character"], "red", "white")
print_section("感情运势", star_info["love"], "yellow", "white")
print_section("财富运势", star_info["money"], "green", "white")