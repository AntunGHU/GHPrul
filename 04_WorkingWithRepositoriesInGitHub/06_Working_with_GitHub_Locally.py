# 3'46

# Slika sa WorkingArea, StagingArea, .git repo ili commit-area u GitHub-repo

# Gill polazi od pretpostavke da smo repo orginalno kreirali na GH
# Clone: je prvi korak rada locally: stvara se i master ali i remote-trackin branches ako ih je bilo na GH orginalu i definira deafault active branch of the remote na localnom kopiju.
# Dodavanje ili Edit fajlova na localnoj kopiji
# Add komanda za stage-anje!
# Kad smo zadovoljni s verzijama Commitamo!

# Sad bi islo Push-anje na orginal! Medjutim ako su drugi radili na slicnim djelovima koda sansa je velika da ce doci do konflikta koje smo duzni razrijesiti! Zato prije pusha moramo sa pull-anjem vidjeti stanje na GH i eventualno postojanje konflikta!
# Za razrijesenje navedenih problema imamo 2 opcije:
# a) Fetch - dobavlja promjene na originu koje mi nemamo lokalno odmah u .git repo i  tu staje. Tek ako sada mergamo nase promjene ce biti mergane kada ce  ponesto biti odradjeno automatski ali za poneke konflikte morat cemo rucno intervenirati.
# b) Pull - opcija koja povlaci stanje na originu i u working dir i u .git repo. Pull se moze promatrati kao precac od fetch i merge u jednom koraku!
# Nakon uspjesnog merganja mozemo pushati na origin!
