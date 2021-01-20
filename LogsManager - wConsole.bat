@ECHO OFF
echo [93mVerifico la presenza delle librerie necessarie...[0m
pip3 install -r requirements.txt
echo [93mAvvio LogsManager...[0m
FOR /f %%p in ('where python') do (
	@ %%p "main.py" 
)
EXIT /B