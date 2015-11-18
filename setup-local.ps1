cd D:\dev\ZAPClient\python\api
python2 -m pip install virtualenv
python2 -m virtualenv env
.\env\Scripts\activate
pip install -r ..\..\requirements.txt
cd .\python\api
python test.py