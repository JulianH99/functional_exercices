def order_list(list):
    if not list:
        return True
    if len(list) == 1:
        return True
    if list[0]<= list[1] and order_list(list[2:]):
        return True

if __name__ == '__main__':
    print(order_list([1,2,4,3]))
