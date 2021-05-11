Dim threadFile, local_Path, local_File, strProgPath, envVarProccess, objFso, shApp
Set objFso = CreateObject("Scripting.FileSystemObject"):Set shApp = CreateObject( "Shell.Application" )
strProgPath = "C:\pub1\Util\"
threadFile = "Register_Schedule_Reverse.Installer.bat":local_File = strProgPath & threadFile
	if objFso.FileExists( local_File ) Then
'		shApp.ShellExecute "c:\Windows\system32\cmd.exe", "/c " & Chr(34) & local_File & Chr(34), strProgPath, "runas", 1
		shApp.ShellExecute "c:\Windows\system32\cmd.exe", "/c " & Chr(34) & local_File & Chr(34), strProgPath, "runas", 0
'	else
'		MsgBox "File: " & local_File & " is NOT Exist"
end if
