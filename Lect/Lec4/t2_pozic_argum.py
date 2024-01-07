# Позиционные и ключевые параметры
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3) # TypeError: т.к. последний не ключевой аргумент
combined_example(1, 2, kwd_only=3) # все ок, т.к. м.б. и позиционы   и ключевой
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # ошибка, т.к. первый не ключевой аргумент