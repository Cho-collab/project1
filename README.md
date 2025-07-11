# project1

샘플 코드는 사용자(User), 앱(KakaoTalkApp), 서버(KakaoTalkServer)로 역할이 명확히 구분되어 있어 "응집도"가 높습니다.
각 클래스는 메시지 전송, 수신, 상태 처리 등 하나의 책임에 집중하며 단일 책임 원칙을 잘 따르고 있습니다.
"결합도"는 전반적으로 낮은 편입니다. `User`는 앱을 통해 동작하고, 앱은 서버와 직접 통신하지만 기능이 명확히 분리되어 있어 클래스 간 "느슨한 결합"을 유지합니다.
다만, 추상화나 인터페이스 없이 직접 호출하는 구조는 결합도를 중간 수준으로 만들 수 있으며, 향후 이벤트 기반 처리나 인터페이스 도입으로 개선할 수 있습니다.
종합하면, 이 코드는 높은 응집도와 낮은 결합도를 가진 구조로 객체 간 역할 분담이 잘 이루어져 있으며, 유지보수성과 확장성 면에서 안정적인 설계입니다.
