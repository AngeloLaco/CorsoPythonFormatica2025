`GUIDA AI COMANDI UNIX/LINUX PER PROGRAMMATORI
Corso Python e AI - Prof. Angelo La Cognata

INDICE
1. Introduzione al Terminale
2. Navigazione nel File System
3. Gestione File e Cartelle
4. Visualizzazione Contenuti
5. Comandi per Python e VS Code
6. Git e Version Control
7. Cheat Sheet Rapido

PERCHE IMPARARE IL TERMINALE?
- Piu veloce per molte operazioni
- Indispensabile per programmazione
- Necessario per Git e gestione progetti
- Richiesto in ambito professionale

NAVIGAZIONE BASE
pwd - Mostra directory corrente
ls - Lista file e cartelle
cd - Cambia directory

GESTIONE FILE
mkdir - Crea cartella
touch - Crea file
cp - Copia
mv - Sposta/Rinomina
rm - Elimina

PYTHON E VS CODE
python script.py - Esegue script
pip install - Installa pacchetti
code . - Apre VS Code

GIT COMANDI
git init - Inizializza repo
git add - Aggiunge file
git commit - Salva modifiche
git push - Invia al server

Per la guida completa con esempi dettagliati, consultare la documentazione.
`;
GUIDA AI COMANDI UNIX/LINUX PER PROGRAMMATORI
Corso Python e AI - Prof. Angelo Laco

═══════════════════════════════════════════════════════════════

INDICE

1. Introduzione al Terminale
2. Navigazione nel File System
3. Gestione File e Cartelle
4. Visualizzazione Contenuti
5. Permessi e Proprietà
6. Operazioni Avanzate
7. Comandi per Python e VS Code
8. Git e Version Control
9. Comandi di Sistema
10. Scorciatoie Utili
11. Cheat Sheet Rapido

═══════════════════════════════════════════════════════════════

1. INTRODUZIONE AL TERMINALE

Il TERMINALE (o Command Line Interface - CLI) è un'interfaccia testuale per interagire con il sistema operativo.

PERCHE IMPARARE IL TERMINALE?
• Piu veloce per molte operazioni
• Indispensabile per programmazione
• Necessario per Git e gestione progetti
• Richiesto in ambito professionale
• Funziona su tutti i sistemi operativi

COME APRIRE IL TERMINALE:
• Windows: Git Bash, PowerShell, WSL, o Windows Terminal
• Mac: Terminal (Applicazioni → Utility → Terminal)
• Linux: Ctrl + Alt + T

NOTA PER WINDOWS:
Windows usa comandi diversi (CMD/PowerShell). Consigliamo:
- Installare Git Bash (comandi Unix su Windows)
- Usare WSL (Windows Subsystem for Linux)
- Usare il terminale integrato in VS Code

═══════════════════════════════════════════════════════════════

2. NAVIGAZIONE NEL FILE SYSTEM

═══════════════════════════════════════════════════════════════

pwd
----
COSA FA: Mostra il percorso della directory corrente
SIGNIFICATO: Print Working Directory

ESEMPIO:
$ pwd
/home/utente/Documenti/Corso_Python

USO: Utile per sapere dove ti trovi nel file system


═══════════════════════════════════════════════════════════════

ls
--
COSA FA: Elenca file e cartelle nella directory corrente
SIGNIFICATO: List

SINTASSI BASE:
$ ls                    # Elenca file
$ ls -l                 # Lista dettagliata
$ ls -a                 # Mostra anche file nascosti
$ ls -la                # Combina -l e -a
$ ls -lh                # Dimensioni leggibili (KB, MB, GB)

ESEMPI:
$ ls
Documenti  Download  Immagini  Video

$ ls -l
drwxr-xr-x 5 utente utente 4096 ott 20 10:30 Documenti
drwxr-xr-x 2 utente utente 4096 ott 19 15:20 Download

$ ls -la
drwxr-xr-x  5 utente utente 4096 ott 20 10:30 .
drwxr-xr-x 24 utente utente 4096 ott 15 09:00 ..
drwxr-xr-x  5 utente utente 4096 ott 20 10:30 Documenti
-rw-r--r--  1 utente utente  220 ott 01 08:00 .bashrc


═══════════════════════════════════════════════════════════════

cd
--
COSA FA: Cambia directory (cartella)
SIGNIFICATO: Change Directory

SINTASSI:
$ cd nome_cartella      # Entra in una cartella
$ cd ..                 # Sale di una cartella (parent)
$ cd ~                  # Vai alla home directory
$ cd /                  # Vai alla root (radice)
$ cd -                  # Torna alla directory precedente

ESEMPI:
$ cd Documenti          # Entra in Documenti
$ cd Corso_Python       # Entra in Corso_Python
$ cd ..                 # Torna indietro di una cartella
$ cd ../..              # Sale di due livelli
$ cd ~                  # Vai alla home
$ cd ~/Documenti/Corso_Python  # Percorso assoluto

TRUCCO: Usa TAB per autocompletare i nomi!


═══════════════════════════════════════════════════════════════

3. GESTIONE FILE E CARTELLE

═══════════════════════════════════════════════════════════════

mkdir
-----
COSA FA: Crea una nuova cartella
SIGNIFICATO: Make Directory

SINTASSI:
$ mkdir nome_cartella
$ mkdir -p percorso/completo/cartella  # Crea cartelle annidate

ESEMPI:
$ mkdir progetti
$ mkdir Lezione_3
$ mkdir -p progetti/python/esercizi    # Crea tutto il percorso


═══════════════════════════════════════════════════════════════

touch
-----
COSA FA: Crea un file vuoto (o aggiorna timestamp)

ESEMPI:
$ touch file.txt
$ touch script.py
$ touch index.html style.css script.js  # Crea più file


═══════════════════════════════════════════════════════════════

cp
--
COSA FA: Copia file o cartelle
SIGNIFICATO: Copy

SINTASSI:
$ cp origine destinazione
$ cp -r cartella_origine cartella_destinazione  # Copia cartelle

ESEMPI:
$ cp file.txt backup.txt              # Copia file
$ cp script.py ../                    # Copia in cartella superiore
$ cp -r progetti backup_progetti      # Copia cartella intera
$ cp *.py backup/                     # Copia tutti i file .py


═══════════════════════════════════════════════════════════════

mv
--
COSA FA: Sposta o rinomina file/cartelle
SIGNIFICATO: Move

SINTASSI:
$ mv origine destinazione

ESEMPI:
# SPOSTARE FILE
$ mv file.txt Documenti/              # Sposta in Documenti
$ mv script.py progetti/              # Sposta in progetti

# RINOMINARE FILE
$ mv vecchio_nome.txt nuovo_nome.txt
$ mv test.py main.py

# SPOSTARE E RINOMINARE
$ mv file.txt ../backup/nuovo_file.txt


═══════════════════════════════════════════════════════════════

rm
--
COSA FA: Elimina file o cartelle
SIGNIFICATO: Remove

⚠️ ATTENZIONE: rm elimina DEFINITIVAMENTE! Non va nel cestino!

SINTASSI:
$ rm file.txt                # Elimina un file
$ rm -r cartella/            # Elimina cartella e contenuto
$ rm -rf cartella/           # Forza eliminazione (usa con cautela!)
$ rm *.txt                   # Elimina tutti i file .txt

ESEMPI:
$ rm test.py
$ rm -r vecchi_progetti/
$ rm file1.txt file2.txt file3.txt


═══════════════════════════════════════════════════════════════

4. VISUALIZZAZIONE CONTENUTI

═══════════════════════════════════════════════════════════════

cat
---
COSA FA: Visualizza il contenuto di un file
SIGNIFICATO: Concatenate

ESEMPI:
$ cat file.txt              # Mostra tutto il file
$ cat script.py             # Mostra il codice Python
$ cat file1.txt file2.txt   # Mostra più file di seguito


═══════════════════════════════════════════════════════════════

head / tail
-----------
COSA FA: Mostra le prime/ultime righe di un file

ESEMPI:
$ head file.txt             # Prime 10 righe
$ head -n 20 file.txt       # Prime 20 righe
$ tail file.txt             # Ultime 10 righe
$ tail -n 5 log.txt         # Ultime 5 righe
$ tail -f log.txt           # Segue il file in tempo reale


═══════════════════════════════════════════════════════════════

less / more
-----------
COSA FA: Visualizza file con scorrimento

ESEMPI:
$ less file.txt             # Visualizza con scorrimento
$ more file.txt             # Simile a less

COMANDI IN LESS:
• Spazio: pagina successiva
• b: pagina precedente
• q: esci
• /parola: cerca "parola"
• n: prossima occorrenza


═══════════════════════════════════════════════════════════════

grep
----
COSA FA: Cerca testo all'interno di file
SIGNIFICATO: Global Regular Expression Print

SINTASSI:
$ grep "testo" file.txt
$ grep -r "testo" cartella/     # Ricerca ricorsiva
$ grep -i "testo" file.txt      # Ignora maiuscole/minuscole
$ grep -n "testo" file.txt      # Mostra numero riga

ESEMPI:
$ grep "def" script.py          # Cerca funzioni
$ grep -r "TODO" progetti/      # Cerca TODO in tutti i file
$ grep -i "error" log.txt       # Cerca errori


═══════════════════════════════════════════════════════════════

5. PERMESSI E PROPRIETÀ

═══════════════════════════════════════════════════════════════

chmod
-----
COSA FA: Cambia i permessi di file/cartelle
SIGNIFICATO: Change Mode

PERMESSI:
• r (read) = 4     → leggere
• w (write) = 2    → scrivere
• x (execute) = 1  → eseguire

ESEMPI:
$ chmod +x script.py        # Rende eseguibile
$ chmod 755 file.sh         # rwxr-xr-x
$ chmod 644 file.txt        # rw-r--r--

SPIEGAZIONE 755:
• 7 (4+2+1) = rwx per il proprietario
• 5 (4+1) = r-x per il gruppo
• 5 (4+1) = r-x per gli altri


═══════════════════════════════════════════════════════════════

6. OPERAZIONI AVANZATE

═══════════════════════════════════════════════════════════════

find
----
COSA FA: Trova file e cartelle

ESEMPI:
$ find . -name "*.py"              # Trova tutti i file .py
$ find . -type f -name "test*"     # File che iniziano con "test"
$ find . -type d -name "backup"    # Cartelle chiamate "backup"
$ find . -mtime -7                 # File modificati negli ultimi 7 giorni


═══════════════════════════════════════════════════════════════

|  (Pipe)
---------
COSA FA: Passa l'output di un comando come input a un altro

ESEMPI:
$ ls -l | grep ".py"               # Lista solo file .py
$ cat file.txt | grep "error"      # Cerca "error" nel file
$ history | grep "git"             # Cerca comandi git usati


═══════════════════════════════════════════════════════════════

> e >>
------
COSA FA: Redirige output su file

> : Sovrascrive il file
>> : Aggiunge in coda al file

ESEMPI:
$ echo "Ciao" > file.txt           # Crea/sovrascrive file
$ echo "Mondo" >> file.txt         # Aggiunge al file
$ ls -l > elenco.txt               # Salva lista in file
$ python script.py > output.txt    # Salva output


═══════════════════════════════════════════════════════════════

7. COMANDI PER PYTHON E VS CODE

═══════════════════════════════════════════════════════════════

python / python3
----------------
ESEMPI:
$ python --version                 # Verifica versione Python
$ python3 --version
$ python script.py                 # Esegue script
$ python -m pip install libreria   # Installa libreria


═══════════════════════════════════════════════════════════════

pip / pip3
----------
COSA FA: Gestisce pacchetti Python

ESEMPI:
$ pip install numpy                # Installa numpy
$ pip install -r requirements.txt  # Installa da file
$ pip list                         # Lista pacchetti installati
$ pip freeze > requirements.txt    # Esporta dipendenze
$ pip uninstall numpy              # Disinstalla pacchetto


═══════════════════════════════════════════════════════════════

code
----
COSA FA: Apre Visual Studio Code

ESEMPI:
$ code .                           # Apre VS Code nella cartella corrente
$ code file.py                     # Apre file in VS Code
$ code cartella/                   # Apre cartella in VS Code


═══════════════════════════════════════════════════════════════

8. GIT E VERSION CONTROL

═══════════════════════════════════════════════════════════════

git init
--------
Inizializza repository Git

$ git init


═══════════════════════════════════════════════════════════════

git clone
---------
Clona un repository

$ git clone https://github.com/utente/progetto.git


═══════════════════════════════════════════════════════════════

git status
----------
Mostra stato del repository

$ git status


═══════════════════════════════════════════════════════════════

git add
-------
Aggiunge file allo staging

$ git add file.py              # Aggiunge un file
$ git add .                    # Aggiunge tutti i file


═══════════════════════════════════════════════════════════════

git commit
----------
Crea un commit

$ git commit -m "Messaggio descrittivo"


═══════════════════════════════════════════════════════════════

git push / pull
---------------
Invia/riceve modifiche da remoto

$ git push origin main         # Invia modifiche
$ git pull                     # Riceve modifiche


═══════════════════════════════════════════════════════════════

9. COMANDI DI SISTEMA

═══════════════════════════════════════════════════════════════

clear
-----
Pulisce il terminale

$ clear


═══════════════════════════════════════════════════════════════

history
-------
Mostra storico comandi

$ history                      # Mostra tutti i comandi
$ history | grep "python"      # Cerca comandi python
$ !123                         # Esegue comando numero 123


═══════════════════════════════════════════════════════════════

exit
----
Chiude il terminale

$ exit


═══════════════════════════════════════════════════════════════

whoami
------
Mostra nome utente corrente

$ whoami


═══════════════════════════════════════════════════════════════

which
-----
Mostra percorso di un comando/programma

$ which python                 # /usr/bin/python
$ which code                   # /usr/local/bin/code


═══════════════════════════════════════════════════════════════

10. SCORCIATOIE UTILI

═══════════════════════════════════════════════════════════════

SCORCIATOIE DA TASTIERA:

Ctrl + C        Interrompe il comando in esecuzione
Ctrl + D        Logout / chiude terminale
Ctrl + L        Pulisce schermo (come clear)
Ctrl + A        Va all'inizio della riga
Ctrl + E        Va alla fine della riga
Ctrl + U        Cancella dalla posizione al inizio riga
Ctrl + K        Cancella dalla posizione alla fine riga
Ctrl + R        Cerca nei comandi precedenti
↑ / ↓           Naviga tra i comandi precedenti
Tab             Autocompletamento

CARATTERI SPECIALI:

~               Home directory
.               Directory corrente
..              Directory superiore
*               Wildcard (tutti i file)
?               Wildcard (un carattere)
|               Pipe (collega comandi)
>               Redirige output
>>              Appende output
&               Esegue in background


═══════════════════════════════════════════════════════════════

11. CHEAT SHEET RAPIDO

═══════════════════════════════════════════════════════════════

NAVIGAZIONE
-----------
pwd                         Dove sono?
ls                          Cosa c'è qui?
ls -la                      Lista dettagliata completa
cd cartella                 Vai in cartella
cd ..                       Torna indietro
cd ~                        Vai alla home

FILE E CARTELLE
---------------
mkdir nome                  Crea cartella
touch file.txt              Crea file
cp origine dest             Copia
mv origine dest             Sposta/Rinomina
rm file                     Elimina file
rm -r cartella              Elimina cartella

VISUALIZZAZIONE
---------------
cat file                    Mostra file
less file                   Scorri file
head file                   Prime righe
tail file                   Ultime righe
grep "testo" file           Cerca nel file

PYTHON
------
python script.py            Esegui script
python --version            Versione Python
pip install libreria        Installa libreria
pip list                    Lista librerie

VS CODE
-------
code .                      Apri VS Code qui
code file.py                Apri file

GIT
---
git init                    Inizializza repo
git status                  Stato repo
git add .                   Aggiungi tutto
git commit -m "msg"         Commit
git push                    Invia modifiche
git pull                    Ricevi modifiche

SISTEMA
-------
clear                       Pulisci schermo
history                     Storico comandi
exit                        Esci


═══════════════════════════════════════════════════════════════

ESERCIZI PRATICI

═══════════════════════════════════════════════════════════════

ESERCIZIO 1: Navigazione Base
------------------------------
1. Apri il terminale
2. Controlla dove ti trovi con pwd
3. Elenca i file con ls
4. Vai nella cartella Documenti con cd
5. Torna alla home con cd ~


ESERCIZIO 2: Creare Struttura Progetto
---------------------------------------
1. Vai in Documenti
2. Crea cartella "MioProgetto"
3. Entra nella cartella
4. Crea sottocartelle: src, tests, docs
5. Crea file main.py in src


ESERCIZIO 3: Gestione File
---------------------------
1. Crea un file test.txt
2. Copialo in backup.txt
3. Rinomina backup.txt in old.txt
4. Elimina old.txt


ESERCIZIO 4: Workflow Python
-----------------------------
1. Crea cartella progetto_python
2. Entra nella cartella
3. Crea file hello.py
4. Apri la cartella in VS Code con: code .
5. Scrivi del codice
6. Eseguilo con: python hello.py


ESERCIZIO 5: Git Base
----------------------
1. Crea cartella my_project
2. Inizializza Git: git init
3. Crea file README.md
4. Aggiungi: git add .
5. Commit: git commit -m "First commit"


═══════════════════════════════════════════════════════════════

CONSIGLI PER PRINCIPIANTI

═══════════════════════════════════════════════════════════════

1. USA TAB PER AUTOCOMPLETARE
   Non digitare tutto! Premi Tab per completare nomi.

2. USA LE FRECCE ↑↓
   Richiama comandi precedenti invece di riscriverli.

3. ATTENZIONE CON rm
   Non c'è "undo"! Verifica sempre prima di eliminare.

4. LEGGI I MESSAGGI DI ERRORE
   Ti dicono cosa è andato storto!

5. USA --help
   Ogni comando ha una guida: comando --help

6. PRATICA PRATICA PRATICA
   Il terminale diventa naturale con l'uso!

7. NON AVER PAURA
   Non puoi "rompere" il computer con i comandi base.

8. USA IL TERMINALE IN VS CODE
   È integrato! View → Terminal (Ctrl + `)


═══════════════════════════════════════════════════════════════

RISORSE AGGIUNTIVE

═══════════════════════════════════════════════════════════════

TUTORIAL ONLINE:
• Linux Journey: linuxjourney.com
• ExplainShell: explainshell.com
• OverTheWire (giochi): overthewire.org

CHEAT SHEET:
• devhints.io/bash
• github.com/RehanSaeed/Bash-Cheat-Sheet

LIBRI:
• "The Linux Command Line" by William Shotts (gratuito)


═══════════════════════════════════════════════════════════════

GLOSSARIO

═══════════════════════════════════════════════════════════════

CLI         Command Line Interface - Interfaccia a riga di comando
Shell       Interprete dei comandi (es. Bash, Zsh)
Terminal    Finestra dove digitare i comandi
Path        Percorso di file/cartella
Home        Cartella utente principale (~)
Root        Cartella radice del sistema (/)
Wildcard    Caratteri jolly (* e ?)
Pipe        Collegamento tra comandi (|)
Flag        Opzione di un comando (es. -l, -a)


═══════════════════════════════════════════════════════════════

CI VEDIAMO A LEZIONE CON VS CODE! 💻

Prof. Angelo Laco
Corso Python e AI - 80 ore

═══════════════════════════════════════════════════════════════