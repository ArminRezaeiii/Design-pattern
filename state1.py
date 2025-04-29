from abc import ABC, abstractmethod


class PrintState(ABC):
    @abstractmethod
    def print_text(self, text: str):
        pass


class NormalState(PrintState):
    def print_text(self, text: str):
        print("جمله به صورت معمولی:")
        print(text)


class ReverseState(PrintState):
    def print_text(self, text: str):
        print("جمله به صورت معکوس:")
        print(text[::-1])


class TextContext:
    def __init__(self, state: PrintState):
        self.state = state

    def set_state(self, state: PrintState):
        self.state = state

    def display(self, text: str):
        self.state.print_text(text)


if __name__ == "__main__":
    sentence = input("لطفاً یک جمله وارد کنید: ")

    print("چگونه جمله چاپ شود؟")
    print("1. معمولی")
    print("2. معکوس")
    choice = input("انتخاب شما (1 یا 2): ")

    # تنظیم وضعیت بر اساس انتخاب کاربر
    if choice == "1":
        state = NormalState()
    elif choice == "2":
        state = ReverseState()
    else:
        print("ورودی نامعتبر! پیش‌فرض: معمولی")
        state = NormalState()

    context = TextContext(state)
    context.display(sentence)
