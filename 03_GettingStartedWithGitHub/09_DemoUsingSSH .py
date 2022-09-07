# 3'30

# podsjeca nas na rezultate nase komande
# ?> git remote -v
# ?origin  https://github.com/AntunGHU/GHPrul.git (fetch)
# ?origin  https://github.com/AntunGHU/GHPrul.git (push)
# nista lose u ovoj formi osim sto svako malo moramo (u starom term obliku komunikacije sa GH) vrsiti upis vjerodajnica!

# sad nas uvodi u kreiranje ssh-key-a kao buduceg nacina komunikacije.
# kreiranje ssh-keya sa k-dom:
# ?> ssh-keygen -t rsa -b 4096 -C "antun.jerkovic@gmail.com"
# odgovaramo na par pitanja: 1. gdje savati key (ajmo ga savati u nadmapu projekta "/home/antun/aCod/vGitVsc") 2.unijeti passfraze 3. pazi! veliko "C"
# key-si su se kreirali u mapi "aCod" a dobili su ime vGitVsc" #* !!!NOVO!!!
# otvaramo i Kopiramo pub-key, idemo na GH -dashboard, profile i Settings i SSH pa klik na "NewSSH keys" i unosimo svoj ssh-pub-key te add-amo! Pokazuje se key i upozorenje da obrisem bilo koji koji ne prepoznajem!

# sad testiramo da je sve ok sa :
# ? > ssh -T git@github.com
# na sto dobijamo poruke 1. ssh-kontakta
# ? The authenticity of host 'github.com (140.82.121.3)' can't be established.
# ? ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
# ? Are you sure you want to continue connecting (yes/no/[fingerprint])?
# odgovaramo sa "yes"
# na sto sam ja dobio negativan odgovor!!
# ? Warning: Permanently added 'github.com,140.82.121.3' (ECDSA) to the list of known hosts.
# ? git@github.com: Permission denied (publickey).
# Pokusaji premjestanja keysa u rootmapu projekta nisu uspjeli!!
# Vracam keyse u default mapu u kojoj ih ssh trazi i...uspio#* !!!NOVO!!!
# ? Hi AntunGHU! You've successfully authenticated, but GitHub does not provide shell access.
