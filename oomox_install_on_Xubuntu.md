### How to install oomox on XUbuntu ###

```bash

sudo apt install libgdk-pixbuf2.0-dev libxml2-utils gtk2-engines-murrine librsvg2-bin
sudo apt install sassc
git clone https://github.com/themix-project/oomox-gtk-theme.git
cd oomox-gtk-theme/
./change_color.sh -o themeName ./themeFile 


HDR_BG=510A11
HDR_FG=ffffff

BG=510A11
FG=ffffff

BTN_BG=510A11
BTN_FG=ffffff

HDR_BTN_BG=559999
HDR_BTN_FG=ffffff

SEL_BG=112200
SEL_FG=ffffff

TXT_BG=510A11
TXT_FG=ffffff

WM_BORDER_FOCUS=510A11
WM_BORDER_UNFOCUS=510A11


sudo add-apt-repository ppa:papirus/papirus
sudo apt-get update
sudo apt-get install papirus-folders

papirus-colors -l

paprirus-colors -C color


```
## colors available to papirus-folder

| Name | Preview | Name | Preview |
|:-----|:-------:|:-----|:-------:|
| **adwaita** | ![folder-adwaita](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-adwaita.svg) ![user-adwaita-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-adwaita-home.svg) ![folder-adwaita-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-adwaita-download.svg) | **black** | ![folder-black](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-black.svg) ![user-black-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-black-home.svg) ![folder-black-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-black-download.svg) |
| **blue** | ![folder-blue](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-blue.svg) ![user-blue-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-blue-home.svg) ![folder-blue-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-blue-download.svg) | **bluegrey** | ![folder-bluegrey](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-bluegrey.svg) ![user-bluegrey-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-bluegrey-home.svg) ![folder-bluegrey-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-bluegrey-download.svg) |
| **breeze** | ![folder-breeze](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-breeze.svg) ![user-breeze-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-breeze-home.svg) ![folder-breeze-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-breeze-download.svg) | **brown** | ![folder-brown](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-brown.svg) ![user-brown-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-brown-home.svg) ![folder-brown-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-brown-download.svg) |
| **carmine** | ![folder-carmine](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-carmine.svg) ![user-carmine-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-carmine-home.svg) ![folder-carmine-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-carmine-download.svg) | **cyan** | ![folder-cyan](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-cyan.svg) ![user-cyan-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-cyan-home.svg) ![folder-cyan-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-cyan-download.svg) |
| **darkcyan** | ![folder-darkcyan](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-darkcyan.svg) ![user-darkcyan-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-darkcyan-home.svg) ![folder-darkcyan-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-darkcyan-download.svg) | **deeporange** | ![folder-deeporange](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-deeporange.svg) ![user-deeporange-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-deeporange-home.svg) ![folder-deeporange-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-deeporange-download.svg) |
| **green** | ![folder-green](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-green.svg) ![user-green-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-green-home.svg) ![folder-green-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-green-download.svg) | **grey** | ![folder-grey](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-grey.svg) ![user-grey-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-grey-home.svg) ![folder-grey-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-grey-download.svg) |
| **indigo** | ![folder-indigo](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-indigo.svg) ![user-indigo-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-indigo-home.svg) ![folder-indigo-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-indigo-download.svg) | **magenta** | ![folder-magenta](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-magenta.svg) ![user-magenta-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-magenta-home.svg) ![folder-magenta-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-magenta-download.svg) |
| **nordic** | ![folder-nordic](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-nordic.svg) ![user-nordic-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-nordic-home.svg) ![folder-nordic-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-nordic-download.svg) | **orange** | ![folder-orange](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-orange.svg) ![user-orange-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-orange-home.svg) ![folder-orange-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-orange-download.svg) |
| **palebrown** | ![folder-palebrown](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-palebrown.svg) ![user-palebrown-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-palebrown-home.svg) ![folder-palebrown-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-palebrown-download.svg) | **paleorange** | ![folder-paleorange](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-paleorange.svg) ![user-paleorange-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-paleorange-home.svg) ![folder-paleorange-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-paleorange-download.svg) |
| **pink** | ![folder-pink](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-pink.svg) ![user-pink-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-pink-home.svg) ![folder-pink-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-pink-download.svg) | **red** | ![folder-red](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-red.svg) ![user-red-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-red-home.svg) ![folder-red-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-red-download.svg) |
| **teal** | ![folder-teal](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-teal.svg) ![user-teal-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-teal-home.svg) ![folder-teal-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-teal-download.svg) | **violet** | ![folder-violet](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-violet.svg) ![user-violet-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-violet-home.svg) ![folder-violet-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-violet-download.svg) |
| **white** | ![folder-white](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-white.svg) ![user-white-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-white-home.svg) ![folder-white-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-white-download.svg) | **yaru** | ![folder-yaru](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-yaru.svg) ![user-yaru-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-yaru-home.svg) ![folder-yaru-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-yaru-download.svg) |
| **yellow** | ![folder-yellow](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-yellow.svg) ![user-yellow-home](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/user-yellow-home.svg) ![folder-yellow-download](https://cdn.jsdelivr.net/gh/PapirusDevelopmentTeam/papirus-icon-theme@master/Papirus/48x48/places/folder-yellow-download.svg) |
