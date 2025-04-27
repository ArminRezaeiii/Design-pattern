class WebPage:
    def __init__(self, content):
        self.content = content

    def display(self):
        return self.content


class AuthRequired(WebPage):
    def __init__(self, page, is_authenticated):
        self.page = page
        self.is_authenticated = is_authenticated

    def display(self):
        if self.is_authenticated:
            return self.page.display()
        else:
            return "لطفا وارد سیستم شوید تا دسترسی به این صفحه ممکن باشد."

class SecurePage(WebPage):
    def __init__(self, page, is_secure):
        self.page = page
        self.is_secure = is_secure

    def display(self):
        if self.is_secure:
            return self.page.display()
        else:
            return "لطفا از یک ارتباط امن (HTTPS) استفاده کنید."




page1 = WebPage("این یک صفحه عمومی است.")
page2 = WebPage("این صفحه فقط برای کاربران وارد شده است.")
page3 = WebPage("این صفحه فقط در صورت استفاده از HTTPS قابل دسترسی است.")



secure_page = SecurePage(page3, is_secure=True)
auth_required_page = AuthRequired(page2, is_authenticated=False)



print(page1.display())  # خروجی: این یک صفحه عمومی است.
print(auth_required_page.display())  # خروجی: لطفا وارد سیستم شوید تا دسترسی به این صفحه ممکن باشد.
print(secure_page.display())  # خروجی: این صفحه فقط در صورت استفاده از HTTPS قابل دسترسی است.
