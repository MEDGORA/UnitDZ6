class task :

    array1 = [1, 2, 3]
    array2 = [1, 2, 3, 4]


    def task(array1, array2):
        

        def Medium(array): 
            if not isinstance(array,list):
                raise TypeError("ожидался тип list")
            M = 0
            for i in range(0, len(array)) :
                M = M + array[i]
            if len(array) == 0 :
                return "Пустой список"
            else :
                return M/len(array)
            

        if not isinstance(array1,list):
                raise TypeError("ожидался тип list")
        if not isinstance(array2,list):
                raise TypeError("ожидался тип list")
        if len(array1) == 0 :
                return "Первый список пустой"
        if len(array2) == 0 :
                return "Второй список пустой"
        if Medium(array1) > Medium(array2) :
            return "Первый список имеет большее среднее значение"
        elif Medium(array1) < Medium(array2) :
            return "Второй список имеет большее среднее значение"
        else :
            return "Средние значения равны"


    print(task(array1=array1, array2=array2))