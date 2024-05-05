'''1.Createastringcontaininganinteger,thenconvertthatstringinto
anactualintegerobjectusingint().Testthatyournewobjectis
anumberbymultiplyingitbyanothernumberanddisplayingthe
result.
2.Repeatthepreviousexercise,butuseafloating-pointnumberand
float().
3.Createastringobjectandanintegerobject,thendisplaythemside
by-sidewithasingleprintstatementbyusingthestr()function.
4.Writeascriptthatgetstwonumbersfromtheuserusingthe
input()functiontwice,multipliesthenumberstogether,and
displaystheresult.Iftheuserenters2and4,yourprogramshould
printthefollowingtext:
Theproductof2and4is8.0. '''
prompt_1st_num = input('Enter a number: ')
prompt_2nd_num =input('Enter another number: ') 
product_of_num= float(prompt_1st_num ) *float(prompt_2nd_num )
print('The product of ' + prompt_1st_num+' and '+prompt_2nd_num + ' is ' + str(product_of_num))