pwd = 'a123456'
i = 3 #剩餘次數
while i > 0:
	ans = input('請輸入密碼：')
	if pwd == ans:
		print('登陸成功')
		break
	else:
		i = i - 1
		print('密碼錯誤！您還有', i, '次機會')





	
	
	