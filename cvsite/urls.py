from django_distill import distill_path as path  # from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #  path('admin/', admin.site.urls, name="admin"),  # admin not required for static site
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/Cell_Segmentation_with_nn-UNet/", views.work1, name="Cell Segmentation with nn-UNet"),
    path("projects/beta_amyloid_Detection_in_Lightsheet_Scan/", views.work2, name="β-amyloid Detection in Lightsheet Scan"),
    path("projects/QR_Code_Scavenge_in_Android/", views.project1, name="QR Code Scavenge in Android"),
    path("projects/Gazprea_Compiler/", views.project2, name="Gazprea Compiler"),
    path("projects/Running_ORB-SLAM_Algorithm_on_Robot_Car/", views.project3, name="Running ORB-SLAM Algorithm on Robot Car"),
    path("contact/", views.contact, name="contact"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
