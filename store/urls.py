from django.urls import path
from .views import allbooks,addbook,deletebook,issuerequest,myissues,issue_book,return_book,requestedissues,myfines,allfines,deletefine,payfine,pay_status,filter_books_by_category

urlpatterns = [
    path('',allbooks,name='home'),
    path('books/<str:category>/',filter_books_by_category, name='filter_books'),
    path('addbook/',addbook),
    path('deletebook/<int:bookID>/',deletebook),
    path('request-book-issue/<int:bookID>/',issuerequest),
    path('my-issues/',myissues),
    path('my-fines/',myfines),
    path('payfines/<int:fineID>/',payfine),
    path('paystatus/<int:fineID>/',pay_status),
    path('all-issues/',requestedissues),
    path('all-fines/',allfines),
    path('issuebook/<int:issueID>/',issue_book),
    path('returnbook/<int:issueID>/',return_book),
    path('delete-fine/<int:fineID>/',deletefine),
]