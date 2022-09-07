# 7'01

# Cilj: create repo na GH and link to our lokal repo

# 1.Kreiranje repoa na GH koji mora biti unique unutar naseg acounta, README.md fajl, gitignore, licence i Create

# 2.Nakon kreiranja u kartici code novog repoa pojavljuju se opcije:
# --Quick setup (za quick setup lokalnog repoa koji ce biti povezan sa ovim kreiranim na GH-eu.) (jedina opcija ostala u GH)
# --"or create a new repo on the command line" ove opcije vise nema ali je jako instruktivna pa je prepisujem:
# ?> echo "# firstrepo" >> README.md
# ?> git init
# ?> git add README.md
# ?> git commit -m "first commit"
# ?> git remote add origin https://github.com/gill-orange/firstrepo.git
# ?> git push -u origin master
# --"or push an existing repository from the command line"
# ?> git remote add origin https://github.com/gill-orange/firstrepo.git
# ?> git push -u origin master
# --"or import code from another repository"
# pise: you can initialize this repo ....

# 3.Gill ide sa drugom opcijom pushanja postojeceg repoa s komand-lajna na GH.
# 3.1 odradjuje komandu unutar naseg istoimenog localnog repoa
# ?> git remote -v
# kako bi provjerio ima li lokalni repo remote origin - nista ne dobija nazad pa zakljucuje da nema!
# ?> git remote add origin https://github.com/gill-orange/firstrepo.git
# ako sada odradimo kdu
# ?> git remote -v
# dobijemo odgovore:
# ?> origin https://github.com/gill-orange/firstrepo.git (fetch)
# ?> origin https://github.com/gill-orange/firstrepo.git (push)
# sada imamo povezan lokalni repo s onim na gh ali jos nista nismo pushali
# ?> git push -u origin master
# login! i git-term mi vratio par infoa i zavrsio: kopirao 4 itd sa zavrsnim "Branch 'master' set up to track remote branch 'master' from 'origin'"
# * Ispada da barosanu nije u pravu, nemoraju imati ista imena!!!
