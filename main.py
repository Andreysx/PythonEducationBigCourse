# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# data = [25, -42, 146, 73, -100, 12]
# print(list(map(str, data)))
# print(max(data, key=lambda x: -x))
# print(*filter(lambda x: not x[0].startswith('__'), globals().items()))

#
# data = {2, 4, 4, 6, 8, 10, 12}
# res1 = {None: item for item in data if item > 4}
# res2 = (item for item in data if item > 4)
# res3 = [[item] for item in data if item > 4]
# print(res1, res2, res3)


# def gen(a: int, b: int) -> str:
#     if a > b:
#         a, b = b, a
#     for i in range(a, b + 1):
#         yield str(i)
#
#
# for item in gen(10, 1):
#     print(f'{item = }')
