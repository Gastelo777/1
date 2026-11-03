"""Выводит текущую дату и время по Астане и сообщение о запуске Profitscape."""

from datetime import datetime, timedelta, timezone

try:
    from zoneinfo import ZoneInfo

    # С 1 марта 2024 года весь Казахстан, включая Астану, живёт по UTC+5.
    ASTANA_TZ = ZoneInfo("Asia/Almaty")
except Exception:
    # Если база часовых поясов недоступна (например, Windows без пакета tzdata),
    # используем фиксированное смещение UTC+5.
    ASTANA_TZ = timezone(timedelta(hours=5), "Астана")


def main() -> None:
    now = datetime.now(ASTANA_TZ)
    print(f"Дата и время в Астане: {now:%d.%m.%Y %H:%M:%S} (UTC{now:%z})")
    print("Profitscape запущен")


if __name__ == "__main__":
    main()
