from logo import print_logo
import sys
import os

def main():
    print_logo()
    
    while True:
        print("\n请选择运行模式:")
        print("1. 默认模式 (自动注册新账号)")
        print("2. 切换机器码模式")
        print("3. 退出程序")
        
        choice = input("\n请输入选项 (1-3): ").strip()
        
        if choice == "1":
            print("\n启动默认模式...")
            import runpy
            runpy.run_module('cursor_pro_keep_alive', run_name='__main__')
            break
        elif choice == "2":
            print("\n启动切换机器码模式...")
            import runpy
            runpy.run_module('cursor_pro_keep_alive_update_storage_file', run_name='__main__')
            break
        elif choice == "3":
            print("\n感谢使用，再见！")
            sys.exit(0)
        else:
            print("\n❌ 无效的选项，请重新选择")

if __name__ == "__main__":
    main() 