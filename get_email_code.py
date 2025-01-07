from DrissionPage.common import Keys
import time
import re


class EmailVerificationHandler:
    def __init__(self, browser, mail_url="https://tempmail.plus"):
        self.browser = browser
        self.mail_url = mail_url

    def get_verification_code(self, email):
        username = email.split("@")[0]
        code = None

        try:
            print("正在处理...")
            # 打开新标签页访问临时邮箱
            tab_mail = self.browser.new_tab(self.mail_url)
            self.browser.activate_tab(tab_mail)

            # 输入用户名
            self._input_username(tab_mail, username)

            # 等待并获取最新邮件
            code = self._get_latest_mail_code(tab_mail)

            # 清理邮件
            self._cleanup_mail(tab_mail)

            # 关闭标签页
            tab_mail.close()

        except Exception as e:
            print(f"获取验证码失败: {str(e)}")

        return code

    def _input_username(self, tab, username):
        while True:
            if tab.ele("@id=pre_button"):
                tab.actions.click("@id=pre_button")
                time.sleep(0.5)
                tab.run_js('document.getElementById("pre_button").value = ""')
                time.sleep(0.5)
                tab.actions.input(username).key_down(Keys.ENTER).key_up(Keys.ENTER)
                break
            time.sleep(1)

    def _get_latest_mail_code(self, tab):
        print("📨 等待验证邮件到达...")
        code = None
        wait_time = 0
        while True:
            new_mail = tab.ele("@class=mail")
            if new_mail:
                if new_mail.text:
                    print("📬 收到新邮件，正在读取...")
                    tab.actions.click("@class=mail")
                    break
                else:
                    break
            time.sleep(1)
            wait_time += 1
            if wait_time % 5 == 0:  # 每5秒提示一次
                print(f"⏳ 已等待 {wait_time} 秒...")

        if tab.ele("@class=overflow-auto mb-20"):
            print("📖 正在提取验证码...")
            email_content = tab.ele("@class=overflow-auto mb-20").text
            verification_code = re.search(
                r"verification code is (\d{6})", email_content
            )
            if verification_code:
                code = verification_code.group(1)
                print(f"🔢 成功获取验证码: {code}")
            else:
                print("❌ 未能在邮件中找到验证码")

        return code

    def _cleanup_mail(self, tab):
        if tab.ele("@id=delete_mail"):
            tab.actions.click("@id=delete_mail")
            time.sleep(1)

        if tab.ele("@id=confirm_mail"):
            tab.actions.click("@id=confirm_mail")
