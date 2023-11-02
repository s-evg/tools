def declination_days(self, days: int) -> str:
    """Правильное склонение для слова «день»"""

    text_day = ""

    if days % 10 == 1 and days % 100 != 11:
        text_day += "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        text_day += "дня"
    else:
        text_day += "дней"

    return text_day


def levenstein(self, A: str, B: str) -> int:
    """Расчёт расстояния Левенштейна (редакционного расстояния"""

    F = [[i + j if i*j == 0 else 0 for j in range(len(B) + 1)]
         for i in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])

    return F[len(A)][len(B)]
