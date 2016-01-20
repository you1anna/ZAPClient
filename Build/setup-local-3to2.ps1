python2 -m pip install virtualenv
python2 -m virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
cd ..\python\api\src\huddleframework
$pyfiles = get-location
$files = gci -Path $pyfiles -Include *.py -Recurse
$files | % {
		Write-Host "Converting..." $_.fullname
		python 3to2 -n $_.fullname
}
cd ..\python\api\
python zapScan.py
cd ..\..
deactivate