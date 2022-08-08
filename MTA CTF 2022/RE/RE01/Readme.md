![](chanllenge.png)

​		DIE chỉ ra rằng đây là một PE64

​										![](DIE.png)

​		Chạy chương trình thử: 

​														![](run1.png)

​		Chương trình in ra chuỗi flag giả, ta thử load file vào IDA64, mình thấy xuất hiện TLS Callback_0.

​													![](TLS_func.png)

​		Linh tính của mình là phải xem qua hàm TlsCallback trước

![](TLS_detail.png)

​		Mình thấy hint 'MSEC Task' nên đoán chương trình chứa flag ở đây. Tiến hành đặt breakpoint ở hàm này xem xét thử.



​								![](Flag.png)

​		Thế là flag xuất hiện, mình k biêt tác giả ra đề còn có phương pháp nào không , nhưng thấy flag rồi nên mình cũng không suy nghĩ thêm nữa.

​		**FLAG:  MSEC{my_name_is_TLS_callback_hope_you_fun!}**

​		

​		