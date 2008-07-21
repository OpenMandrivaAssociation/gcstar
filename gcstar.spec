%define name    gcstar
%define version 1.4.1
%define release %mkrel 1
%define iconname %{name}.png

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
BuildRequires: desktop-file-utils
BuildArch:  noarch 
Obsoletes:  gcfilms

%description
Gstar is an application that can manage multiple collections.
An expansion on gcfilms this is an alpha release but will be developed
as it's successor.
Currently Gstar only supports films.

%prep
%setup -q -n %{name}
 
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

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--add-category='Office;AudioVideo;GTK' \
	%buildroot%_datadir/applications/*.desktop

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
%{__cp} share/gcstar/icons/%{name}_48x48.png %{buildroot}%{_liconsdir}/%{iconname}
%{__cp} share/gcstar/icons/%{name}_32x32.png %{buildroot}%{_iconsdir}/%{iconname} 
%{__cp} share/gcstar/icons/%{name}_16x16.png %{buildroot}%{_miconsdir}/%{iconname} 

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

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
