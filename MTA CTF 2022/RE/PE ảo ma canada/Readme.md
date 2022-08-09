​					![](Challenge.png)

​		Đề bài cho một file đuôi DMP, xem dung lượng của file khá lớn.

​									![](colbalt.png)

​	Mình search google thì biết đây file DMP là file được dump từ memory ra. Mình mở HXD xem qua file, thì thấy có nhiều dấu hiệu của PE File. Thực ra là mình được hint nên biết trước trong đó có file PE rồi.

​							![](dump.png)

​		Mình dump tất cả các file PE ra, sau đó dùng DIE để kiểm tra thì thấy có rất nhiều file dll và một file exe.

​							![](DIE.png)					

​		Mình thử cho vào IDA xem thử 



​							![](IDA1.png)

​		Sau một hồi phân tích tĩnh thử thì không thu được thông tin gì . Mình chợt nhớ ra đây là một file PE được dump ra từ memory nên lúc này các section đang được load theo Virtual Size và Virtual Address. Bởi vậy mình mở CFF Explorer ra và sửa đại chỉ Raw Size và Raw Address giống với Virtual Size và Virtual Address.

​				![](CFFExpplore.png)

​		Load lại vào IDA mình thấy code đã đẹp và các funtion đã hiển thị chính xác.

​						![](Funtion.png)

​		Xem xét hàm main : 

​			![](MainFunction.png)



Ở đây mình thấy chương trình kiểm tra gì đó rồi in ra Flag : **FLAG{Flag real đã bay màu}**. Mình submit thử thì thấy không đúng. Mình xem thử lại luồng bên kia 

​		![](mainFunction2.png)

​	Mình thấy có hàm StartAddress, mình mở xem thì thấy có tạo một Messagebox với tiêu đề là "Congratulation" với nội dung hiển thị là Parameter truyền vào nên đoán đây mới là luồng chính xác.

​	