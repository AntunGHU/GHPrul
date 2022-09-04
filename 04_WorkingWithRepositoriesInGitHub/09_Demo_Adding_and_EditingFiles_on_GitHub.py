# 7'16

# Stvoriti cemo uvjete za primjenu pull-a i fetch-a tako da cemo editati i add-ati fajlove direktno na GH-repo copiji cime simuliramo promjene na GH-repou od strane drugih developera!

# * editanje postojeceg index.html fajla i commitanje direktno na main
# idemo na home-screen od repoa i vidimo da je isti bio promjenjen tako da se vidi taj najnoviji commit!

# * kreiranje novog fajla: instructions.txt sa nekim textom pa ga commitamo u main
# nalazi se u root-u repoa

# nakon editanja i creiranja  novog fajla, sad je GH-dio repoa za 2 commita ispred lokalne copije. Lokalna kopija je nesvjesna dogadjanja i to treba syncati! To cemo raditi sa fetch ili pull komandama. Fetch donosi promjene samo git-database tj .git commit infoe ali ne i u stvarne fajlove a Pull ce to i mergati promjene u nase lokalno nepromjenjene fajlove!!! Pri tome to merganje moze proci kao ala "fast-forward" ili ce morati ici manualno ako se pojavi konflikt!

# * idemo na lokalnu kopiju i sa
# ? git status
# zahvaljujuci tome sto radim na vsc nemam isti odziv kao gill-ov git-term. Moj je term kao dio vsc-ea svjestan promjena na origin-main a gillov nije. Kako bih simulirao kopiram odgovor sa 07 fajla
# ? antun@ub:~/aCod/gillianH$ git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.
# ? nothing to commit, working tree clean

# * prvo idemo sa fetch-om koji nije destructive i nece nista mergati u nase lokalne fajlove!! Samo ce potegnuti commite! u .git db tako da ih tamo mozemo gledati i izvrsiti rucno merganje.
# ? git fetch
# i nema nikakvog responsa u termu!! za razliku od gill-a koji je dobio gomilu odgovora ala:
# ? remote: Counting objects: 6. done
# ? remote: Compressing objects: 100% (6/6). done
# ? remote: Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
# ? Unpacking objects: 100% (6/6), done
# ? From githun.com:gill-orange/fuzzy-spoon
# ?      53179d8..0cd34fg master     -> origin/master
# nakon ovog mozemo raditi manualni merge ili git pull sto gill i odradjuje i naglasava da je pull izveo fetch i merge. Idem i ja i..
# ? antun@ub:~/aCod/gillianH$ git pull
# ? Updating ca43049..4bacb97
# ? Fast-forward
# ?  index.html       | 4 ++--
# ?  instructions.txt | 3 +++
# ?  2 files changed, 5 insertions(+), 2 deletions(-)
# ?  create mode 100644 instructions.txt
# skuzio raznobojne + i - znakove pored fajlova. ++ pored index-a znaci da sam imao dva inserta a -- znaci da sam imao i dva brisanja. Dalje pored instructions +++ kaze da sam imao 3 linije insertovanja. Takodjer posebno naglasava da je kreiran instructions.txt. Bitno je istaci da je automatsko merganje nastupilo za index-fajl zato sto je on bio needitiran od zajednickog zadnjeg komita pa se promjene napravljene vremenski iza kod jedne kopije smatraju kao glavne. Da sam editirao i lokalnu i remote kopiju poslije zajednickog commita merge bi se suocio sa dva naknadna commita (po jedan na remote i local) i to bi smatrao konfliktom!!!
# ? antun@ub:~/aCod/gillianH$ git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.
# ? nothing to commit, working tree clean

# * sad idemo editati fajlove na remote (da simuliramo radove drugih developera) i kreirati commit tamo kao i na lokalnoj kopiji uz lokalno commitanje!
# editamo na GH fajl "instructions.txt" i commitamo.
# editamo lokalno index.html i stagamo i commitamo
# ? git commit -m "index.html changed"
# ? antun@ub:~/aCod/gillianH$ git commit -m "index.html changed"
# ? [main 015d8d3] index.html changed
# ?  1 file changed, 2 insertions(+), 1 deletion(-)
# sad simuliramo push nasih lokalnih promjena i ...
# ? antun@ub:~/aCod/gillianH$ git push
# ? To github.com:AntunGHU/gillianH.git
# ?  ! [rejected]        main -> main (non-fast-forward)
# ? error: failed to push some refs to 'git@github.com:AntunGHU/gillianH.git'
# ? hint: Updates were rejected because the tip of your current branch is behind
# ? hint: its remote counterpart. Integrate the remote changes (e.g.
# ? hint: 'git pull ...') before pushing again.
# ? hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# GH je odbio moj push jer je primjetio sukobe tj po 1 commit razlike te hint-a pull-anje prije push-anja kako bi smo lokalno razrijesili konflikt!
# postupamo po savjetu i pull-amo kako bi dobili promjene koje su na GH i razrjesili ih ako se sukobljavaju sa mojim. Nakon
# ? git pull
# pojavio se editor sa zahtjevom da napisemo -m poruku za merganje i commitanje zbog toga sto je napravio automatski merge-lokalno jer je mogao, jer promjene i razlike koje smo izveli, unatoc postojanju ranih commita ipak nisu bile sukobljavajuce, na gh smo editali jedan a lokalno drugi fajl!
# Ostavljamo ponudjenu opciju -m poruke i snimamo je!!! i izlazimo iz editora (nanoa) i dobijamo poruku
# ? antun@ub:~/aCod/gillianH$ git pull
# ? Merge made by the 'recursive' strategy.
# ?  instructions.txt | 2 ++
# ?  1 file changed, 2 insertions(+)
# dakle, promjene koje sam lokalno napravio su iskombinirane sa onim napravljenim na GH i mergane u novi commit. Isto bi bilo i da sam imao konflikte koje sam morao rjesavati manuelno.
# stanje je sad da je moj lokal ispred remotea jer ima njega a remote nema lokalne promjene. zato moramo push-ati
# ? antun@ub:~/aCod/gillianH$ git push origin main
# ? Enumerating objects: 9, done.
# ? Counting objects: 100% (8/8), done.
# ? Delta compression using up to 8 threads
# ? Compressing objects: 100% (5/5), done.
# ? Writing objects: 100% (5/5), 606 bytes | 606.00 KiB/s, done.
# ? Total 5 (delta 3), reused 0 (delta 0)
# ? remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
# ? To github.com:AntunGHU/gillianH.git
# ?    ae75ae7..e918a2a  main -> main
# idemo na GH i vidimo da je zaista zadnji kommit na njem sada onaj kombinirani nastali
