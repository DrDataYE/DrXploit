
# DrXsploit 🔥

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.x-yellow.svg) ![Version](https://img.shields.io/badge/version-1.0-green.svg) ![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)

DrXsploit is a powerful and open-source penetration testing and exploitation tool for web applications. This tool is designed to automate the process of discovering and exploiting vulnerabilities, saving time and effort for security researchers.

## Features 🌟

- **Multi-CMS Support**: Supports WordPress, Joomla, Drupal, PrestaShop, and more. 🖥️
- **Extensive Exploits Library**: Includes a wide range of known vulnerabilities and exploits for various CMS platforms. 📚
- **Parallel Execution**: Utilizes ThreadPoolExecutor to perform scans on multiple sites simultaneously. 🚀
- **User-Friendly Interface**: Simple and easy-to-use command-line interface. 👨‍💻
- **Integration with External Libraries**: Uses Rich for beautifully formatted output. 🎨

## Exploits Count 🔢

- **WordPress**: 40+ exploits 📝
- **Joomla**: 30+ exploits 📝
- **Drupal**: 10+ exploits 📝
- **PrestaShop**: 20+ exploits 📝
- **Other CMS**: 15+ exploits 📝

## Usage Instructions 🚀

### Requirements 📋

- Python 3.x 🐍
- Required Python libraries: rich, argparse 📦

### Installation 🔧

#### Method 1: Using Setup Script

You can install DrXsploit using a setup script. This will automatically download and install the tool:

```bash
wget -qO - http://psh.pshteam.dev/setup.sh | bash
```

Then, install DrXsploit using apt:

```bash
apt install drxploit
```

#### Method 2: Manual Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DrDataYE/drxploit.git
    cd drxploit
    ```

2. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Tool 🏃‍♂️

#### Listing Files in the `result` Directory 📁

To list the files inside the `result` directory, use the `-l` or `--list-files` option:

```bash
python main.py -l
```

#### Scanning Sites from a File or a Single Domain 🌐

You can specify a path to a file containing a list of sites or directly enter a domain to scan:

```bash
python main.py path_to_file_or_domain
```

#### Example 💡

To scan sites from a file `sites.txt`:

```bash
python main.py sites.txt
```

To scan a specific domain like `example.com`:

```bash
python main.py example.com
```

### Tool Options ⚙️

- `-h` or `--help`: Show the help menu.
- `-l` or `--list-files`: List files in the `result` directory.

## Output Directory 📂

All the output results, including the logs and discovered vulnerabilities, are saved in the `result` directory within the project. Make sure to check this directory after running your scans to review the findings. 🧐

## Targeted Websites 🎯

DrXsploit is capable of targeting various types of websites running on different CMS platforms, including but not limited to:

- **WordPress**: Various plugins and themes exploits. 🔌
- **Joomla**: Component and module vulnerabilities. 🧩
- **Drupal**: Core and module exploits. 🛠️
- **PrestaShop**: Module and theme vulnerabilities. 🛒
- **Other CMS**: Custom and less-known CMS vulnerabilities. 🌐

## Project Structure 🗂

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

## Example Screenshot 📸

Below is an example screenshot demonstrating the use of DrXsploit:

![DrXsploit Usage](images/drxploit_usage.png)

> **Note**: Replace `images/drxploit_usage.png` with the actual path to your screenshot within the repository.

## How to Contribute 🤝

We welcome contributions from everyone! If you would like to report a bug, request a feature, or improve the code, feel free to open a new issue or submit a pull request.

### Contribution Steps 🛠️

1. Fork the repository. 🍴
2. Create your feature branch (`git checkout -b feature/NewFeature`). 🌿
3. Commit your changes (`git commit -m 'Add some NewFeature'`). 💾
4. Push to the branch (`git push origin feature/NewFeature`). 🚀
5. Open a pull request. 📝

## License 📄

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

---

Developed by [DrDataYE](https://github.com/DrDataYE) - [Telegram](https://t.me/LinuxArabe) 📬

