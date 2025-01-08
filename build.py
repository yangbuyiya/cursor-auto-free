import os
import platform
import site
import sys

def build():
    # 获取 site-packages 路径
    site_packages = site.getsitepackages()[0]
    
    # 检查实际存在的文件
    existing_files = [
        'main.py',
        'browser_utils.py',
        'cursor_pro_keep_alive.py',
        'cursor_pro_keep_alive_update_storage_file.py',
        'get_email_code.py',
        'cursor_auth_manager.py',
    ]
    
    # 基础打包参数
    base_command = [
        'pyinstaller',
        '--noconfirm',
        '--clean',
        '--name=CursorPro',
        # 添加所有必要的隐藏导入
        '--hidden-import=selenium',
        '--hidden-import=webdriver_manager',
        '--hidden-import=DrissionPage',
        '--hidden-import=DrissionPage.common',  # 添加具体的子模块
        '--hidden-import=DrissionPage.common.Keys',
        '--hidden-import=schedule',
        # 添加 DrissionPage 相关文件
        f'--add-data={os.path.join(site_packages, "DrissionPage")}:DrissionPage',
    ]
    
    # 添加数据文件
    if os.path.exists('turnstilePatch'):
        base_command.append('--add-data=turnstilePatch:turnstilePatch')
    
    # 添加其他必要的Python文件
    for file in existing_files:
        if os.path.exists(file):
            base_command.append(f'--add-data={file}:.')
    
    # 优化选项
    base_command.extend([
        '--noupx',  # 禁用UPX压缩以提高兼容性
        '--clean',  # 清理临时文件
        '--collect-all=DrissionPage',  # 收集所有 DrissionPage 相关文件
    ])
    
    # 根据操作系统添加特定参数
    if platform.system() == 'Darwin':  # macOS
        base_command.extend([
            '--windowed',  # macOS 图形界面
            '--target-arch=x86_64',  # 指定目标架构
        ])
    elif platform.system() == 'Windows':
        base_command.extend([
            '--windowed',
            '--runtime-tmpdir=.',  # 运行时临时文件存放在程序目录
        ])
    
    # 添加主程序文件
    base_command.append('main.py')
    
    # 执行打包命令
    os_command = ' '.join(base_command)
    print(f"开始打包...")
    print(f"执行命令: {os_command}")
    
    # 执行打包
    result = os.system(os_command)
    
    if result == 0:
        print("打包成功!")
        print(f"可执行文件位于: {os.path.join('dist', 'CursorPro')}")
    else:
        print(f"打包失败,错误代码: {result}")

if __name__ == '__main__':
    build() 