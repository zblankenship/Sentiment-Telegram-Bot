$key_values = "Token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
paralleldots = 'xxxxxxxxxxxxxxxxxxxxxxxx'"
python -m pip install -r .\requirements.txt
New-Item -Path . -Name "key.env" -ItemType "file" -Value $key_values