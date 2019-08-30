from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from books.models import Book


def render_book_catalogue(request, user_id):
    template = 'books/catalogue.html'
    context = {
        'catalogue': Book.objects.filter(owner_id=user_id),
        'user': user_id
    }
    return render(request, template, context)


def create_book(request, user_id):
    if request.method == 'POST':
        new_book = Book(
            name=request.POST['name'],
            author=request.POST['author'],
            genre=request.POST['genre'],
            language=request.POST['language'],
            publication_date=request.POST['publication_date'],
            owner_id=request.POST['owner_id'],
        )
        new_book.save()

        return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': new_book.owner.id}))
    elif request.method == 'GET':
        template = 'books/create_book_form.html'
        context = {
            'user': user_id
        }
        return render(request, template, context)
    return HttpResponse('Error: method now allowed.')


def edit_book(request, book_id):
    if request.method == 'POST':
        updated_book = Book.objects.get(id=book_id)
        updated_book.name = request.POST['name']
        updated_book.author = request.POST['author']
        updated_book.genre = request.POST['genre']
        updated_book.language = request.POST['language']
        updated_book.publication_date = request.POST['publication_date']
        updated_book.save()

        return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': updated_book.owner.id}))
    elif request.method == 'GET':
        template = 'books/edit_book_form.html'
        context = {
            'book': Book.objects.get(id=book_id)
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_book(request, book_id):
    deleted_book = Book.objects.get(id=book_id)
    deleted_book.delete()

    return HttpResponseRedirect(reverse('books:catalogue', kwargs={'user_id': deleted_book.owner.id}))
