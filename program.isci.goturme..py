print("magazaya ise qebul ")
print('Melumatlariniz duzgun daxil etmeyi unutmayin!')
ad_soyad = (input('adinizi ve soyadinizi daxil edin:'))
yasadigi_yer = input('yasadiginiz yeri daxil edin:')

if yasadigi_yer == 'baki':
  print('yasadiginiz yer gebul sertlerine uygundur') 
else:
  print('teesuf ki yasadiginiz yer qebul sertlerine uygun deyil')
dogum_ili= int(input('dogum ilinizi daxil edin:'))
if dogum_ili >= 2002:
   print('ise daxil olmaq ucun yasiniz uygun deyil !')
elif dogum_ili <= 1983:
    print('ise daxil olmaq ucun yasiniz uygun deyil!')
else:
     print('ise daxil olmaq ucun yasiniz uygundur')
aile= (input('aile veziyyetinizi qeyd edin evli yada subay :'))
if aile == "evli":
  print('ise qebul olmaginiz mumkun deyil:')
elif aile == "subay" :
    print('novbeti merheleye kece bilersiniz')
else:
    print('davam edinn')
old_job= int(input('nece magazada is tecrubesi gormusuz, sayini reqemle qeyd edin:')) 
if old_job == 1:
  print('emek haqqiniz 120 manatla balayacaq ')
elif old_job >= 2:
    print('emek haqqiniz 180 manatdan baslayacaqdir')
elif old_job == 0:
    print('emek haqqiniz 100 manatla baslayacaqdir')
else:
    print('emek haqqiniz 90 manatla baslayacaqdir')
    
 


     

