[Setup]
AppName=Smart Data Tool
AppVersion=1.0
DefaultDirName={pf}\SmartDataTool
OutputBaseFilename=SmartDataToolInstaller
SetupIconFile=icon.ico
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\Smart Data Tool"; Filename: "{app}\app.exe"
