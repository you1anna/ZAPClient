python -m pip install virtualenv
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
cd ..\..\Huddle\Huddle-Selenium-Framework\huddleframeworksrc\framework\
python setup.py develop
cd ..\..\..\..\Huddle-ZAPClient\python-owasp-zap\
python setup.py build
cd ..\python\api\
deactivate