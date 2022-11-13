# WHILE LOOP PRACTICE  
#  a=True;
# while(a):
#     a=False;
#     print("Inside While Loop")
#     if(a==False):
#         print("the value of a is :",a);
#         a=False;
#     else:
#         print("the value of a is :",a);

# FOR LOOP PRACTICE
# print("List Iteration");
# l=["asad","mian-wali","hassaan",8,3]
# for i in l:
#     if(i==8):
#         i="shah"

# for i in range(0,5):
#     if i==2:
#         l[i]="shah"


# for i in l:
#     print(i)
# TUPLE PRACTICE
# print("List Iteration Using tuple");
# l=("asad","mian-wali","hassaan",8,3,8.4,'j');
# for i in l:
#     l[i]="dawood";


# statement="geeksforgeeks"
# for character in statement:
#     if(character=='s' or character=='e'):
#         continue
#     print("Current Letter is ",character)
# statement="geeksforgeeks"

# for character in statement:
#     if(character=='s' or character=='e'):
#         break
#     print("Current Letter is ",character)

def print_fun(a,b):
    print("Inside The function",a,b);


print("Outside Function");
a="asad";
b="mina wali";
print_fun(a,b);

