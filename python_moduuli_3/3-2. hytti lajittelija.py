hyttiluokka = input('mikä on hyttiluokkasi?: ')

if hyttiluokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif hyttiluokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hyttiluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hyttiluokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('tätä hyttiluokkaa ei ole olemassa. katso että kirjoitit luokan isoilla kirjaimilla.')