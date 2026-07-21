# -*- coding: utf-8 -*-
"""
星座运势查询系统 程序总入口 main.py
串联 data、judge、show 全部子模块
开发分支：feature/main-doc
"""
import data
import judge
import show

def main():
    # 启动欢迎界面
    show.show_welcome()

    # 接收用户输入
    input_month = input("请输入出生月份：")
    input_day = input("请输入出生日期：")

    # 调用judge模块校验输入
    valid_state, tip_msg, birth_month, birth_day = judge.check_birth_input(input_month, input_day)
    if not valid_state:
        show.show_error(tip_msg)
        return

    # 计算对应星座名称
    constellation_name = judge.get_constellation(birth_month, birth_day)
    # 读取全部星座数据
    all_star_data = data.get_all_star_info()
    target_star_detail = all_star_data[constellation_name]

    # 调用show模块，彩色格式化输出星座完整信息
    show.show_star_info(constellation_name, target_star_detail)

    # 程序结束致谢界面
    show.show_goodbye()

if __name__ == "__main__":
    main()
