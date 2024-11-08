# Calc_Entropy
计算程序的熵值
使用PyQt5库制作的gui界面，把程序拖到gui界面上，就能看到程序熵值和对应的颜色
![image](https://github.com/user-attachments/assets/4e8ef8d5-61d2-48dd-a457-1cc553a6186f)

程序太大，请自行编译

显示颜色：update_label_color 函数根据熵值设置标签背景颜色。
熵值 < 3.0：背景色为 lightgreen
3.0 <= 熵值 < 4.0：背景色为 green
4.0 <= 熵值 < 5.0：背景色为 yellow
5.0 <= 熵值 < 6.0：背景色为 orange
6.0 <= 熵值 < 7.0：背景色为 red
熵值 >= 7.0：背景色为 darkred
