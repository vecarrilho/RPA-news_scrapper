
# Informations

API made to search a sentence in a news website, generating a xlsx file with titles, descriptions, filenames, dates.

* Made with: [Python](https://python.org/)
* Encode: UTF-8

### Steps

Install Robocorp server actions
```sh
#macOS
brew update
brew install robocorp/tools/action-server

#Windows
curl -o action-server.exe https://downloads.robocorp.com/action-server/releases/latest/windows64/action-server.exe

#Linux
curl -o action-server https://downloads.robocorp.com/action-server/releases/latest/linux64/action-server
chmod a+x action-server
# Add to PATH or move to a folder that is in PATH
sudo mv action-server /usr/local/bin/
```

# Start appliction

Go in your application folder 
```sh
cd your/application
```

Execute the command to start-action
```sh
action-server start --expose --port=8080
```

Test it
```sh
localhot:8080
```

# XLSX file

After executing the research, the xlsx file will be created in your application folder
