Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "LogsManager.exe" & chr(34), 0
Set WshShell = Nothing