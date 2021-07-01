from django.shortcuts import get_object_or_404, render, redirect
from .models import Like, Rental

def rental(request):
    rentals = Rental.objects.all()
    return render(request, "rental.html",{'rentals':rentals})

def product(request, rental_id):
    rental = Rental.objects.get(id = rental_id)
    try:
        liked =  rental.like.filter(user = request.user).exists()
    except:
        liked = False
    total_likes = rental.like.all()
    count = 0
    for l in total_likes:
        count +=1
    return render(request, "product.html",{'rental':rental, 'total_likes':count,'liked':liked})

def new(request):
    return render(request, "new.html")

def submit(request):
    rental = Rental()
    rental.product = request.POST['product']
    rental.writer = request.user
    rental.price = request.POST['price']
    rental.location_city = request.POST['city']
    rental.location_detail = request.POST['address']
    rental.rentterm = request.POST['rentterm']
    rental.information = request.POST['information']
    rental.chatting = request.POST['chatting']
    try:
        rental.images = request.FILES['images']
    except:
        pass
    rental.save()
    return redirect('product',rental.id)
    
def edit(request, rental_id):
    edit_rental = Rental.objects.get(id= rental_id)
    return render(request,'edit.html',{'rental':edit_rental})

def update(request, rental_id):
    update_rental = Rental.objects.get(id = rental_id)
    update_rental.product = request.POST['product']
    rental.writer = request.user
    update_rental.price = request.POST['price']
    update_rental.location_city = request.POST['city']
    update_rental.location_detail = request.POST['address']
    update_rental.rentterm = request.POST['rentterm']
    update_rental.information = request.POST['information']
    update_rental.chatting = request.POST['chatting']
    try:
        update_rental.images = request.FILES['images']
    except:
        pass
    update_rental.save()
    return redirect('product',update_rental.id)

def delete(request, rental_id):
    delete_rental = Rental.objects.get(id = rental_id)
    delete_rental.delete()
    return redirect('rentallist')


def search(request):
    search_keyword = request.GET.get('q')
    
    if len(search_keyword) >= 1 :
        rental_list = Rental.objects.filter(product=search_keyword)

    else : 
        rental_list = Rental.objects.all()
           

    return render(request, 'rental.html', {
        'rentals' : rental_list
    })

def like(request,rental_id):
    liked = get_object_or_404(Rental,pk = rental_id)
    if liked.like.filter(user = request.user).exists():
        liked.like.filter(user = request.user).delete()
    else:
        like = Like(
            user = request.user,
            rental = liked
        )
        like.save()
    return redirect('product',rental_id)
