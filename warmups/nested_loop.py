def my_method(arr, num):
    for int in arr:
        if num < int:
            print('num is not higher')
            return false

    arr = [1, 2, 3, 4, 5, 6]
    my_method(arr, 10)
    print ('no')
    my_method(arr, 4)
    print 'Yes'
