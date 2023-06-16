import base64
import secrets 
import string 
import gzip 
flag ="HNF23{REDACTED}"
def asd (OO0000OO00O0O0O0O ):
    return OO0000OO00O0O0O0O .encode ('ascii')
def qw (OOOOO0OO0O0OO0O00 ):
    return gzip .compress (OOOOO0OO0O0OO0O00 )
def sFAF (O0OO00OO0O0OO00OO ):
    return O0OO00OO0O0OO00OO .decode ('ascii')
def dsjfdhh (OOOO0OO000OOO00O0 ):
    return base64 .b64encode (OOOO0OO000OOO00O0 )
def adsads (OOO0000OO000OOO00 ):
    OOO000OOO00O0OOOO ="ins + 2 - 2 + 32 + 64 + 128 + 256"
    OO000OOO0OO0O0O00 =secrets .choice (string .ascii_letters )
    eval (OOO000OOO00O0OOOO )
    return OOO000OOO00O0OOOO ,OO000OOO0OO0O0O00 
def sldsgffs (OOOO0000000O0000O ):
    O000O0000OOOO00O0 =asd (OOOO0000000O0000O )
    OOOOO0OOOOO0O0OOO =dsjfdhh (O000O0000OOOO00O0 )
    OO00OO00OOOOO0O00 =sFAF (OOOOO0OOOOO0O0OOO )
    for _OO00OO00O00O0OO00 in range (32 ):
        OO00OO00OOOOO0O00 +=adsads (_OO00OO00O00O0OO00 )[1 ]
    OO00OO00OOOOO0O00 =asd (OO00OO00OOOOO0O00 )
    return qw (OO00OO00OOOOO0O00 )
def sgdsgds (OOOO0O00O00OOOOO0 ):
    O0O0000O0O0OOO0O0 =open ('output.txt','wb')
    O0O0000O0O0OOO0O0 .write (OOOO0O00O00OOOOO0 )
    O0O0000O0O0OOO0O0 .close ()
sgdsgds (sldsgffs (flag ))
