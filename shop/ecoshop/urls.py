from django.urls import path, re_path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("info/<str:ecoshop>/<slug:street>/<int:number>/", views.info_ecoshop, name="info_ecoshop"),
    path("goodscatalog/", views.goods_catalog, name="Goods catalog"),
    path("data/", views.data_views, name="data_views"),
    path("blog/",views.blog, name="blog"),
    path("products/checkout",views.checkout,name="checkout"),
    path("products/cart",views.cart,name="checkout"),
    path("pages/login", views.login, name="login"),
    path("pages/register", views.register, name="register"),
    path("pages/faq", views.faq, name="faq"),
    path("about_us/", views.about_us, name="about_us"),
    path("products/order_complete", views.order_complete,name="order_complete"),
    path("products/", views.products, name="products"),
    re_path(r"^regular/(?P<year>[12][09][89012][0-9])/?$", views.regular_views),

]
