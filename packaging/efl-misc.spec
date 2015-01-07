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


%description
Elementary configuration files


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
%__cp etc/profile.d/* %{buildroot}%{_sysconfdir}/profile.d/

%post

%if %{with wayland}
f="/etc/profile.d/elm.sh"
grep --silent ELM_ENGINE "$f" \
    || printf "\nELM_ENGINE=wayland_shm\n[ ! -d /dev/dri ] || ELM_ENGINE=wayland_egl\nexport ELM_ENGINE" >> "$f"

%endif

chown root:root /etc/profile.d/elm.sh
chown root:root /etc/profile.d/evas.sh


%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_sysconfdir}/profile.d/*



