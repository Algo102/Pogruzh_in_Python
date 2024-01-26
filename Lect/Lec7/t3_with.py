# # старый вариант записи
# with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
#         open('text.txt', 'rb') as f2, \
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# другой вариант в современном пайтоне
with (
        open('text_data.txt', 'r+', encoding='utf-8') as f1,
        open('text.txt', 'rb') as f2,
        open('data.txt', 'r', encoding='utf-8', errors='replace') as f3,
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f4,
        open('data.txt', 'r', encoding='utf-8', errors='ignore') as f5
):
    print(list(f1))
    print(list(f2))
    print(list(f3))
    print(list(f4))
    print(list(f5))