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
if [ -x "$(command -v apt-get)" ]; then
    URL="https://github.com/DrDataYE/DrXploit/releases/download/v1.0.0/drxploit_1.0.0_all_linux.deb"
elif [ -x "$(command -v pkg)" ]; then
    URL="https://github.com/DrDataYE/DrXploit/releases/download/v1.0.0/drxploit_1.0.0_all_termux.deb"
else
    print_error "Unsupported system. Only Linux and Termux are supported."
    exit 1
fi

# تحميل الملف بصمت
wget $URL -O drxploit.deb &> /dev/null

if [ $? -ne 0 ]; then
    print_error "Failed to download the package"
    exit 1
fi

# تثبيت الحزمة بصمت
if [ -x "$(command -v apt-get)" ]; then
    sudo dpkg -i drxploit.deb &> /dev/null
elif [ -x "$(command -v pkg)" ]; then
    pkg install ./drxploit.deb &> /dev/null
fi

if [ $? -ne 0 ]; then
    print_error "Failed to install the package"
    exit 1
fi

# تنظيف بصمت
rm drxploit.deb &> /dev/null

# رسالة للمستخدم
echo -e "${GREEN}Installation completed successfully!${NC}"
echo -e "${BLUE}You can now use the tool by typing:${NC} ${GREEN}drxploit${NC}"
