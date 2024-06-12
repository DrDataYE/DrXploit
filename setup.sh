#!/bin/bash

# ألوان
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # لا لون

# دالة للطباعة الملونة
print_step() {
    echo -e "[${BLUE}*${NC}] $1"
}

print_success() {
    echo -e "[${GREEN}+${NC}] $1"
}

print_error() {
    echo -e "[${RED}-${NC}] $1"
}

# تحديد النظام المناسب
if [ -x "$(command -v pkg)" ]; then
    print_step "Detected Termux system"
    URL="https://github.com/DrDataYE/DrXploit/releases/download/v1.0.0/drxploit_1.0.0_all_termux.deb"
elif [ -x "$(command -v apt-get)" ]; then
    print_step "Detected Linux system"
    URL="https://github.com/DrDataYE/DrXploit/releases/download/v1.0.0/drxploit_1.0.0_all_linux.deb"
else
    print_error "Unsupported system. Only Linux and Termux are supported."
    exit 1
fi

# تحميل الملف بصمت
print_step "Downloading package..."
wget $URL -O drxploit.deb &> /dev/null

if [ $? -ne 0 ]; then
    print_error "Failed to download the package"
    exit 1
fi

print_success "Package downloaded successfully"

# تثبيت الحزمة
print_step "Installing the package"
if [ -x "$(command -v apt-get)" ]; then
    dpkg -i drxploit.deb
elif [ -x "$(command -v pkg)" ]; then
    pkg install ./drxploit.deb
fi

if [ $? -ne 0 ]; then
    print_error "Failed to install the package"
    exit 1
fi

print_success "Package installed successfully"

# تنظيف
print_step "Cleaning up"
rm drxploit.deb


# رسالة للمستخدم
print_success "Installation completed successfully!"
print_success "You can now use the tool by typing: ${GREEN}drxploit${NC}"
