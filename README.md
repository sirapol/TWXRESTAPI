# TWXRESTAPI

python version : 3.7.3

This python script is will send data directly to properties of thing.
It using REST API of Thingworx by PUT method.

The data is json type.

## How to use?
1. Clone this git to your folder.
2. Create Thing in Thingworx and add properties what your want.
3. Create ApplicationKey in Thingworx and set user name reference to your user. E.g. Administrator.
4. Edit parameter in script.
    Host name # E.g. IP address of Thingworx server or localhost if you using same server.
    ApplicationKey # Hash key from topic 3.
    ThingName # Thing Name from topic 2.
    Data # edit strData
5. run script. If you config correct, This script will be reply "<Response [200]>"

## Link Referense

1. All data for developer : https://developer.thingworx.com/
2. Thingworx REST API Doc : https://developer.thingworx.com/en/resources/apis