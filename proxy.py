class Server:
    def handle_request(self, request):
        return f"درخواست '{request}' با موفقیت پردازش شد."

import datetime

class LoggingProxy:
    def __init__(self, real_server):
        self._real_server = real_server

    def handle_request(self, request):
        self._log_event(f"دریافت درخواست: {request}")
        response = self._real_server.handle_request(request)
        self._log_event(f"ارسال پاسخ: {response}")
        return response

    def _log_event(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        # همچنین می‌توانید لاگ را در یک فایل ذخیره کنید
        with open("server_logs.txt", "a", encoding="utf-8") as log_file:
            log_file.write(log_message + "\n")
if __name__ == "__main__":

    server = Server()

    proxy_server = LoggingProxy(server)

    requests = [
        "درخواست اطلاعات کاربر 101",
        "ثبت سفارش جدید",
        "دریافت لیست محصولات",
    ]

    for req in requests:
        response = proxy_server.handle_request(req)
        print("پاسخ به کاربر:", response)
        print("-" * 40)
