Name:           deepin-system-monitor
Version:        5.6.11.13
Release:        1
Summary:        A more user-friendly system monitor
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz	

BuildRequires:  qt5-devel
BuildRequires:  cmake

BuildRequires:  dtkwidget-devel
BuildRequires:  dtkcore-devel
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkwm) >= 2.0

BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  libpcap-devel
BuildRequires:  libcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  deepin-gettext-tools 
BuildRequires:  libicu-devel
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup

%build
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
mkdir build && pushd build 
%cmake -DCMAKE_BUILD_TYPE=Release ../  -DAPP_VERSION=%{version} -DVERSION=%{version} 
%make_build  
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%caps(cap_kill,cap_net_raw,cap_dac_read_search,cap_sys_ptrace=+ep) %{_bindir}/%{name}
%{_bindir}/%{name} 
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy

%changelog
* Wed Jul 07 2021 weidong <weidong@uniontech.com> - 5.6.11.13-1
- Update to 5.6.11.13

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init

