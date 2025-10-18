#3)  input საშუალებით შემოიტანეთ 2 რიცხვი ეს რიცხვები გარდაქმენით float შემდეგ გამოიყენეთ ამ რიცხვებზე ყველა 
# მათემატიკური ოპერაცია და შედარებები (კომენბატრებით ახსენით თითოეული 
# კოდის დეტალი რას აკეთებთ და რატომ გამოიყენეთ შესაბამისი ფუნქციები)


num1 = input("Enter the first number: ") 
num1 = float(num1) 


num2 = input("Enter the second number: ")
num2 = float(num2)  


print("Sum:", num1 + num2)              
print("Difference:", num1 - num2)      
print("Product:", num1 * num2)       
print("Division:", num1 / num2)        
print("Integer division:", num1 // num2)
print("Remainder:", num1 % num2)       
print("Exponent:", num1 ** num2)        


print("num1 == num2 ?", num1 == num2)   
print("num1 != num2 ?", num1 != num2)  
print("num1 > num2 ?", num1 > num2)     
print("num1 < num2 ?", num1 < num2)     
print("num1 >= num2 ?", num1 >= num2)  
print("num1 <= num2 ?", num1 <= num2)   
