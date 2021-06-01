# bibliobot
Bot per prenotarsi automaticamente tramite affluences in biblioteca di ingegneria Unibo 

ATTUALMENTE BIBLIOTECHE SUPPORTATE:
Biblioteca Ingegneria Dore
Biblioteca Bigiavi
Biblioteca Chimica Ingegneria
Biblioteca Campus Rimini

E' necessario modificare i file con il proprio nome utente e password di unibo.

USAGE: python3 prenotaDore.py o qualunque biblioteca di proprio interesse, il bot è impostato per prenotare la biblioteca mattina e pomeriggio di 7 giorni dopo il momento del lancio (tranne bigiavi ogni 2 giorni), se si desidera cambiare tale parametro modificare il file.
Su ubuntu è possibile lanciare in automatico il file a mezzanotte tramite crontab.
Per farlo usare il comando crontab -e da terminale e inserire  
1 0 * * 1,2,3,4,5 /percorsoPython/python3 /percorsoFile/prenotaX.py


