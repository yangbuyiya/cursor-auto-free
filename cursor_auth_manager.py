import sqlite3
import os


class CursorAuthManager:
    """Cursor认证信息管理器"""

    def __init__(self, browser=None):
        self.browser = browser
        # 判断操作系统
        if os.name == "nt":  # Windows
            self.db_path = os.path.join(
                os.getenv("APPDATA"), "Cursor", "User", "globalStorage", "state.vscdb"
            )
        else:  # macOS
            self.db_path = os.path.expanduser(
                "~/Library/Application Support/Cursor/User/globalStorage/state.vscdb"
            )

    def update_auth(self, email=None, access_token=None, refresh_token=None):
        """
        更新Cursor的认证信息
        
        Args:
            email: 新的邮箱地址
            access_token: 新的访问令牌
            refresh_token: 新的刷新令牌
            
        Returns:
            bool: 是否成功更新
        """
        updates = []
        # 登录状态
        updates.append(("cursorAuth/cachedSignUpType", "Auth_0"))

        if email is not None:
            updates.append(("cursorAuth/cachedEmail", email))
        if access_token is not None:
            updates.append(("cursorAuth/accessToken", access_token))
        if refresh_token is not None:
            updates.append(("cursorAuth/refreshToken", refresh_token))

        if not updates:
            print("没有提供任何要更新的值")
            return False
            
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for key, value in updates:
                # 检查键是否存在
                check_query = "SELECT COUNT(*) FROM itemTable WHERE key = ?"
                cursor.execute(check_query, (key,))
                if cursor.fetchone()[0] == 0:
                    # 键不存在，执行插入
                    insert_query = "INSERT INTO itemTable (key, value) VALUES (?, ?)"
                    cursor.execute(insert_query, (key, value))
                else:
                    # 键存在，执行更新
                    update_query = "UPDATE itemTable SET value = ? WHERE key = ?"
                    cursor.execute(update_query, (value, key))

                if cursor.rowcount > 0:
                    print(f"成功更新 {key.split('/')[-1]}")
                else:
                    print(f"未找到 {key.split('/')[-1]} 或值未变化")

            conn.commit()
            return True

        except sqlite3.Error as e:
            print("数据库错误:", str(e))
            return False
        except Exception as e:
            print("发生错误:", str(e))
            return False
        finally:
            if conn:
                conn.close()

    def login(self, email, password):
        """登录功能"""
        try:
            # 实现登录逻辑
            pass
        except Exception as e:
            print(f"登录失败: {str(e)}")
            return False
            
    def register(self, email, password):
        """注册功能"""
        try:
            # 实现注册逻辑
            pass
        except Exception as e:
            print(f"注册失败: {str(e)}")
            return False
            
    def verify_email(self, email, code):
        """验证邮箱"""
        try:
            # 实现邮箱验证逻辑
            pass
        except Exception as e:
            print(f"邮箱验证失败: {str(e)}")
            return False
