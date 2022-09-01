# 7'56

# Creating tags locally and pushing to GH to explore infos about tag

# sa k-dom
# ? git log
# dobijem history projekta sa svim commitima
# ?antun@ub:~/aCod/gillianH$ git log
# ?commit 94444f6ef4121cd72c938dba1056c6b2f9010a46 (HEAD -> main, origin/#?main, origin/HEAD)
# ?Merge: 0973a49 070aae7
# ?Author: Antun <antun.jerkovic@gmail.com>
# ?Date:   Tue Aug 30 18:44:07 2022 +0200
# ?
# ?    Merge pull request #3 from AntunGHU/add-install
# ?
# ?    instalguide added predmarged commit added
# izlazim sa
# ? q

# sa kdom
# ? git tag
# provjeravam postojanje tagova i kako nista nema na output-u nema tagova!

# sa
# ? git tag stable main
# dodajem svom zadnjem commit-u label "stable" sto sa
# ?antun@ub:~/aCod/gillianH$ git tag
# ?stable
# i potvrdjujem, ali iz njega je tesko graspati ista o projektu, za bilo sto treba malo poduza k-da git log
# ? git log --oneline --graph --decorate -all
# ? antun@ub:~/aCod/gillianH$ git log --oneline --graph --decorate --all
# ? *   94444f6 (HEAD -> main, tag: stable, origin/main, origin/HEAD) Merge #? pull request #3 from AntunGHU/add-install
# ? |\
# ? | * 070aae7 (origin/add-install, add-install) instalguide added
# ? | | * c0ace64 (origin/primjer) Update instructions.txt
# ? | |/
# ? |/|
# ? * | 0973a49 Novi red od colaboratora
# ? |/
# ? *   e918a2a Merge branch 'main' of github.com:AntunGHU/gillianH into main
# ? |\
# ? | * ae75ae7 Update instructions.txt
# ? * | 015d8d3 index.html changed
# ? |/
# ? * 4bacb97 Create instructions.txt
# ? :

# zato idemo kreirati anotated tag s kom
# ? git tag -a v0.1 -m "0.1 release" 94444f6
# ponovna provjera sa git tag daje
# ? antun@ub:~/aCod/gillianH$ git tag
# ? stable
# ? v0.1

# sad ako zelimo pushati i tagove na GH nije dovoljno samo push, moramo dodati --tags, dakle
# ? git push --tags
# ? antun@ub:~/aCod/gillianH$ git push --tags
# ? Enumerating objects: 1, done.
# ? Counting objects: 100% (1/1), done.
# ? Writing objects: 100% (1/1), 159 bytes | 159.00 KiB/s, done.
# ? Total 1 (delta 0), reused 0 (delta 0)
# ? To github.com:AntunGHU/gillianH.git
# ?  * [new tag]         stable -> stable
# ?  * [new tag]         v0.1 -> v0.1

# na gh!!!
# na gh po novom releases su prazni i ne kreiraju se automatski iz tagova (koa kod gill-a) ali postoji opcija kreiranja
# kreiram i pratim gilla: brisanje taga i pokaz da to brisanje nije obrisalo lokalni istoimeni tag. njega mogu lokalno obrisati sa
# ? git tag -d "stable"
# obrnuto, ako prvo brisemo lokalno sa
# ? git tag -d "v0.2"
# brisanje moramo dovrsiti sa
# ? git push origin :v0.2
# kada odlazak na gh i refresh pokazuju da je v0.2 obrisan!
