import re

log_lines = [
    "2025-11-15 08:30:15 ERROR: Service unavailable (code=500)",
    "2025-11-15 10:00:00 ERROR: Access denied (permission denied)",
    "2025-11-15 11:55:10 INFO: User logged in",
    "2025-11-15 12:00:00 WARNING: Low disk space (code=999)"
]

# ОБНОВЛЕННЫЙ ПАТТЕРН
# 1. (\S+\s+\S+) - Date_Time (дата + пробел + время)
#    \s+         - Пробел-разделитель перед уровнем
# 2. ([^:]+)     - Level (уровень, все символы до двоеточия)
#    :\s+        - Разделитель (двоеточие и пробел)
# 3. (.*?)       - Message (сообщение, ленивый захват)
# 4. (\d+)       - Code (опциональный код в конце)
pattern = r"^(\S+\s+\S+)\s+([^:]+):\s+(.*?)(?:\s+\(code=(\d+)\))?$"

for line in log_lines:
    match = re.match(pattern, line)
    if match:
        # Индексы групп сместились, так как date и time теперь одна группа
        print(f"Date_Time: {match.group(1)}")
        print(f"Level:     {match.group(2)}")
        print(f"Message:   '{match.group(3)}'")
        print(f"Code:      {match.group(4)}") # None, если кода нет
        print("-" * 30)