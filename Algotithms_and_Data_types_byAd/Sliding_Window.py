# Sliding Window(Техника скользящего окна)
# Использует два указателя на диапазон(окно)
# Двигает границы по необходимости
# Использует множество для хранения уникальных символов

# Пример: длина наибольшей подстроки
def lengthoflongestsubstring(s: str) -> int:
    if not s:
        return 0
    max_len_substr = 0
    left = 0
    uniq_set = set()
    for right in range(len(s)):
        while s[right] in uniq_set:
            uniq_set.remove(s[left])
            left += 1
        uniq_set.add(s[right])
        max_len_substr = max(max_len_substr, right - left + 1)
        #если указатели находятся на одной и той же позиции
    return max_len_substr

text = "abcdabc"
print(lengthoflongestsubstring(text))