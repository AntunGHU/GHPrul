# 5'07

# Plan: Cloning repo, Making some changing, Publishing (push) na GH

# * kreiranje klona:
# idemo na code repoa i kopy link za ssh (a po volji moze i https)
# idermo na term lokalno (otvaram 2. kopiju vsc-ea i mapu aCod unutar koje clon treba biti ravnopravan sa ostalim repoima) i k-da
# ? git clone git@github.com:AntunGHU/gillianH.git
# doslo je do kloniranja uz popratne poruke
# ? Cloning into 'gillianH'...
# ? remote: Enumerating objects: 9, done.
# ? remote: Counting objects: 100% (9/9), done.
# ? remote: Compressing objects: 100% (7/7), done.
# ? remote: Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
# ? Receiving objects: 100% (9/9), done.
# prelazimo u mapu kloniranog repoa sa
# ? cd gillianH
# ? ls -al
# ? total 20
# ? drwxrwxr-x  3 antun antun 4096 kol   6 08:29 .
# ? drwxrwxrwx 12 antun antun 4096 kol   6 08:29 ..
# ? -rw-rw-r--  1 antun antun   81 kol   6 08:29 CONTRIBUTING.md
# ? drwxrwxr-x  8 antun antun 4096 kol   6 08:29 .git
# ? -rw-rw-r--  1 antun antun  145 kol   6 08:29 README.md
# gill naglasava da je njegov prompt dobio nastavak (master) cim je usao u clonirani repo. Kod mene nije jer radim u termu od vsc! ali sam ja zato zatvorio folder za kloniranje i ponovo vsc otvorio u cloniranom repou: !!! umjesto master kao u dosadasnjim repoima pojavio se naziv main!?!?
# ? git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.

# ? nothing to commit, working tree clean
# osim main umjesto master sve drugo isto!

# * pravljenje  lokanih promjena
# kopiramo par fajlova web-seita. Ja cu one od brada
# ? git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.

# ? Untracked files:
# ?   (use "git add <file>..." to include in what will be committed)
# ?         MyTutorial/
# ?         MyZoo/
# ?         about.html
# ?         contact.html
# ?         index.html
# ?         portofolio.html

# ? nothing added to commit but untracked files present (use "git add" to track)

# idemo ih stagati sa:
# ? git add .
# pa ponovo
# ? git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.

# ? Changes to be committed:
# ?   (use "git restore --staged <file>..." to unstage)
# ?         new file:   MyTutorial/home.html
# ?         new file:   MyTutorial/images/Tutor.png
# ?         new file:   MyZoo/animals.html
# ?         new file:   MyZoo/home.html
# ?         new file:   MyZoo/images/Crocodile_Park_Davao_City.jpg
# ?         new file:   MyZoo/images/Kangaroo_Australia.JPG
# ?         new file:   MyZoo/images/Minla_strigula.jpg
# ?         new file:   MyZoo/images/snake.jpg
# ?         new file:   MyZoo/images/zoo_welcomee.jpg
# ?         new file:   MyZoo/prices.html
# ?         new file:   about.html
# ?         new file:   contact.html
# ?         new file:   index.html
# ?         new file:   portofolio.html

# idemo commit-ati sa
# ? git commit -m "Added web.files"
# ? [main ca43049] Added web-files
# ?  14 files changed, 289 insertions(+)
# ?  create mode 100644 MyTutorial/home.html
# ?  create mode 100644 MyTutorial/images/Tutor.png
# ?  create mode 100644 MyZoo/animals.html
# ?  create mode 100644 MyZoo/home.html
# ?  create mode 100644 MyZoo/images/Crocodile_Park_Davao_City.jpg
# ?  create mode 100644 MyZoo/images/Kangaroo_Australia.JPG
# ?  create mode 100644 MyZoo/images/Minla_strigula.jpg
# ?  create mode 100644 MyZoo/images/snake.jpg
# ?  create mode 100644 MyZoo/images/zoo_welcomee.jpg
# ?  create mode 100644 MyZoo/prices.html
# ?  create mode 100644 about.html
# ?  create mode 100644 contact.html
# ?  create mode 100644 index.html
# ?  create mode 100644 portofolio.html
# akko sada status-am
# ? antun@ub:~/aCod/gillianH$ git status
# ? On branch main
# ? Your branch is ahead of 'origin/main' by 1 commit.
# ?   (use "git push" to publish your local commits)

# ? nothing to commit, working tree clean
# i idemo pushati bez daljnih komplikacija. Gill koristi k-du "git push origin master" a ja cu iako mi savjetuje samo "git push" ipak probati sa
# ? git push origin main
# i sve ok!
# ? Enumerating objects: 21, done.
# ? Counting objects: 100% (21/21), done.
# ? Delta compression using up to 8 threads
# ? Compressing objects: 100% (19/19), done.
# ? Writing objects: 100% (20/20), 164.08 KiB | 1.33 MiB/s, done.
# ? Total 20 (delta 4), reused 0 (delta 0)
# ? remote: Resolving deltas: 100% (4/4), done.
# ? To github.com:AntunGHU/gillianH.git
# ?    fa9cad3..ca43049  main -> main
# ako sada statusam
# ? antun@ub:~/aCod/gillianH$ git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.

# ? nothing to commit, working tree clean

# vracamo se na gh i osvjezavamo stranicu repoa i vidimo nove fajlove!!!
