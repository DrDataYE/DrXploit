#!/bin/bash

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m'

print_step() {
    echo -e "[${BLUE}*${NC}] $1"
}

print_success() {
    echo -e "[${GREEN}+${NC}] $1"
}

print_warn() {
    echo -e "[${YELLOW}!${NC}] $1"
}

print_error() {
    echo -e "[${RED}-${NC}] $1" >&2
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_NAME="DrXploit"

detect_system() {
    if [ -n "${TERMUX_VERSION-}" ] || command -v termux-info >/dev/null 2>&1 || command -v pkg >/dev/null 2>&1; then
        echo "termux"
    elif [ -n "${ISH_VERSION-}" ] || [ "$(uname -o 2>/dev/null)" = "iSH" ]; then
        echo "ish"
    elif [ "$(uname -s)" = "Linux" ]; then
        echo "linux"
    else
        echo "unknown"
    fi
}

SYSTEM="$(detect_system)"

if [ "$SYSTEM" = "unknown" ]; then
    print_error "Unsupported system. Supported environments: Termux, Linux, iSH."
    exit 1
fi

print_step "Detected system: $SYSTEM"

DEFAULT_PREFIX=""
FALLBACK_PREFIX=""
BIN_DIR=""
INSTALL_DIR=""
PKG_INSTALLER=()
PKG_NEEDS_ROOT=0
REQUIRED_PKGS=()

case "$SYSTEM" in
    termux)
        DEFAULT_PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
        FALLBACK_PREFIX="$DEFAULT_PREFIX"
        PKG_INSTALLER=(pkg install -y)
        REQUIRED_PKGS=(python git)
        ;;
    ish)
        DEFAULT_PREFIX="/usr/local"
        FALLBACK_PREFIX="$HOME/.local"
        PKG_INSTALLER=(apk add --no-cache)
        REQUIRED_PKGS=(python3 py3-pip git)
        ;;
    linux)
        DEFAULT_PREFIX="/usr/local"
        FALLBACK_PREFIX="$HOME/.local"
        if command -v apt-get >/dev/null 2>&1; then
            PKG_INSTALLER=(apt-get install -y)
            PKG_NEEDS_ROOT=1
            REQUIRED_PKGS=(python3 python3-venv python3-pip git)
        elif command -v dnf >/dev/null 2>&1; then
            PKG_INSTALLER=(dnf install -y)
            PKG_NEEDS_ROOT=1
            REQUIRED_PKGS=(python3 python3-venv python3-pip git)
        elif command -v pacman >/dev/null 2>&1; then
            PKG_INSTALLER=(pacman -S --noconfirm)
            PKG_NEEDS_ROOT=1
            REQUIRED_PKGS=(python python-virtualenv python-pip git)
        else
            print_warn "No supported package manager detected. Ensure python3, pip, and git are installed."
        fi
        ;;
esac

has_write_access() {
    local target="$1"
    local dir="$target"
    if [ ! -d "$dir" ]; then
        dir="$(dirname "$dir")"
    fi
    [ -w "$dir" ] && [ -x "$dir" ]
}

SELECTED_PREFIX="$DEFAULT_PREFIX"

if [ -n "$FALLBACK_PREFIX" ] && [ "$DEFAULT_PREFIX" != "$FALLBACK_PREFIX" ]; then
    if ! has_write_access "$DEFAULT_PREFIX/bin" || ! has_write_access "$DEFAULT_PREFIX/opt"; then
        print_warn "Cannot write to $DEFAULT_PREFIX; falling back to $FALLBACK_PREFIX"
        SELECTED_PREFIX="$FALLBACK_PREFIX"
    else
        print_step "Using system prefix: $DEFAULT_PREFIX"
    fi
else
    SELECTED_PREFIX="$DEFAULT_PREFIX"
fi

PREFIX="$SELECTED_PREFIX"
BIN_DIR="$PREFIX/bin"
INSTALL_DIR="$PREFIX/opt/drxploit"

if [[ "$PREFIX" == "$FALLBACK_PREFIX" && "$PREFIX" != "$DEFAULT_PREFIX" ]]; then
    DATA_HOME="${XDG_DATA_HOME:-$HOME/.local/share}"
    USER_DATA_DIR="$DATA_HOME/$PROJECT_NAME"
else
    USER_DATA_DIR="$INSTALL_DIR"
fi

install_dependencies() {
    if [ "${#REQUIRED_PKGS[@]}" -eq 0 ]; then
        return
    fi

    if [ "${#PKG_INSTALLER[@]}" -eq 0 ]; then
        print_warn "Skipping automatic dependency installation."
        return
    fi

    print_step "Installing dependencies: ${REQUIRED_PKGS[*]}"

    if [ $PKG_NEEDS_ROOT -eq 1 ] && [ "$EUID" -ne 0 ]; then
        if command -v sudo >/dev/null 2>&1; then
            sudo "${PKG_INSTALLER[@]}" "${REQUIRED_PKGS[@]}"
        else
            print_error "Root privileges required to install dependencies. Please rerun with sudo or install manually."
            exit 1
        fi
    else
        "${PKG_INSTALLER[@]}" "${REQUIRED_PKGS[@]}"
    fi
}

install_dependencies

PYTHON_BIN="$(command -v python3 || command -v python || true)"
if [ -z "$PYTHON_BIN" ]; then
    print_error "Python 3 is required but was not found."
    exit 1
fi

print_step "Using python interpreter: $PYTHON_BIN"

mkdir -p "$BIN_DIR"
mkdir -p "$(dirname "$INSTALL_DIR")"
mkdir -p "$USER_DATA_DIR"

if [ -d "$INSTALL_DIR" ]; then
    print_step "Removing previous installation at $INSTALL_DIR"
    rm -rf "$INSTALL_DIR"
fi

print_step "Copying project files to $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
cp -a "$SCRIPT_DIR"/. "$INSTALL_DIR"/
rm -rf "$INSTALL_DIR/.git" "$INSTALL_DIR/.github" 2>/dev/null || true

VENV_DIR="$USER_DATA_DIR/.venv"
if [ -d "$VENV_DIR" ]; then
    print_step "Removing previous virtual environment at $VENV_DIR"
    rm -rf "$VENV_DIR"
fi

print_step "Creating virtual environment at $VENV_DIR"
"$PYTHON_BIN" -m venv "$VENV_DIR"

PIP_BIN="$VENV_DIR/bin/pip"

print_step "Upgrading pip"
"$PIP_BIN" install --upgrade pip

print_step "Installing Python requirements"
"$PIP_BIN" install -r "$INSTALL_DIR/requirements.txt"

echo "$VENV_DIR" > "$INSTALL_DIR/.venv_path"

print_step "Deploying launcher to $BIN_DIR"
install -m 755 "$INSTALL_DIR/bin/drxploit" "$BIN_DIR/drxploit"

print_success "$PROJECT_NAME installed successfully!"

if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    export PATH="$BIN_DIR:$PATH"
fi

ensure_path_config() {
    local target_dir="$1"

    local shell_name
    shell_name="$(basename "${SHELL:-}")"
    local profile_candidates=()

    case "$SYSTEM" in
        termux)
            profile_candidates=("$HOME/.bashrc")
            ;;
        ish)
            profile_candidates=("$HOME/.profile" "$HOME/.bashrc")
            ;;
        *)
            case "$shell_name" in
                bash)
                    profile_candidates=("$HOME/.bashrc" "$HOME/.profile")
                    ;;
                zsh)
                    profile_candidates=("$HOME/.zshrc" "$HOME/.zprofile" "$HOME/.profile")
                    ;;
                fish)
                    profile_candidates=("$HOME/.config/fish/config.fish")
                    ;;
                *)
                    profile_candidates=("$HOME/.profile" "$HOME/.bashrc")
                    ;;
            esac
            ;;
    esac

    local profile=""
    for candidate in "${profile_candidates[@]}"; do
        if [ -f "$candidate" ]; then
            profile="$candidate"
            break
        fi
    done

    if [ -z "$profile" ]; then
        profile="${profile_candidates[0]}"
    fi

    mkdir -p "$(dirname "$profile")"
    touch "$profile"

    if grep -Fq "$target_dir" "$profile"; then
        print_step "PATH entry already configured in $profile"
    else
        print_step "Adding $target_dir to PATH via $profile"
        {
            echo ""
            echo "# Added by $PROJECT_NAME installer on $(date +'%Y-%m-%d %H:%M:%S')"
            if [[ "$profile" == *"config.fish" ]]; then
                echo "set -gx PATH $target_dir \$PATH"
            else
                echo "export PATH=\"$target_dir:\$PATH\""
            fi
        } >> "$profile"
        print_success "Updated $profile. Reload your shell or run: source $profile"
    fi
}

NEED_PROFILE_UPDATE=0
if [ "$PREFIX" = "$FALLBACK_PREFIX" ] && [ "$DEFAULT_PREFIX" != "$FALLBACK_PREFIX" ]; then
    NEED_PROFILE_UPDATE=1
elif [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    NEED_PROFILE_UPDATE=1
fi

if [ "$NEED_PROFILE_UPDATE" -eq 1 ]; then
    ensure_path_config "$BIN_DIR"
fi

print_success "You can now run the tool with: ${GREEN}drxploit${NC}"
