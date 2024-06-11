
# DrXsploit 🔥

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-yellow.svg)
![Version](https://img.shields.io/badge/version-1.0-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)

DrXsploit هو أداة قوية ومفتوحة المصدر لاختبار الاختراق واستغلال الثغرات في مواقع الويب. تم تطوير هذه الأداة لتسهيل عملية اكتشاف الثغرات واستغلالها بشكل آلي، مما يوفر الوقت والجهد للباحثين الأمنيين.

## مميزات الأداة 🌟

- **دعم متعدد لأنظمة إدارة المحتوى**: يدعم WordPress، Joomla، Drupal، PrestaShop، وغيرها.
- **مكتبة كبيرة من الثغرات**: تتضمن ثغرات معروفة ومستغلة في أنظمة إدارة المحتوى المختلفة.
- **تنفيذ متوازي**: يستخدم ThreadPoolExecutor لتنفيذ الفحص على عدة مواقع في نفس الوقت.
- **سهولة الاستخدام**: واجهة سطر أوامر بسيطة وسهلة الاستخدام.
- **تكامل مع مكتبات خارجية**: يستخدم Rich لتنسيق المخرجات وتقديمها بشكل جميل.

## كيفية الاستخدام 🚀

### المتطلبات

- Python 3.x
- مكتبات Python المطلوبة: rich، argparse

### التثبيت

1. استنساخ المستودع:

    ```bash
    git clone https://github.com/DrDataYE/drxploit.git
    cd drxploit
    ```

2. تثبيت المتطلبات:

    ```bash
    pip install -r requirements.txt
    ```

### تشغيل الأداة

#### عرض الملفات في مجلد `result`

لعرض الملفات داخل مجلد `result`، يمكنك استخدام الخيار `-l` أو `--list-files`:

```bash
python main.py -l
```

#### فحص مواقع من ملف أو دومين محدد

يمكنك تحديد مسار ملف يحتوي على قائمة بالمواقع أو إدخال دومين مباشرة لفحصه:

```bash
python main.py path_to_file_or_domain
```

#### مثال

لفحص المواقع من ملف `sites.txt`:

```bash
python main.py sites.txt
```

لفحص دومين محدد مثل `example.com`:

```bash
python main.py example.com
```

### خيارات الأداة

- `-h` أو `--help`: عرض قائمة المساعدة.
- `-l` أو `--list-files`: عرض الملفات في مجلد `result`.

## هيكلية المشروع 🗂

```
drxploit/
├── bin/
├── BruteForce/
├── cms/
├── core/
├── exploits/
├── files/
├── lists/
├── result/
├── tools/
├── main.py
├── LICENSE
└── README.md
```

## المساهمة 🤝

نرحب بالمساهمات من الجميع! إذا كنت ترغب في الإبلاغ عن خطأ أو طلب ميزة جديدة أو تحسين الكود، فلا تتردد في فتح قضية جديدة أو إرسال طلب سحب.

## الرخصة 📄

هذا المشروع مرخص تحت رخصة MIT. لمزيد من التفاصيل، انظر ملف [LICENSE](LICENSE).

---

بواسطة [DrDataYE](https://github.com/DrDataYE) - [Telegram](https://t.me/LinuxArabe)

