cd ..\huddleframework
$pyfiles = get-location
$files = gci -Path $pyfiles -Recurse

$files | % {

	$containsPy = $_ -match ".py" 
	if($containsPy -contains $true)
	{	
		Write-Host "Converting..." $_.fullname
		python3 3to2 -w -n $_.fullname
	}
}