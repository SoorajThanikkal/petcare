from django.shortcuts import render,redirect,get_object_or_404
from .models import userreg,product,PostModel,CommentSectionModel
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')  

def register(request):
    if request.method=='POST':
        profilepic=request.FILES.get('profilepic')
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        userreg(username=username,phone=phone,email=email,password=password,profilepic=profilepic).save()
        return redirect('index')
    return render(request,'register.html')
    

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=userreg.objects.filter(email=email,password=password).first()
        if user:
            request.session['email']=email
            return redirect('index')
        else:
            error_msg="Couldn't find your Account"
            return render(request,'login.html',{'error_msg':error_msg})
             
    return render(request,'login.html')

def home(request):
    return render(request,'home.html') 

def profile(request):
    email=request.session.get('email')
    if email:
        user=userreg.objects.get(email=email)
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('login')


from .models import product 
def addproduct(request):
    if request.method=='POST':
        productname=request.POST.get('productname')
        productprice=request.POST.get('productprice')
        category=request.POST.get('category')
        description=request.POST.get('description')
        image=request.FILES.get('image')

        product(productname=productname,productprice=productprice,category=category,description=description,image=image).save()
        return redirect('productlist')
    return render(request,'product.html')

def productlist(request):
    prod=product.objects.all()
    return render(request,'productlist.html',{'prod':prod})


def userlist(request):
    prof=userreg.objects.all()
    return render(request,'userlist.html',{'prof':prof}) 

def logout(request):
    request.session.flush()  
    return redirect('home') 

def editprofile(request):
    if request.method=='POST':
        email=request.session.get('email')
        user=userreg.objects.get(email=email)

        user.username=str(request.POST.get('username',user.username)),
        #user.password=request.POST.get('password',user.password),
        user.phone=int(request.POST.get('phone',user.phone)),

        if 'profilepic' in request.FILES:
            photo=request.FILES['profilepic']
            user.profilepic=photo

        user.save()

        return redirect('index')
    
    return render(request,'editprofile.html')

def deluser(request,id):
    temp=userreg.objects.get(id=id)
    temp.delete()
    return redirect('userlist')

def delproduct(request,id):
    d=product.objects.get(id=id)
    d.delete()
    return redirect('productlist')


#Post Section
def CreatePostView(request):
    email=request.session['email']
    if email:
        user_dtls=userreg.objects.get(email=email)
        if request.method == "POST":
            post_pic= request.FILES.get('post_pic')
            description = request.POST.get('description')
            like_count=0
            PostModel(user=user_dtls,post_pic=post_pic,description=description,likes_count=like_count).save()
            return redirect('home')
        else:
            return render(request,'addpost.html')
    else:
        return redirect('login')
        
def DisplayPostsView(request):
    posts = PostModel.objects.all()
    try:
        email = request.session['email']
    except:
        return redirect('login')
    
    if email:
        user = userreg.objects.get(email=email)
        liked_posts = user.liked_posts.all()
        post_comments = {}
        for post in posts:
            comments = CommentSectionModel.objects.filter(post=post)  # Fetch comments for each post
            post.comment_count = comments.count()
    else:
        liked_posts = []
    
    return render(request, 'viewallposts.html', {'posts': posts, 'liked_posts': liked_posts,'us': user})
def like_post(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    email = request.session.get('email')
    user = get_object_or_404(userreg, email=email)

    if post.liked_users.filter(email=email).exists():
        post.liked_users.remove(user)
        post.likes_count = max(0, post.likes_count - 1)
    else:
        post.liked_users.add(user)
        post.likes_count += 1

    post.save()
    return redirect('view_all_posts')
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(PostModel, id=post_id)
        comment_text = request.POST.get('comment')
        email = request.session.get('email')
        user = userreg.objects.get(email=email)
        
        if comment_text:
            CommentSectionModel.objects.create(
                user=user, 
                post=post, 
                comment=comment_text
            )
    return redirect('view_all_posts')


def DeleteCommentsView(request, cmt_id):
    comment = get_object_or_404(CommentSectionModel, id=cmt_id)
    email= request.session['email']
    user=userreg.objects.get(email=email)
    print(user)
    # Check if the logged-in user is the author of the comment
    if user == comment.user:
        comment.delete()
        return redirect('view_all_posts')
    else:
        return HttpResponse("You are not allowed to delete this comment.")
        
            
# Create your views here.
