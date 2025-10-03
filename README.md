# DrXploit 🔥

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.x-yellow.svg) ![Version](https://img.shields.io/badge/version-1.0-green.svg) ![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)

DrXploit is an open-source web application security assessment toolkit. It automates the detection and verification of known vulnerabilities across popular CMS platforms, helping security researchers save time during authorized testing.

Use this tool only on systems you own or have explicit permission to test.

## Features 🌟

- Multi-CMS coverage: WordPress, Joomla, Drupal, PrestaShop, and more.
- Curated exploit checks: A broad collection of known issues for multiple CMS ecosystems.
- Parallel execution: ThreadPoolExecutor-based scanning of multiple targets.
- Simple CLI: Clean, easy-to-use command-line interface.
- Rich output: Nicely formatted console output via Rich.

## Exploits Count 🔢

- SITE: 158+ exploits

## Usage 🚀

### Requirements 📋

- Python 3.x
- Python packages: rich, argparse, bs4, requests, colorama

### Installation 🔧

#### Using setup script

```bash
git clone https://github.com/DrDataYE/DrXploit.git
cd DrXploit
bash setup.sh
```

> Note: The setup script installs dependencies and configures a launcher.

### Uninstallation 🧹

From the project directory:

```bash
bash uninstall.sh
```

For system-wide installs (e.g., if setup was run with sudo):

```bash
sudo bash uninstall.sh
```

The script removes installed files, the virtual environment, the launcher, and related PATH entries.

### Running 🏃‍♂️

#### List files in the result directory 📁

```bash
drxploit -l
```

#### Scan from a file or a single domain 🌐

```bash
drxploit path_to_file_or_domain
```

#### Add an email for important notifications 📧

```bash
drxploit -e "your_email@example.com"
```

#### Examples 💡

Scan domains from a file:

```bash
drxploit sites.txt
```

Scan a single domain:

```bash
drxploit example.com
```

### Options ⚙️

- -h, --help: Show help.
- -l, --list-files: List files in the result directory.
- -c, --list-cms: List files in the cms directory.
- -e, --email: Set an email address for important data.

## Output Directory 📂

All logs and findings are saved to the result directory in the project. Review this folder after scans to inspect results.

## Targeted Websites 🎯

DrXploit supports multiple CMS platforms, including:

- WordPress: Plugin and theme issues.
- Joomla: Component and module vulnerabilities.
- Drupal: Core and module checks.
- PrestaShop: Module and theme vulnerabilities.
- Other CMS: Custom and lesser-known platforms.

## Example Screenshot 📸

![DrXploit Usage](images/drxploit_usaged.jpg)

## Contributing 🤝

Contributions are welcome. Open an issue to report bugs or request features, or submit a pull request.

> Note: We do not condone unethical use of this tool.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Developed by [DrDataYE](https://github.com/DrDataYE) — [Telegram](https://t.me/Tryhacking) 📬
