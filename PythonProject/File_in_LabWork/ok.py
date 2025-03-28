# # Writing file 1
# with open('file1.txt', 'r', encoding='utf-8') as file:
#     content = file.read()  # Читаем содержимое файла
#     print(content)  # Выводим текст на экран
#
#
# # Sum in the file string 2
# def sring_sum(counter=0):
#     with open('file1.txt', 'r', encoding='utf-8') as file2:
#         for i in file2:
#             counter += 1
#
# print(sring_sum())
#
# 3
def word_search(word):
    with open('file1.txt', 'r', encoding='utf-8') as file3:
        for i_string in file3:
            if word in i_string:
                return f"Yes this word has in the file {word}"
            else:
                return None


enter = input()
print(word_search(enter))
#
# 4
# def change_word(old_word, new_word):
#     with open('file1.txt', 'r', encoding='utf-8') as file:
#         content = file.read()
#
#     new_content = content.replace(old_word, new_word)
#
#     with open('file1.txt', 'w', encoding='utf-8') as file:
#         file.write(new_content)
#
#     return f'Слово "{old_word}" заменено на "{new_word}"'
#
#
# enter_word, enter_word2 = input(), input()
# print(change_word(enter_word, enter_word2 ))