Name:           deepin-system-monitor
Version:        5.6.1
Release:        1
Summary:        A more user-friendly system monitor
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        %{name}_%{version}.orig.tar.xz	
Source1:        %{name}-appdata.xml
Patch0:         0001-fix-building-error.patch

BuildRequires:  dtkwidget-devel >= 5.1
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires:  libpcap-devel
BuildRequires:  libcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  deepin-gettext-tools 
BuildRequires:  dtkwm-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  dtkcore-devel >= 5.1
BuildRequires:  libicu-devel
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
%{summary}.

%prep
%setup -q
%patch0 -p1

%build
export PATH=$PATH:/usr/lib64/qt5/bin
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dm644 %SOURCE1 %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc README.md
%license LICENSE
%caps(cap_kill,cap_net_raw,cap_dac_read_search,cap_sys_ptrace=+ep) %{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy

%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init
