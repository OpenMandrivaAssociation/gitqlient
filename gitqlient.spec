%global AName GitQlient
 
Name:       gitqlient
Version:    1.6.2
Release:    1
Summary:    Multi-platform Git client written with Qt
License:    LGPLv2+
URL:        https://github.com/francescmm/GitQlient
Source0:    %{url}/releases/download/v%{version}/%{name}_%{version}.tar.gz
 
BuildRequires: desktop-file-utils
BuildRequires: git-core
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)
 
Requires:   git-core
Requires:   hicolor-icon-theme
Requires:   %{_lib}qt5svg5
 
%description
GitQlient, pronounced as git+client (/gɪtˈklaɪənt/) is a multi-platform Git
client originally forked from QGit. Nowadays it goes beyond of just a fork and
adds a lot of new functionality.
 
Some of the major feature you can find are:
 
  * Easy access to remote actions like: push, pull, submodules management and
    branches
  * Branches management
  * Tags and stashes management
  * Submodules handling
  * Allow to open several repositories in the same window
  * Better visualization of the commits and the work in progress
  * Better visualization of the repository view
  * GitHub/GitLab integration
  * Embedded text editor with syntax highlight for C++

%prep
%autosetup -n %{name}_%{version} -p1
 
 
%build
%qmake_qt5 \
    PREFIX=%{_prefix} \
    %{AName}.pro
%make_build
 
%install
%make_install INSTALL_ROOT=%{buildroot}
 
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
 
%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.{png,svg}
