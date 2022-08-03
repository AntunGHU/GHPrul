# 7'01

# Cilj: create repo na GH and link to our lokal repo

# 1.Kreiranje repoa na GH koji mora biti unique unutar naseg acounta, readme fajl, gitignore (mogu se specificirati prema vrsti projekta fajlovi koje ce git ignorirati), github i generiranje licencev(apashe, gnu, Mit, itd) i Create

# 2.Nakon kreiranja u kartici code novog repoa pojavljuju se opcije:
# --Quick setup (za quick setup lokalnog repoa koji ce biti povezan sa ovim kreiranim na GH-eu.) (Malo izmjenjena ovo je jedina opcija ostala u GH)
# --"or create a new repo on the command line" oveopcije vise nema ali je jako instruktivna pa je prepisujem:
# ?> echo "# firstrepo" >> README.md
# ?> git init
# ?> git add README.md
# ?> git commit -m "first commit"
# ?> git remote add origin https://github.com/gill-orange/firstrepo.git
# ?> git push *u origin master
# --"or push an existing repository from the command line"
# ?> git remote add origin https://github.com/gill-orange/firstrepo.git
# ?> git push -u origin master
# --"or import code from another repository"
# pise: you can initialize this repo ....

# 3.Gill ide sa drugom opcijom pushanja postojeceg repoa s komand-lajna na GH, tj na ovaj koji je sad upravo stvorio. Kopira: "git remote add origin https://github.com/gill-orange/firstrepo.git" i ide u term.
# 3.1 odradjuje komandu unutar naseg istoimenog localnog repoa
# ?> git remote -v
# kako bi provjerio ima li lokalni repo remote origin. nista ne dobija nazad pa zakljucuje da nema!
# sad odradjuje komandu sa termom unutar mape naseg lokalnog projekta
# ?> git remote add origin https://github.com/gill-orange/firstrepo.git
# ako sada odradimo kdu
# ?> git remote -v
# dobijemo odgovore:
# ?> origin https://github.com/gill-orange/firstrepo.git (fetch)
# ?> origin https://github.com/gill-orange/firstrepo.git (push)
# dakle sada imamo povezan lokalni repo s onim na gh ali jos nista nismo pushali
# idemo na GH i kopiramo 2. k-du te sekcije "git push -u origin master" gdje -u daje instrukciju da se stvori tracking relation izmedju lokalnog mastera i origina
# ?> git push -u origin master
# pojavljuju se login podaci (hm, kad bih sve radio iz git-terminala mozda bih i to morao, ovako preko vsc to se pojednostavilo). Nakon prijave git-term mi vratio par infoa i zavrsio: kopirao 4 itd sa zavrsnim "Branch 'master' set up to track remote branch 'master' from 'origin'". Zahvaljujuci tome ubuduce nemoramo navoditi imena i pushanje ce se odvijati automatski izmedju povezanih mastera

# * Ispada da barosanu nije u pravu, nemoraju imati ista imena!!!
