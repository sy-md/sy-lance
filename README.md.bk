# sy-lance

You gave me the pin; indeed, you did. And I turned into a lance 


git communication:

1: Make an SSH key 
2: eval $(ssh-agent -s) 
3: ssh-add {location of the id_rsa} 
4: copy the pub into the git hub key part


git remote set-url origin <NEW_GIT_URL_HERE>
git config --global user.name "Your Name"
git config --global user.email "email"

New workflow tools found for 2025

yazi
zellij








# sy_lance Rice Setup (2025)

A minimalist/cyberpunk-themed Linux/BSD rice focusing on productivity and TUI tools.  

## **🌿 Core System**
| Tool              | Purpose               | Alternatives          |
|-------------------|-----------------------|-----------------------|
| `ohmyzsh` + `powerlevel10k` | Shell + prompt       | Starship, fish        |
| `neofetch`        | System info           | fastfetch, pfetch     |
| `bpytop`         | Resource monitor      | btm (bottom), nvtop   |
| `feh`            | Wallpaper             | sxiv, nitrogen        |

## **🖥️ Window Management**
| Tool              | Purpose               | Alternatives          |
|-------------------|-----------------------|-----------------------|
| `polybar`        | Status bar            | eww (widgets), i3blocks|
| `picom`          | Compositor (blur/transparency) | jonaburg/picom (animations), Hyprland (Wayland) |

## **⌨️ Terminal & Productivity**
| Tool              | Purpose               | Alternatives          |
|-------------------|-----------------------|-----------------------|
| `zellij`         | Terminal multiplexer  | tmux, wezterm         |
| `yazi`           | File manager (TUI)    | lf, nnn               |
| `khal`           | Calendar (CLI)        | calcurse, todoman     |

## **✏️ Editors & Dev**
| Tool              | Purpose               | Alternatives          |
|-------------------|-----------------------|-----------------------|
| `neovim` + `airline` | Editor + statusline | lualine, feline       |

## **🔍 Launchers & Utilities**
| Tool              | Purpose               | Alternatives          |
|-------------------|-----------------------|-----------------------|
| `rofi`           | App launcher (X11)    | dmenu, fuzzel (Wayland) |
| `dunst`          | Notifications         | mako, swaync          |

---

## **✨ Optional Additions**
- **Theming**: `lxappearance` (GTK), `qt5ct` (Qt)  
- **Clipboard**: `wl-copy`/`xclip` + `clipmenu`  
- **Screenshots**: `flameshot` (X11), `grim` + `slurp` (Wayland)  
- **Audio**: `pavucontrol` (GUI), `ncpamixer` (TUI)  
- **PDF Reader**: `zathura` (keybind-focused)  

---

## **✅ Rice Checklist**
- [ ] Pick/create a **color scheme** (e.g., `pywal` or manual `.Xresources`).  
- [ ] Install **Nerd Fonts** for icons in Polybar/Neovim.  
- [ ] Map consistent **keyboard shortcuts** (e.g., `$mod + d` → rofi).  
- [ ] Backup **dotfiles** to GitHub (use `git` or `Chezmoi`).  

---

## **🎨 Theme Inspiration**
- **Cyberpunk**: Neon accents (e.g., `#00ff9d`) on dark backgrounds.  
- **Minimalist**: Monochrome + single highlight color (e.g., `#ff5555`).  

```sh
# Example command to clone dotfiles (replace URL):
git clone https://github.com/yourusername/sy_lance_dots.git ~/.config/sy_lance
```

*(Update this table as you refine your setup!)*






# installing Arch 

1. Oracle VM Setup
VM Configuration
OS Type: Linux (Arch 64-bit)

RAM: ≥2GB (recommended)

Storage: ≥20GB (dynamic VDI)

Network: NAT (or Bridged for SSH)

Enable EFI (Optional)
bash
# In Oracle VM settings:
System → Motherboard → Enable EFI
2. Arch Linux Installation
Boot & Connect to Internet
Boot the Arch ISO in VM.

Check internet:

bash
ping archlinux.org
(If no internet, run dhcpcd for DHCP.)

Partitioning (GPT + EFI)
bash
fdisk /dev/sda  # or /dev/nvme0n1 for NVMe  
Create partitions:

+512M (EFI, type EF00)

+4G (Swap, type 8200)

Remainder (Root, type 8300)

Format & Mount
bash
mkfs.fat -F32 /dev/sda1            # EFI  
mkswap /dev/sda2 && swapon /dev/sda2  # Swap  
mkfs.ext4 /dev/sda3                # Root  
mount /dev/sda3 /mnt  
mkdir /mnt/boot && mount /dev/sda1 /mnt/boot  
Install Base System
bash
pacstrap /mnt base linux linux-firmware vim  
genfstab -U /mnt >> /mnt/mnt/etc/fstab  
Chroot & Basic Setup
bash
arch-chroot /mnt  
ln -sf /usr/share/zoneinfo/Region/City /etc/localtime  
hwclock --systohc  
echo "myhostname" > /etc/hostname  
passwd  # Set root password  
Bootloader (GRUB)
bash
pacman -S grub efibootmgr  
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB  
grub-mkconfig -o /boot/grub/grub.cfg  
Reboot
bash
exit  
umount -R /mnt  
reboot  
3. Post-Install Essentials
User & Sudo
bash
useradd -m -G wheel username  
passwd username  
EDITOR=vim visudo  # Uncomment `%wheel ALL=(ALL) ALL`  
Network (Optional)
bash
pacman -S networkmanager  
systemctl enable --now NetworkManager  




