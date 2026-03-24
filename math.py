x = int(input("請輸入 x："))
opt = input("請輸入運算符號 (+, -, *, /)：")
y = int(input("請輸入 y："))

# 先預設 Result 為 None，避免 NameError
Result = None

if (opt == "/" and y == 0):
    print("錯誤：除數不能為 0")
else:
    match opt:
        case "+":
            Result = x + y
        case "-":
            Result = x - y
        case "*":
            Result = x * y
        case "/":
            Result = x / y
        case _: # 當輸入不是 +-*/ 時執行這裡
            print(f"錯誤：不支援的符號 '{opt}'")

# 只有在 Result 被成功計算（不是 None）時才列印結果
if Result is not None:
    # 注意這裡要把 opt 放進大括號 {opt} 才會顯示你輸入的符號
    print(f"{x} {opt} {y} 的結果是 {Result}")
