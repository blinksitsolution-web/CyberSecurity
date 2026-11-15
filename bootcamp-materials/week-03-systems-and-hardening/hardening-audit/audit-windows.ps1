# Read-only Windows lab notes for the Week 3 workstation baseline.
# This script prints settings. It does not change them.
# Run in PowerShell on the Windows VM:  powershell -ExecutionPolicy Bypass -File .\audit-windows.ps1
# Paste the output into evidence/windows-audit.txt yourself. Do not invent lines.

Write-Output "=== Read-only Windows baseline notes ==="
Write-Output ("Collected: " + (Get-Date -Format o))
Write-Output "Replace this file's output with what YOUR virtual machine printed."

Write-Output ""
Write-Output "--- Firewall profiles ---"
try {
    Get-NetFirewallProfile | Select-Object Name, Enabled | Format-Table -AutoSize | Out-String | Write-Output
} catch {
    Write-Output ("Firewall query failed: " + $_.Exception.Message)
}

Write-Output "--- Microsoft Defender status ---"
try {
    Get-MpComputerStatus |
        Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, IoavProtectionEnabled |
        Format-List | Out-String | Write-Output
} catch {
    Write-Output ("Defender query failed: " + $_.Exception.Message)
}

Write-Output "--- Local password policy (net accounts) ---"
net accounts

Write-Output "--- SMBv1 server feature (display only) ---"
try {
    Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol |
        Select-Object FeatureName, State | Format-List | Out-String | Write-Output
} catch {
    Write-Output ("SMBv1 query failed: " + $_.Exception.Message)
}

Write-Output "=== End. No settings were changed. ==="
