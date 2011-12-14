%define iconname gcstar.png

Summary:	A collection manager 
Name:		gcstar
Version:	1.6.2
Release:	%mkrel 3
License:	GPLv2+
Group:		Databases
URL:		https://gna.org/projects/gcstar/
Source:		http://download.gna.org/gcstar/%{name}-%{version}.tar.gz
Patch0:		gcstar-1.6.2-ru.patch
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	gtk2
BuildRequires:	desktop-file-utils
BuildArch:	noarch
Obsoletes:	gcfilms
Provides:	perl(GCItemsLists::GCImageLists) perl(GCItemsLists::GCTextLists)
Provides:	perl(GCPlugins::GCfilms::GCThemoviedb)

%description
Gcstar is an application that can manage multiple collections.
Movies, Books, Video games, Games, Music, Stamps, Vine, etc.
It builds upon gcfilm's legacy.
You can update your data directly from the Internet.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .ru

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_prefix}
%__install -d %{buildroot}%{_bindir}
%__install bin/gcstar %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_prefix}/lib
%__cp -a lib/gcstar %{buildroot}%{_prefix}/lib
%__install -d %{buildroot}%{_datadir}
%__cp -a share/* %{buildroot}%{_datadir}
%__install -d %{buildroot}%{_mandir}/man1
%__install man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

desktop-file-install --vendor='' \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category='Office;AudioVideo;GTK' \
        %{buildroot}%{_datadir}/applications/*.desktop

%__mkdir_p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
%__cp share/gcstar/icons/%{name}_48x48.png %{buildroot}%{_liconsdir}/%{iconname}
%__cp share/gcstar/icons/%{name}_32x32.png %{buildroot}%{_iconsdir}/%{iconname}
%__cp share/gcstar/icons/%{name}_16x16.png %{buildroot}%{_miconsdir}/%{iconname}

%clean
rm -rf %{buildroot}

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

