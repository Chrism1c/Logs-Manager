title MyBatch
nircmd.exe win hide ititle "MyBatch" cmdwait 0
@ECHO OFF
FOR /f %%p in ('where pythonw') do (
	@ %%p "main.py" 
)
EXIT /B