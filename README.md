# sy-lance

You gave me the pin; indeed, you did. And I turned into a lance 


git communication:

1: Make an SSH key 
2: eval $(ssh-agent -s) 
3: ssh-add {location of the id_rsa} 
4: copy the pub into the git hub key part


git remote set-url origin <NEW_GIT_URL_HERE>

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












