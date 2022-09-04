# 3'10

# rad u git-u, kreiranje lokalbrancha i pushanje na gh

# prvo provjera statusa dok smo u loc kopiji naseg projektasa
# ? git status
# ? On branch main
# ? Your branch is up to date with 'origin/main'.
# ? nothing to commit, working tree clean

# sad idemo kreirati loalni branch sto mozemo sa
# ? git branch "ime"
# ili sa
# ? git checkout -b "add-install"
# sto kreira (!!koristeci navodne znakove) i odmah prebacuje u tu granu
# ? Switched to a new branch 'add-install'
# kreiram novi fajl "install.txt"
# ? git add .
# ? git commit -m "instalguide added"
# ? [add-install 070aae7] instalguide added
# ? 1 file changed, 1 insertion(+)
# ? create mode 100644 install.txt

# idemo pushati na gh navodeci ime origina (origin) i ime (!bez navodnih) koje zelimo da nasa lokalna grana ima na orgin (obicno isto)
# ? git push -u origin add-install
# ? Enumerating objects: 4, done.
# ? Counting objects: 100% (4/4), done.
# ? Delta compression using up to 8 threads
# ? Compressing objects: 100% (2/2), done.
# ? Writing objects: 100% (3/3), 283 bytes | 283.00 KiB/s, done.
# ? Total 3 (delta 1), reused 0 (delta 0)
# ? remote: Resolving deltas: 100% (1/1), completed with 1 local object.
# ? remote:
# ? remote: Create a pull request for 'add-install' on GitHub by visiting:
# ? remote:      https://github.com/AntunGHU/gillianH/pull/new/add-install
# ? remote:
# ? To github.com:AntunGHU/gillianH.git
# ?  * [new branch]      add-install -> add-install
# ? Branch 'add-install' set up to track remote branch 'add-install' from 'origin'.
# skok na gh pokazuje da sad imam dvije zute grane koje se obe nude za pullrequest
