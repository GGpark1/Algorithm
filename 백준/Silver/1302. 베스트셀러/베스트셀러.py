book_dict = dict()
N = int(input())

for _ in range(N):
    name = input()
    if name not in book_dict:
        book_dict[name] = 1
    else:
        book_dict[name] += 1

sales_counts = max(list(book_dict.values()))
tuple_book_list = list(book_dict.items())

best_seller_list = []
for i, j in tuple_book_list:
    if j == sales_counts:
        best_seller_list.append(i)

best_seller_list.sort()

print(best_seller_list[0])