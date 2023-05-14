%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(GC(.*)\\)|perl\\(Gtk2::(.*)\\)'
%endif

%define iconname gcstar.png

Summary:	A collection manager 
Name:		gcstar
Version:	1.8.0
Release:	1
License:	GPLv2+
Group:		Databases
URL:		https://gna.org/projects/gcstar/
Source0:	https://gitlab.com/GCstar/GCstar/-/archive/v%{version}/GCstar-v%{version}.tar.bz2
Requires:	perl-Gtk2
BuildRequires:	desktop-file-utils
BuildArch:	noarch

%description
Gcstar is an application that can manage multiple collections.
Movies, Books, Video games, Games, Music, Stamps, Vine, etc.
It builds upon gcfilm's legacy.
You can update your data directly from the Internet.

%prep
%autosetup -n GCstar-v%{version} -p1

%install
install -d %{buildroot}%{_bindir}
install bin/gcstar %{buildroot}%{_bindir}
install -d %{buildroot}%{_prefix}/lib
cp -a lib/gcstar %{buildroot}%{_prefix}/lib
install -d %{buildroot}%{_datadir}
cp -a share/* %{buildroot}%{_datadir}
install -d %{buildroot}%{_mandir}/man1
install man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

desktop-file-install --vendor='' \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category='Office;AudioVideo;GTK' \
	%{buildroot}%{_datadir}/applications/*.desktop

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
cp share/gcstar/icons/%{name}_48x48.png %{buildroot}%{_liconsdir}/%{iconname}
cp share/gcstar/icons/%{name}_32x32.png %{buildroot}%{_iconsdir}/%{iconname}
cp share/gcstar/icons/%{name}_16x16.png %{buildroot}%{_miconsdir}/%{iconname}

%files
%doc README CHANGELOG
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/applications/%{name}*
%{_datadir}/%{name}
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_mandir}/man1/%{name}*

