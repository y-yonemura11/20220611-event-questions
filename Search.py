def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    left = 0           # 探索範囲の左端の設定
    right = len(sorted_array) - 1           # 探索範囲の右端の設定
    while left <= right:
        mid = (left + right) // 2           # 探索する範囲の中央を計算
        if sorted_array[mid] == target_number:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif sorted_array[mid] < target_number:
            # 中央の値より大きい場合は探索範囲の左端を変更
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右端を変更
            right = mid - 1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()