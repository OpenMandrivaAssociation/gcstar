%define name    gcstar
%define version 1.3.1
%define release %mkrel 1
%define iconname %{name}.png

%define title   Gcfilms

Summary:    A collection manager 
Name:       %{name}
Version:    %{version}
Release:    %{release}
License:    GPLv2+
Group:      Databases
URL:        https://gna.org/projects/gcstar/
Source:     http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-root
Requires:   gtk2
BuildArch:  noarch 
BuildRequires: desktop-file-utils

%description
Gstar is an application that can manage multiple collections.
An expansion on gcfilms this is an alpha release but will be developed
as it's successor.
Currently Gstar only supports films.

%prep
%setup -q -n %{name}
 
# %%build

# this doesn't work..
#./install --text --prefix=$RPM_BUILD_ROOT/usr 

%install

%{__mkdir_p} %{buildroot}%{_prefix}
%{__install} -d %{buildroot}%{_bindir}
%{__install} bin/gcstar %{buildroot}%{_bindir}
%{__install} -d %{buildroot}%{_prefix}/lib
%{__cp} -a lib/gcstar %{buildroot}%{_prefix}/lib
%{__install} -d %{buildroot}%{_datadir}
%{__cp} -a share/* %{buildroot}%{_datadir} 
%{__install} -d %{buildroot}%{_mandir}/man1
%{__install} man/%name.1 %{buildroot}%{_mandir}/man1/%name.1


mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
%{__cp} share/gcstar/icons/%{name}_48x48.png %{buildroot}%{_liconsdir}/%{iconname}
%{__cp} share/gcstar/icons/%{name}_32x32.png %{buildroot}%{_iconsdir}/%{iconname} 
%{__cp} share/gcstar/icons/%{name}_16x16.png %{buildroot}%{_miconsdir}/%{iconname} 
cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}):\
    command="%{name}" \
    icon="%{iconname}" \
    title="%{title}" \
    longtitle="Gcstar collection manager" \
    needs="x11" \
    section="%section" \
        xdg="true"
EOF

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="GTK" \
--add-category="Database" \
--add-category="X-MandrivaLinux-MoreApplications-Databases" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root) 
%doc README CHANGELOG
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/applications/%{name}*
%{_datadir}/%{name}
%{_menudir}/%{name}
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname} 
%{_mandir}/man1/%{name}*


