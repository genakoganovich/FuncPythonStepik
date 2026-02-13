def analyze_logs(log_data: str) -> list[int]:
    """
    Анализирует многострочный лог и возвращает отсортированный
    список кодов ошибок по заданным правилам.
    """
    # 1. Разбейте log_data на строки
    lines = log_data.splitlines()

    # 2. Постройте конвейер из filter, map и sorted
    #    для выполнения всех условий задачи.

    # Напишите ваш код здесь
    from datetime import datetime
    import re

    def parse_line(line: str) -> tuple:
        pattern = r"^(\S+\s+\S+)\s+([^:]+):\s+(.*?)(?:\s+\(code=(\d+)\))?$"
        match = re.match(pattern, line)
        date_time = datetime.fromisoformat(match.group(1))
        code = int(match.group(4))
        return date_time, code


    return sorted(list(map(lambda x: x[1],
                    filter(lambda x: 8 <= x[0].hour < 12,
                        map(parse_line,
                            filter(lambda line: "(code=" in line,
                                filter(lambda line: "ERROR" in line,
                                lines
        )))))), reverse=True)


def main():
    log_data = """2025-11-15 08:30:15 ERROR: Service unavailable (code=500)
2025-11-15 09:15:40 ERROR: Not found (code=404)
2025-11-15 11:55:10 INFO: User logged in
2025-11-15 14:05:00 ERROR: Service overloaded (code=503)
2025-11-15 10:00:00 ERROR: Access denied (permission denied)
    """
    print(analyze_logs(log_data))


if __name__ == "__main__":
    main()
