# libenom

What is Libenom ??

Libenom is a tool created for make more easy and fast the creation of payloads with MSFvenom and get all the data generated ordered.

![captura de pantalla de 2016-08-14 17-25-06](https://cloud.githubusercontent.com/assets/16175933/17650072/1ea48a38-6244-11e6-981f-afd68191c50c.png)

<hr/>

<h2><img class="emoji" title=":exclamation:" alt=":exclamation:" height="20" width="20" src="https://assets-cdn.github.com/images/icons/emoji/unicode/2757.png"></g-emoji> Requirements</h2>

<li><p>A linux distribution for pentesting or Ubuntu, Debian, Mint </p></li>
<li><p>Recommended Kali Linux 2.0 sana or 2016.1 rolling, Parrot OS, Blackarch, Dracos ,Lionsec </p></li>

<hr/>
<h2><img class="emoji" title=":book:" alt=":book:" height="20" width="20" src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f4d6.png"> Getting Started</h2>


git clone https://github.com/bounteous/libenom.git <br/>
cd libenom<br/>
chmod +x libenom.py<br/>

<hr/>

How it works:

Execute "./libenom.py" to show all the options. For example you can first create a profile named "profile1" with "-c" option and assign it to the msfvenom parameters 

![captura de pantalla de 2016-08-14 17-48-40](https://cloud.githubusercontent.com/assets/16175933/17650180/624cd6a2-6247-11e6-9a50-a1d03d4b9745.png)

After that you can execute it "./libenom.py -x profile1", delete it "-d" or read "-r"

Also you have some pre created msfconsole listeners for a "reverse_tcp" conexion

![captura de pantalla de 2016-08-17 19-21-25](https://cloud.githubusercontent.com/assets/16175933/17746318/d4b0ed54-64af-11e6-985d-2199923c35c8.png)

<hr/>

<h2>v-1.0.1</h2>
<li><p>Added new option to <b>edit</b> IDs</p></li>
