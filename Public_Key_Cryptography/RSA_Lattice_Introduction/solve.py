from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes, bytes_to_long

e = 127 # kinda small -> small public key exponent attack

c1 = 2084227311578896504443456891135149636502594170996387889165463586461424725059541533787767041288429738064580955622451305616498186131307715129465784375455365768772957374127432690792899122124637176422529566934586476544916325439742396928355234712078183
c2 = 2089345450675350619564678004237958808781665154806166982467914729811172246521053196269736493675888244684173898988722302290793814087306806212626014865440389101781291949058853550159423562152992240869808574085962263942173316863362277246322130097359903249313
c3 = 15351988337964905099701960376347076532439043589617467841763029200910162258670083394997893897566293618070669709960876401857858929595090590610409163098252906678940270348578645367087079347216129233790173543224953780408040213693490500724979084761978285646999197843456
c4 = 27904208858505919506689042950498726643957813119400643293322771534900822430923585848781848455603612081226575100801226570484212026594858252089217840328837906708276016306114842897236574701434742246311142664328247890170520592851161647470983489359620795002699
c5 = 14562438053393942865563565506076319964337086564418653275680839364685346358348263872708128968423412681687735816462730409112745256517215618953897227627256898533454858045297931958376394955610471867756244498725191655684274134657700794939801031701760045360349184
c6 = 37370666535363066168961624931547694539547602092327751979114535130065929115448532953082477972777170290304404725670126936586698604529648793581659263060970546938259944838952911170478265448614822495177677220252704340545251785434955476627944717241828329
c7 = 57018830572739461491984788995673407709179639540390781558806685226845173001582252740946299992152591496992831944316269907785235915676185879264232465783672876342034636885982343764812696958235155060812119686263202672834115657789006658553081283546825372990992701071
c8 = 45667206025566800148122417818312587397117202643844088800399634507595677539812531804389800633373563635203026530295808267186537869501854999997585813165610459945099323041449890076258008953903360989998622098817497527261455918497690247104725594122565082035057621175773
c9 = 1686227313539318647886505059139335446746996624220331975878146712709645794810888946761963350628222465151134851313061316471360362284419753231478405415985364477239725795743107788714671289354822510203766481055710075778057712258940862586529599570943303841410139029504
c10 = 341849165158053526832505863192782931224162822759788612832891748659486026106737910383076021602844922593096922368623753010447251025423582399396141954459468286768770464472831982875580635659918156592765109749350304246573018358473129678989
c11 = 5112410579669852183534608382871115572785704026088086397778432135886054190982581109427995967742224987294310956529550255351980372648223511404048486808382051821395722995189698471430744248012819713379428438493366462166096818135752055667353488388471305370330810546875

print(long_to_bytes(int(iroot(c1, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c2, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c3, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c4, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c5, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c6, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c7, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c8, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c9, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c10, 127)[0])).decode(), end = '')
print(long_to_bytes(int(iroot(c11, 127)[0])).decode(), end = '')
