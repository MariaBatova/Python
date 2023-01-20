# 1. Напишите программу вычисления арифметического
#   выражения заданного строкой. Используйте операции
#   +,-,/,* приоритет операций стандартный.
#   * Добавьте скобки,  приоритет операций меняется.

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


def calculator(new_lst):

    for i, val in enumerate(new_lst):
        if isinstance(val, list):
            new_lst[i] = calculator(val)

    index_lst = [i for i, val in enumerate(new_lst) if val in "*/"]

    while index_lst:
        index_op = index_lst[0]
        a, b, c = new_lst[index_op - 1: index_op + 2]
        new_lst.insert(index_op - 1, actions[b](a, c))
        del new_lst[index_op: index_op + 3]
        index_lst = [i for i, val in enumerate(new_lst) if val in "*/"]

    while len(new_lst) > 1:
        a, b, c = new_lst[:3]
        del new_lst[:3]
        new_lst.insert(0, actions[b](a, c))

    return new_lst[0]


def cut(ls):
    lst = []
    index_ = 0

    while index_ < len(ls):
        if ls[index_] == "(":
            end = ls.index(')')
            lst.append(ls[index_ + 1:end])
            index_ = end
        else:
            lst.append(ls[index_])
        index_ += 1

    return lst

user_ls = input('...').split()
print(calculator(cut(user_ls)))

# --------Вариант 2------------
# Ищем скобки, обосабливаем в списки


# def parse(exp_1):
#     pr_list = []
#     i = 0

#     while i < len(exp_1):
#         if exp_1[i] == "(":
#             # Если дальше, с текущего индекса,
#             # есть ещё открывающая скобка
#             # вызываем рекурсивно parse
#             if "(" in exp_1[i + 1:]:
#                 exp_1 = exp_1[:i + 1] + parse(exp_1[i + 1:])
#             n_2 = exp_1.index(")", i)
#             pr_list.append(exp_1[i + 1: n_2])
#             i = n_2
#         else:
#             pr_list.append(exp_1[i])
#         i += 1
#     return pr_list


# # Результирующая функция
# # TODO доработать
# def decision(final_list: list):

#     # Проверка на список, раскрытие скобок
#     for i, v in enumerate(final_list):
#         if isinstance(v, list):
#             # Если список, вызываем рекурсивно decision
#             final_list[i] = decision(v)

#     # Получение индексов приоритетных операций
#     ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

#     # Работа с приоритетными операциями
#     while ind_list:
#         k = ind_list[0]
#         a, s, b = final_list[k - 1: k + 2]
#         final_list.insert(k - 1, actions[s](a, b))
#         del final_list[k:k + 3]
#         ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

#     # Работа с оставшимися операциями
#     while len(final_list) > 1:
#         a, s, b = final_list[:3]
#         del final_list[:3]
#         final_list.insert(0, actions[s](a, b))

#     return final_list[0]


# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# # exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
# # exp = "( 12 + 8 ) * 3 - 11 / 2".split()
# # exp = "11 / 2 - ( 12 + 8 ) * 3".split()
# # exp = "5 + 11 / 2 - ( 12 + 8 ) * 3 - 12".split()
# # exp = "4 * ( 3 - 1 ) / ( 9 - 7 ) * -1".split()
# # exp = "8 + 2 * 4 + ( 6 + ( 2 - 3 * 7 + ( 77 - 11 ) ) * 2 )".split()

# print(parse(exp))
# print(decision(parse(exp)))
