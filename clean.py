import os
import shutil

def clean():
    """清理编译生成的文件"""
    
    # 需要删除的目录
    dirs_to_remove = ['build', 'dist', '__pycache__']
    
    # 需要删除的文件后缀
    file_patterns = ['*.spec', '*.pyc']
    
    print("开始清理...")
    
    # 删除目录
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✓ 已删除目录: {dir_name}")
            except Exception as e:
                print(f"✗ 删除目录失败 {dir_name}: {str(e)}")
    
    # 删除 .spec 和 .pyc 文件
    for pattern in file_patterns:
        for file in os.listdir('.'):
            if file.endswith(pattern.replace('*', '')):
                try:
                    os.remove(file)
                    print(f"✓ 已删除文件: {file}")
                except Exception as e:
                    print(f"✗ 删除文件失败 {file}: {str(e)}")
    
    # 清理子目录中的 __pycache__
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"✓ 已删除目录: {pycache_path}")
            except Exception as e:
                print(f"✗ 删除目录失败 {pycache_path}: {str(e)}")
    
    print("清理完成!")

if __name__ == '__main__':
    clean() 