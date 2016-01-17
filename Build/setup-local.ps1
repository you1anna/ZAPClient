$root = get-location
python2 -m pip install virtualenv
python2 -m virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
cd ..\python\api\
python zapScan.py
cd ..\..
deactivate