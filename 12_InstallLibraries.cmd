:: mkdir dependencies
:: pip download -r requirements.txt -d "./dependencies"
:: tar cvfz dependencies.tar.gz dependencies

::tar zxvf dependencies.tar.gz
@ECHO OFF
cd src\req\dependencies
pip install --no-index --find-links=wheels/ -r requirements.txt
EXIT /B