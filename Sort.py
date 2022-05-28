def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    # return用　空の配列
    array_return = []
    # 一時保存用
    array_save = []
    
    def sort2(array):
        # 配列の先頭を基準値とする
        pivot = array[0]
        
        end = len(array) - 1  #末端のindex 分割する位置のindexの保存
        for i in range(len(array)):
            if i >= end:   # 検索がぶつかっていないか確認
                break
            if array[i] < pivot:   # 先頭から検索
                continue
            while pivot <= array[end]:   # 末端から探索
                end = end - 1
                if i >= end:   # 検索がぶつかっていないか確認
                    break
            array[i], array[end] = array[end], array[i]   # 値の入れ替え
        
        array_return = [array[:end], array[end:]]   # グループを分けて保存
        return array_return
    
    array_save.append(array)   # 初期配列を追加
    
    while len(array_save) != 0:   # 一時保存用の配列の長さが0になるまでソートする
        array_before = array_save[0]   # array_beforeにソートする配列を代入
        array_save.pop(0)   # ソートする配列をarray_saveから削除
        if len(array_before) != 1:
            array_sorted = sort2(array_before)
            if array_sorted[0] != []:   # ソートして分割されたとき
                array_save.insert(0, array_sorted[1])
                array_save.insert(0, array_sorted[0])
            if array_sorted[0] == []:   # もとから配列が昇順にソートされていた場合
                 array_return.extend(array_sorted[1])
        else:   # 要素が一つの場合はreturn用配列に追加
            array_return.extend(array_before)

    return array_return
    # ここまで記述

if __name__ == '__main__':
    main()