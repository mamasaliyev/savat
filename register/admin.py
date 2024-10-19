from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from news.models import News, Comment  # 2-chi app modellarini import qilish
from savatcha.models import Mahsulot, Savat  # 3-chi app modellarini import qilish

# CustomUserAdmin klassi
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_picture', 'phone_number')}),  # Custom fieldlar
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_picture', 'phone_number')}),  # Qo'shiladigan fieldlar
    )

# NewsAdmin klassi
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'likes', 'created_at', 'updated_at')  # Qaysi maydonlarni ko'rsatish
    search_fields = ('title', 'description')  # Qidiruv uchun maydonlar
    list_filter = ('likes', 'user')  # Filtrlar
    ordering = ('-created_at',)  # Tartibga solish

# CommentAdmin klassi
class CommentAdmin(admin.ModelAdmin):
    list_display = ('news', 'user', 'created_at')  # Qaysi maydonlarni ko'rsatish
    search_fields = ('content',)  # Qidiruv uchun maydonlar
    ordering = ('-created_at',)  # Tartibga solish
    list_filter = ('user',)  # Filtrlar

# MahsulotAdmin klassi
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'quantity', 'user')  # Qaysi maydonlarni ko'rsatish

# SavatAdmin klassi
class SavatAdmin(admin.ModelAdmin):
    list_display = ('mahsulot_id', 'miqdor')  # Qaysi maydonlarni ko'rsatish

# Admin panelga barcha modellarning admin klasslarini ro'yxatdan o'tkazish
admin.site.register(CustomUser, CustomUserAdmin)  # CustomUser modelini ro'yxatdan o'tkazish
admin.site.register(News, NewsAdmin)  # News modelini ro'yxatdan o'tkazish
admin.site.register(Comment, CommentAdmin)  # Comment modelini ro'yxatdan o'tkazish
admin.site.register(Mahsulot, MahsulotAdmin)  # Mahsulot modelini ro'yxatdan o'tkazish
admin.site.register(Savat, SavatAdmin)  # Savat modelini ro'yxatdan o'tkazish
