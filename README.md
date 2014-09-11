django_haitao
=============

a django project which search the information of the goods overseas( such as Amazon, Ebay etc.)


=============
#Step 1.

download python & django.

#Step 2.

enter the directory,press 'python manage.py syncdb'
'python manage.py makemigrations'

#Step 3.

modify the search_haitao.py line 66:'self.conn = sqlite3.connect('F:\\django_haitao-master\\django_haitao-master\\mysite\\db.sqlite3', check_same_thread = False)'
modify the directory of the sql your computer.

#Step 4.

run the search_haitao.py to prase the data.

#Step 4.

 press 'python manage.py runserver'
