# libenom

What is Libenom ??

Libenom is a tool created for make more easy and fast the creation of payloads with MSFvenom and get all the data generated ordered.

![captura de pantalla de 2016-08-14 17-25-06](https://cloud.githubusercontent.com/assets/16175933/17650072/1ea48a38-6244-11e6-981f-afd68191c50c.png)

<hr/>

Getting Started:

git clone https://github.com/bounteous/libenom.git <br/>
cd libenom<br/>
chmod +x libenom.py<br/>

<hr/>

How it works:

Execute "./libenom.py" to show all the options. For example you can first create a profile named "profile1" with "-c" option and asign it to the msfvenom parameters 

![captura de pantalla de 2016-08-14 17-48-40](https://cloud.githubusercontent.com/assets/16175933/17650180/624cd6a2-6247-11e6-9a50-a1d03d4b9745.png)

After that you can execute it "./libenom.py -x profile1", delete it "-d" or read "-r"

Also you have some precreated msfconsole listeners for a "reverse_tcp" conexion

![captura de pantalla de 2016-08-14 17-53-03](https://cloud.githubusercontent.com/assets/16175933/17650201/f9236ae6-6247-11e6-8b2f-c528bdb5788a.png)
