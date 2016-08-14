# libenom

What is Libenom ??

Libenom is a tool created for make more easy and fast the creation of payloads with MSFvenom and get all the data generated ordered.

![captura de pantalla de 2016-08-14 17-25-06](https://cloud.githubusercontent.com/assets/16175933/17650072/1ea48a38-6244-11e6-981f-afd68191c50c.png)

<hr/>

<g-emoji alias="exclamation" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/2757.png"><img class="emoji" title=":exclamation:" alt=":exclamation:" height="20" width="20" src="https://assets-cdn.github.com/images/icons/emoji/unicode/2757.png"></g-emoji>

<h2><a id="user-content-heavy_exclamation_mark-requirements" class="anchor" href="#heavy_exclamation_mark-requirements" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><g-emoji alias="exclamation" fallback-src="https://assets-cdn.github.com/images/icons/emoji/unicode/2757.png"><img class="emoji" title=":exclamation:" alt=":exclamation:" height="20" width="20" src="https://assets-cdn.github.com/images/icons/emoji/unicode/2757.png"></g-emoji> Requirements</h2>

<li><p>A linux distribution for pentesting or Ubuntu, Debian, Mint) </p></li>
<li><p>Recommended Kali Linux 2.0 sana or 2016.1 rolling, Parrot OS, Blackarch, Dracos ,Lionsec ) </p></li>

<hr/>

Getting Started:

git clone https://github.com/bounteous/libenom.git <br/>
cd libenom<br/>
chmod +x libenom.py<br/>

<hr/>

How it works:

Execute "./libenom.py" to show all the options. For example you can first create a profile named "profile1" with "-c" option and assign it to the msfvenom parameters 

![captura de pantalla de 2016-08-14 17-48-40](https://cloud.githubusercontent.com/assets/16175933/17650180/624cd6a2-6247-11e6-9a50-a1d03d4b9745.png)

After that you can execute it "./libenom.py -x profile1", delete it "-d" or read "-r"

Also you have some pre created msfconsole listeners for a "reverse_tcp" conexion

![captura de pantalla de 2016-08-14 17-53-03](https://cloud.githubusercontent.com/assets/16175933/17650201/f9236ae6-6247-11e6-8b2f-c528bdb5788a.png)
