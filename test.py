class User:
    def __init__(self, name, app=None):
        self.name = name
        self.app = app

    def send_message(self, message, recipient):
        print(f"[{self.name}] 메시지를 입력하고 전송 버튼을 클릭합니다.")
        self.app.send_message(message, recipient)

    def receive_notification(self, message):
        print(f"[{self.name}] 새 메시지 알림을 받았습니다: '{message}'")
        self.read_message(message)

    def read_message(self, message):
        print(f"[{self.name}] 메시지를 열람합니다: '{message}'")
        self.app.send_read_receipt()


class KakaoTalkApp:
    def __init__(self, user, server):
        self.user = user
        self.server = server
        user.app = self

    def send_message(self, message, recipient_user):
        print(f"[{self.user.name}의 앱] 서버에 메시지를 전송합니다.")
        self.server.deliver_message(message, self.user, recipient_user)

    def receive_message(self, message, sender):
        print(f"[{self.user.name}의 앱] {sender.name}로부터 메시지를 받았습니다.")
        self.user.receive_notification(message)

    def send_read_receipt(self):
        print(f"[{self.user.name}의 앱] 서버에 읽음 상태를 전송합니다.")
        self.server.update_read_status(self.user)


class KakaoTalkServer:
    def deliver_message(self, message, sender, recipient):
        print("[서버] 메시지를 수신하고 수신자 앱에 푸시 알림을 보냅니다.")
        recipient.app.receive_message(message, sender)

    def update_read_status(self, reader):
        print(f"[서버] {reader.name}의 읽음 상태를 발신자에게 업데이트합니다.")


# 시뮬레이션 실행
server = KakaoTalkServer()

# 사용자와 앱 생성
user_a = User("사용자 A")
user_b = User("사용자 B")

app_a = KakaoTalkApp(user_a, server)
app_b = KakaoTalkApp(user_b, server)

# 메시지 전송 시뮬레이션
user_a.send_message("안녕! 잘 지내?", user_b)
