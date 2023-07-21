### Scriptul a fost dezvoltat cu urmatoarele:

#### Sistemul de operare: Windows 10 version 22H2
#### python --version: Python 3.10.2
### Bibliotecile folosite:
#### Selenium:
    - pip install -U selenium
#### pyAudio:
    - python -m pip install pyaudio
#### pyautogui:
    - py -m pip install pyautogui
#### numpy:
    - pip install numpy
#### opencv:
    - pip install opencv-python
#### moviepy (pentru concatenarea audio + video):
    - pip install moviepy
#### shutil (pentru verificare spatiu memorie):
    - pip install shutil

### Structura fisierelor:
   Proiectul contine 7 fisiere pentru: verificare conexiunii la internet, deschidere YouTube, deschidere videoclip,
inregistrare video, inregistrare audio, concatenare fisiere audio si video, afisarea nivelului decibelilor.
#### Erori intampinate:
   - In momentul deschiderii YouTube videoclipul era deja selectat inainte ca pagina de acceptare sau refuzare a cookie-urilor sa fie afisata. Am ales sa pun un `time.sleep(2)` pentru a astepta pagina de cookie-uri sa fie incarcata.
   - In fisierul ***RecordAudio.py*** se afla codul comentat pentru inregistrarea audio-ului din output, nu cel de la microfon. Fiind folosit in threaduri nu functioneaza si are erori. O posibila cauza este atunci cand este deschisa si o aplicatie de meet precum Zoom, Discord, Teams. Nu am avut o solutie finala, asa ca am ramas la inregistrarea audio-ului de la microfon.
   - Caz in care videoclipul nu are reclama si in consecinta nu exista buton de skip. Am adaugat o verificare in cazul in care butonul de skip a fost gasit atunci sa fie apasat.

#### Functionalitatea:
   Scriptul verifica conexiunea la internet pentru a incepe cautarea paginii si inregistrarea ecranului. In caz contrar, o atentionare este trecuta in fisierul ***LogFile.log***.
####
   Cu ajutorul functiei `open_browser()` este deschis un tab de Firefox. Toate executiile realizate sunt trecute in fisierul `.log`.
####
   Odata deshisa pagina de YouTube sunt refuzate cookie-urile si se extrage o lista cu fisierele afisate pe prima pagina (am observat ca sunt alese 33 de videoclipuri). Din aceasta lista de videoclipuri este selectat random unul. Dupa deschiderea videoclipului se va da click pe butonul de play, iar in cazul in care avem o reclama apasam pe butonul de skip.
####
   Dupa inceperea videoclipui, incep in mod paralel inregistrarea ecranului video si inregistrarea audio, inregistrarea audio de face doar din microfon. Insa se verifica daca mai exista memorie pe dispozitiv pentru a fi salvate.
####
   In momentul in care ambele fisiere au fost salvate, apelam functia `create_video()` care concatezeaza fisierul audio, impreuna cu fisierul video.
####
   In final este realizata o analiza a fisierului audio pentru a afla nivelul decibelilor. Rezultatul final este salvat in fisierul `.log`.
