%define name    gcstar
%define version 1.3.1
%define release %mkrel 2
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
Patch0:     gcstar-1.3.1-fix-desktop-file.patch
BuildRoot:  %{_tmppath}/%{name}-root
Requires:   gtk2
BuildArch:  noarch 

%description
Gstar is an application that can manage multiple collections.
An expansion on gcfilms this is an alpha release but will be developed
as it's successor.
Currently Gstar only supports films.

%prep
%setup -q -n %{name}
%patch0 -p0
 
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
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname} 
%{_mandir}/man1/%{name}*
