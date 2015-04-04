%bcond_with wayland

Name:       efl-misc
Summary:    Elementary config files
Version:    0.1.31
Release:    0
Group:      Graphics & UI Framework/Development
License:    LGPL-2.1
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
Source1001: efl-misc.manifest
BuildRequires: eet-tools


%description
Elementary configuration files


%prep
%setup -q
cp %{SOURCE1001} .


%build
make

%install
make install prefix=%{_prefix} DESTDIR=%{buildroot}

%post

%if %{with wayland}
f="/etc/profile.d/efl.sh"
grep --silent ELM_ENGINE "$f" \
    || printf "\nELM_ENGINE=wayland_shm\n[ ! -d /dev/dri ] || ELM_ENGINE=wayland_egl" >> "$f"
%endif

%files
%defattr(-,root,root,-)
%license COPYING
%{_sysconfdir}/profile.d/*
%{_datadir}/elementary/config/*
%manifest %{name}.manifest
