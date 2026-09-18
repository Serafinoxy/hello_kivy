[app]

title = HelloKivy
package.name = hellokivy
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 34
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

# Fix importante per buildozer moderno
android.enable_androidx = True
android.gradle_dependencies =

# Evita errori con SDK moderni
log_level = 2
warn_on_root = 1