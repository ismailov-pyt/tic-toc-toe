from random import randint
tas=['1','2','3','4','5','6','7','8','9']
for i in [0,1]:
	print(i)
a1=a2=a3=a4=a5=a6=a7=a8=a9=''
print(str(tas[randint(0,8)]))
print(' ___________')
print('| 1 | 2 | 3 |')
print(' ___________')
print('| 4 | 5 | 6 |')
print(' ___________')
print('| 7 | 8 | 9 |')
print(' ___________')
loop=[0,1]

while True:
	sikl=0
	
    


	for i in loop:
		if i==0:
			
			while True:
				
				user=input('Joylashuvni kiriting(1-o`yinchi)>>> ')
				if user=='1' and a1=='':
					a1+='x'
					sikl+=1
					
					break
				if user=='2' and a2=='':
				    a2+='x'
				    sikl+=1
				    break
				if user=='3' and a3=='':
					a3+='x'
					sikl+=1
					break
				if user=='4' and a4=='':
					a4+='x'
					sikl+=1
					break
				if user=='5' and a5=='':
				    a5+='x'
				    sikl+=1
				    break
				if user=='6' and a6=='':
					a6+='x'
					sikl+=1
					break
				if user=='7' and a7=='':
					a7+='x'
					sikl+=1
					break
				if user=='8' and a8=='':
				    a8+='x'
				    sikl+=1
				    break
				if user=='9' and a9=='':
					a9+='x'
					sikl+=1
					break

				if user=='1' or user=='2' or user=='3'or user=='4' or user=='5' or user=='6'or user=='7' or user=='8' or user=='9':
				    print('BU joy band')
				    
				else:
					print('Xatolik!!!')
		print(' ___________'+'\n'+'| ' + a1 + ' | ' + a2 + ' | ' + a3 + ' |'+'\n'+' ___________'+'\n'+'| '+a4+' | '+a5+' | '+a6+' |'+'\n'+' ___________'+'\n'+'| '+a7+' | '+a8+' | '+a9+' |'+'\n'+' ___________')
		
		if a1==a2==a3=='x'or a1==a4==a7=='x' or a3==a6==a9=='x' or a7==a8==a9=='x' or a1==a5==a9=='x' or a4==a5==a6=='x' or a2==a5==a8=='x' or a3==a5==a7=='x':
			print('Birinchi o`yinchi yutti...')
			break
		if a1==a2==a3=='o'or a1==a4==a7=='o' or a3==a6==a9=='o' or a7==a8==a9=='o' or a1==a5==a9=='o' or a4==a5==a6=='o' or a2==a5==a8=='o' or a3==a5==a7=='o':
			print('Ikkinchi o`yinchi yutti...')
			break		
		if i==0:
			
			while True:
				
				user2=input('Joylashuvni kiriting(2-o`yinchi)>>> ')
				if user2=='1' and a1=='':
					a1+='o'
					sikl+=1
					
					break
				if user2=='2' and a2=='':
				    a2+='o'
				    sikl+=1
				    break
				if user2=='3' and a3=='':
					a3+='o'
					sikl+=1
					break
				if user2=='4' and a4=='':
					a4+='o'
					sikl+=1
					break
				if user2=='5' and a5=='':
				    a5+='o'
				    sikl+=1
				    break
				if user2=='6' and a6=='':
					a6+='o'
					sikl+=1
					break
				if user2=='7' and a7=='':
					a7+='o'
					sikl+=1
					break
				if user2=='8' and a8=='':
				    a8+='o'
				    sikl+=1
				    break
				if user2=='9' and a9=='':
					a9+='o'
					sikl+=1
					break

				if user2=='1' or user2=='2' or user2=='3'or user2=='4' or user2=='5' or user2=='6'or user2=='7' or user2=='8' or user2=='9':
				    print('BU joy band')
				    
				else:
					print('Xatolik!!!')
		        
		        

          
		print(' ___________'+'\n'+'| ' + a1 + ' | ' + a2 + ' | ' + a3 + ' |'+'\n'+' ___________'+'\n'+'| '+a4+' | '+a5+' | '+a6+' |'+'\n'+' ___________'+'\n'+'| '+a7+' | '+a8+' | '+a9+' |'+'\n'+' ___________')
		if a1==a2==a3=='x'or a1==a4==a7=='x' or a3==a6==a9=='x' or a7==a8==a9=='x' or a1==a5==a9=='x' or a4==a5==a6=='x' or a2==a5==a8=='x' or a3==a5==a7=='x':
			print('Birinchi o`yinchi yutti...')
			break
		if a1==a2==a3=='o'or a1==a4==a7=='o' or a3==a6==a9=='o' or a7==a8==a9=='o' or a1==a5==a9=='o' or a4==a5==a6=='o' or a2==a5==a8=='o' or a3==a5==a7=='o':
			print('Ikkinchi o`yinchi yutti...')
			break		



