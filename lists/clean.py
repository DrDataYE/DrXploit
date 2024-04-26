import argparse

def clean_data(file_path):
    # قراءة البيانات من الملف
    with open(file_path, "r") as file:
        lines = file.readlines()

    # إزالة التواريخ من كل سطر
    cleaned_lines = [line.split()[0] + '\n' for line in lines if line.strip()]

    # إعادة كتابة البيانات المنظفة في الملف نفسه
    with open(file_path, "w") as file:
        file.writelines(cleaned_lines)

def main():
    # إنشاء محلل الأوامر
    parser = argparse.ArgumentParser(description="Clean dates from file entries.")
    # إضافة وسيطة لمسار الملف
    parser.add_argument("file_path", type=str, help="The path to the file to be cleaned.")
    # تحليل الوسائط
    args = parser.parse_args()

    # استدعاء الدالة لتنظيف البيانات
    clean_data(args.file_path)

if __name__ == "__main__":
    main()


