# coordination-game
Minerva Coordination Game


# Setup Notes (Anaconda)

pip install virtualenvwrapper


# virtualenvwrapper (under anaconda)
export WORKON_HOME=~/Envs

# for virtualenevwrapper
alias vew='source /home/dchen/anaconda3/bin/virtualenvwrapper.sh'(minverva)


mkvirtualenv minerva

workon minerva

pip install -r requirements_base_beta.txt
# go to otree-core
pip install -e .

pip install django-environ
pip install django-extensions
otree resetdb
python avatar/updateStatic.py

otree runserver
