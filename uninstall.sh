#!/bin/bash

set -euo pipefail

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

PROJECT_NAME="DrXploit"

has_write_access() {
    local target="$1"
    local dir="$target"
    if [ ! -d "$dir" ]; then
        dir="$(dirname "$dir")"
    fi
    [ -w "$dir" ] && [ -x "$dir" ]
}

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
PROFILE_CANDIDATES=()

case "$SYSTEM" in
    termux)
        DEFAULT_PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
        FALLBACK_PREFIX="$DEFAULT_PREFIX"
        PROFILE_CANDIDATES=("$HOME/.bashrc")
        ;;
    ish)
        DEFAULT_PREFIX="/usr/local"
        FALLBACK_PREFIX="$HOME/.local"
        PROFILE_CANDIDATES=("$HOME/.profile" "$HOME/.bashrc")
        ;;
    *)
        DEFAULT_PREFIX="/usr/local"
        FALLBACK_PREFIX="$HOME/.local"
        PROFILE_CANDIDATES=("$HOME/.bashrc" "$HOME/.profile" "$HOME/.zshrc" "$HOME/.zprofile" "$HOME/.config/fish/config.fish")
        ;;
 esac

PREFIX_CANDIDATES=()

add_candidate() {
    local candidate="$1"
    for existing in "${PREFIX_CANDIDATES[@]}"; do
        if [ "$existing" = "$candidate" ]; then
            return
        fi
    done
    PREFIX_CANDIDATES+=("$candidate")
}

add_candidate "$DEFAULT_PREFIX"
if [ -n "$FALLBACK_PREFIX" ]; then
    add_candidate "$FALLBACK_PREFIX"
fi

cleanup_profile() {
    local file="$1"
    [ -f "$file" ] || return

    local tmp
    tmp="$(mktemp)"
    awk '
        BEGIN { skip = 0 }
        {
            if (skip > 0) { skip--; next }
            if ($0 ~ /# Added by DrXploit installer/) { skip = 1; next }
            if ($0 ~ /drxploit/ && ($0 ~ /export PATH/ || $0 ~ /set -gx PATH/)) { next }
            print $0
        }
    ' "$file" > "$tmp" && mv "$tmp" "$file"
}

remove_path_entries() {
    for profile in "${PROFILE_CANDIDATES[@]}"; do
        cleanup_profile "$profile"
    done
}

remove_target() {
    local target="$1"
    local description="$2"

    if [ ! -e "$target" ]; then
        return 1
    fi

    if rm -rf "$target"; then
        print_success "Removed $description at $target"
        return 0
    else
        print_warn "Failed to remove $description at $target (insufficient permissions?)"
        return 2
    fi
}

any_removed=0

process_prefix() {
    local prefix="$1"
    local install_dir="$prefix/opt/drxploit"
    local bin_path="$prefix/bin/drxploit"

    if [ ! -d "$install_dir" ] && [ ! -e "$bin_path" ]; then
        return
    fi

    if ! has_write_access "$prefix/bin" || ! has_write_access "$install_dir"; then
        print_warn "No write access to $prefix. Try running with sudo if you want to remove this installation."
        return
    fi

    print_step "Cleaning installation under $prefix"

    local venv_dir=""
    if [ -f "$install_dir/.venv_path" ]; then
        read -r venv_dir < "$install_dir/.venv_path"
    fi

    if [ -z "$venv_dir" ]; then
        venv_dir="$install_dir/.venv"
    fi

    if [ -n "$venv_dir" ] && [ -d "$venv_dir" ]; then
        if remove_target "$venv_dir" "virtual environment"; then
            any_removed=1
        fi
    fi

    if remove_target "$install_dir" "installation directory"; then
        any_removed=1
    fi

    if [ -e "$bin_path" ]; then
        if remove_target "$bin_path" "launcher"; then
            any_removed=1
        fi
    fi

    if [ "$prefix" = "$FALLBACK_PREFIX" ] && [ "$DEFAULT_PREFIX" != "$FALLBACK_PREFIX" ]; then
        local data_home="${XDG_DATA_HOME:-$HOME/.local/share}"
        local user_data_dir="$data_home/$PROJECT_NAME"
        if [ -d "$user_data_dir" ]; then
            if remove_target "$user_data_dir" "user data"; then
                any_removed=1
            fi
        fi
    fi
}

for prefix in "${PREFIX_CANDIDATES[@]}"; do
    process_prefix "$prefix"
done

if [ "$DEFAULT_PREFIX" != "$FALLBACK_PREFIX" ]; then
    remove_path_entries
fi

if [ "$any_removed" -eq 1 ]; then
    print_success "Uninstallation completed."
else
    print_warn "No DrXploit installation artifacts were found to remove."
fi
